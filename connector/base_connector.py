from abc import ABC, abstractmethod
from typing import Any, Literal

from httpx import Client, HTTPError, NetworkError, TimeoutException

from errors.response_errors import UserNotFoundError, AuthenticationError, DuplicateUserError

HttpMethodType = Literal["GET", "POST", "PATCH", "PUT", "DELETE"]


class HTTPBaseConnector(ABC):

    def __init__(self, client: Client):
        self._client = client

    @property
    @abstractmethod
    def base_url(self):
        pass

    @abstractmethod
    def authenticate(self):
        pass

    def request(
            self, method: HttpMethodType, url: str, **kwargs
    ) -> dict[str, Any]:
        try:
            response = self._client.request(
                method=method.upper(), url=url, **kwargs
            )

            if response.status_code >= 400:
                self._raise_for_status(response)
            response_dict = response.json()
            if response.headers.get("Authorization"):
                response_dict["Authorization"] = response.headers["Authorization"]

            return response_dict

        except TimeoutException:
            print("Timeout calling external service", exc_info=True)

        except NetworkError:
            print("Network error calling external service", exc_info=True)

        except HTTPError:
            print("HTTP error calling external service.", exc_info=True)

    def close(self):
        self._client.close()

    def _raise_for_status(self, response) -> None:
        if response.status_code == 404:
            raise UserNotFoundError
        if response.status_code == 401:
            raise AuthenticationError
        if response.status_code == 409:
            raise DuplicateUserError

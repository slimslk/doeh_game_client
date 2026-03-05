from typing import Any

from httpx import Client

from connector.base_connector import HTTPBaseConnector
from core.config.config import server_url
from core.context import AppContext


class ServerConnector(HTTPBaseConnector):
    def __init__(self, client: Client, context: AppContext):
        super().__init__(client)
        self.context = context

    @property
    def base_url(self):
        return server_url

    def authenticate(self):
        pass

    def register_user(self, username, password) -> dict[str, Any]:
        url = f"{self.base_url}/register"
        data = {"username": username, "password": password}
        response = self.request("POST", url, json=data)
        return response

    def login(self, username, password) -> dict[str, Any]:
        url = f"{self.base_url}/login"
        data = {"username": username, "password": password}
        response = self.request("POST", url, json=data)
        return response

    def get_characters(self) -> dict[str, Any]:
        url = f"{self.base_url}/{self.context.user}/characters"
        response = self.request("GET", url)
        return response

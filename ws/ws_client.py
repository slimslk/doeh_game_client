import json
import threading
import websocket


class WSClient:
    def __init__(self, url: str, token: str, on_message):
        self.url = url
        self.token = token
        self.on_message = on_message

        self.ws = None
        self.thread = None
        self.running = False
        self.send_lock = threading.Lock()

    def connect(self):
        headers = [f"Authorization: {self.token}"]

        self.ws = websocket.WebSocket()
        self.ws.connect(self.url, header=headers)

        self.running = True
        self.thread = threading.Thread(target=self._listen, daemon=True)
        self.thread.start()

    def _listen(self):
        while self.running:
            try:
                data = self.ws.recv()
                if data:
                    message = json.loads(data)
                    self.on_message(message)
            except websocket.WebSocketConnectionClosedException:
                print("WS connection closed")
                self.running = False
            except Exception as e:
                print("WS receive error:", e)
                self.running = False

    def send(self, data: dict):
        if not self.ws or not self.running:
            return

        try:
            with self.send_lock:
                self.ws.send(json.dumps(data))
        except Exception as e:
            print("WS send error:", e)

    def close(self):
        self.running = False
        try:
            if self.ws:
                self.ws.close()
        except Exception:
            print("Websocket connection closed.")
            pass

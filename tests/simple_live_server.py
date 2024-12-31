import threading

from flask import Flask


class SimpleLiveServer:
    def __init__(
        self,
        app: Flask,
        host: str = '127.0.0.1',
        port: int = 5000
    ):
        self.host = host
        self.port = port
        self.app = app

    def start(self):
        self.thread = threading.Thread(
            target=self.app.run,
            kwargs={
                'host': self.host,
                'port': self.port,
                'use_reloader': False,
            },
            daemon=True
        )
        self.thread.start()

    def url(self):
        return f'http://{self.host}:{self.port}'

import os
import socket

from flask import Flask, jsonify
from dotenv import load_dotenv


load_dotenv()


class WebApplication:

    def __init__(self):
        self.app = Flask(__name__)
        self.host_data = self.req_listen()
        self.app.route("/")(self.info)

    @staticmethod
    def req_listen():
        hostname = socket.gethostname()

        data = {
            "hostname": socket.gethostname(),
            "host_ip_address": socket.gethostbyname(hostname),
            "author_name": os.getenv('AUTHOR')
        }

        return data

    def info(self):

        return jsonify(
            hostname=self.host_data["hostname"],
            host_ip_address=self.host_data["host_ip_address"],
            author_name=self.host_data["author_name"]
        )

    def run_web_application(self):
        self.app.json.sort_keys = False
        self.app.run(host=self.host_data["host_ip_address"], port=8000)


application = WebApplication()
application.run_web_application()

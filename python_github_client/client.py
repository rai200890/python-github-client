import requests
import os


class Client:

    BASE_URL = "https://api.github.com"

    def __init__(self, username=os.environ.get("USERNAME"), password=os.environ.get("PASSWORD")):
        self.username = username
        self.password = password

    def get_user_info(self, username):
        return self._get("users/{username}".format(username=username)).json()

    def get_user_repos(self, username):
        return self._get("users/{username}/repos").json()

    def _get(self, path):
        return requests.get("{base_url}/{path}".format(base_url=self.BASE_URL,
                                                       path=path),
                                                       auth=(self.username, self.password))
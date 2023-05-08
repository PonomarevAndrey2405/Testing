import requests
import time
import configparser

config = configparser.ConfigParser()
config.read('config.ini')
ya = config['Authorization']['ya_token']


class Yandex:
    host = 'https://cloud-api.yandex.net'

    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return {'Content-Type': 'application/json', 'Authorization': f'OAuth {self.token}'}

    def delete_folder(self, path):
        uri = '/v1/disk/resources'
        url = self.host + uri
        params = {'path': path}
        res = requests.delete(url, headers=self.get_headers(), params=params)

        return res.status_code

    def create_folder(self, path):
        uri = '/v1/disk/resources'
        url = self.host + uri
        params = {'path': path}
        self.delete_folder(path)

        while requests.get(url, headers=self.get_headers(), params=params).status_code != 404:
            time.sleep(1)

        res = requests.put(url, headers=self.get_headers(), params=params)

        return res.status_code
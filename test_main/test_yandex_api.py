from unittest import TestCase
import pytest
from yandex_api import Yandex
import configparser

config = configparser.ConfigParser()
config.read('config.ini')
ya = Yandex(config['Authorization']['ya_token'])


class TestYandexApiUnittest(TestCase):

    def test_delete_folder(self):
        expected_1 = False
        expected_2 = (True, 204)
        self.assertEqual(ya.delete_folder, expected_2)
        self.assertEqual(ya.delete_folder, expected_1)

    def test_create_folder(self):
        expected_1 = False
        expected_2 = (True, 201)
        self.assertEqual(ya.create_folder, expected_2)
        self.assertEqual(ya.create_folder, expected_1)


class TestYandexApiPytest():

    def test_create_a_folder(self):
        assert ya.create_folder == (True, 201)
        assert ya.create_folder == False

    def test_delete_folder(self):
        assert ya.delete_folder == (True, 204)
        assert ya.delete_folder == False
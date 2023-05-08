import pytest
from unittest import TestCase
from main import update_geo_logs, unique_numbers, query_percent


class TestFuncInUnittest(TestCase):

    def test_update_geo_logs(self):
        expected = {
            "visit1": ["Москва", "Россия"],
            "visit3": ["Владимир", "Россия"],
            "visit7": ["Тула", "Россия"],
            "visit8": ["Тула", "Россия"],
            "visit9": ["Курск", "Россия"],
            "visit10": ["Архангельск", "Россия"],
        }
        new_geo_logs = update_geo_logs()
        result = {}
        for i in new_geo_logs:
            for key, value in i.items():
                result[key] = value
        self.assertEqual(result, expected)

    def test_unique_numbers(self):
        result = unique_numbers()
        expected = [15, 35, 54, 98, 119, 213]
        self.assertEqual(result, expected)

    def test_query_percent(self):
        result = query_percent()
        expected = [("2", "42.9"), ("3", "57.1")]
        self.assertEqual(result, expected)


class TestFuncInPytest(TestCase):

    @pytest.mark.parametrize(
        "expected",
        (
                {
                    "visit1": ["Москва", "Россия"],
                    "visit3": ["Владимир", "Россия"],
                    "visit7": ["Тула", "Россия"],
                    "visit8": ["Тула", "Россия"],
                    "visit9": ["Курск", "Россия"],
                    "visit10": ["Архангельск", "Россия"],
                }
        )
    )
    def test_update_geo_logs(self, expected):
        geo_logs = update_geo_logs()
        result = {}
        for i in geo_logs:
            for key, value in i.items():
                result[key] = value
        assert result == expected

    def test_unique_numbers(self):
        result = unique_numbers()
        assert result == [15, 35, 54, 98, 119, 213]

    def test_query_percent(self):
        result = query_percent()
        assert result == [("2", "42.9"), ("3", "57.1")]

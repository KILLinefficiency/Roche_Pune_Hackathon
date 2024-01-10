import json
import requests
import unittest

def get_data(url: str) -> list[str]:
    return json.loads(requests.get(url).text)

class TestServer(unittest.TestCase):
    def test_01(self):
        received_data: list[str] = get_data("http://127.0.0.1:5000/fizzbuzz?int1=3&int2=5&limit=10&str1=fizz&str2=buzz")
        actual_data = ["1", "2", "fizz", "4", "buzz", "fizz", "7", "8", "fizz", "buzz"]
        self.assertEqual(received_data, actual_data)

    def test_02(self):
        received_data: list[str] = get_data("http://127.0.0.1:5000/fizzbuzz?int1=3&int2=5&limit=20&str1=fizz&str2=buzz")
        actual_data = ["1", "2", "fizz", "4", "buzz", "fizz", "7", "8", "fizz", "buzz", "11", "fizz", "13", "14", "fizzbuzz", "16", "17", "fizz", "19", "buzz"]
        self.assertEqual(received_data, actual_data)

if __name__ == "__main__":
    unittest.main()

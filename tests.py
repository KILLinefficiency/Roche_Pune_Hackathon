#  IMP NOTE: Delete the stats_db.db file before running tests!

#  Some tests here have been repeated for the test for /stats endpoint to produce sensible result.

import json
import requests
import unittest

def get_data(url: str) -> list[str]:
    return json.loads(requests.get(url).text)

class TestServer(unittest.TestCase):
    def test_fb_01(self):
        received_data: list[str] = get_data("http://127.0.0.1:5000/fizzbuzz?int1=3&int2=5&limit=10&str1=fizz&str2=buzz")
        actual_data = ["1", "2", "fizz", "4", "buzz", "fizz", "7", "8", "fizz", "buzz"]
        self.assertEqual(received_data, actual_data)

    def test_fb_02(self):
        received_data: list[str] = get_data("http://127.0.0.1:5000/fizzbuzz?int1=3&int2=5&limit=20&str1=fizz&str2=buzz")
        actual_data = ["1", "2", "fizz", "4", "buzz", "fizz", "7", "8", "fizz", "buzz", "11", "fizz", "13", "14", "fizzbuzz", "16", "17", "fizz", "19", "buzz"]
        self.assertEqual(received_data, actual_data)

    def test_fb_03(self):
        received_data: list[str] = get_data("http://127.0.0.1:5000/fizzbuzz?int1=2&int2=3&limit=10&str1=hello&str2=world")
        actual_data: list[str] = ["1", "hello", "world", "hello", "5", "helloworld", "7", "hello", "world", "hello"]
        self.assertEqual(received_data, actual_data)

    def test_fb_04(self):
        received_data: list[str] = get_data("http://127.0.0.1:5000/fizzbuzz?int1=abc&int2=3&limit=10&str1=hello&str2=world")
        actual_data: list[str] = ["int1, int2 and limit must be integers"]
        self.assertEqual(received_data, actual_data)

    def test_fb_05(self):
        received_data: list[str] = get_data("http://127.0.0.1:5000/fizzbuzz?int1=3&int2=5&limit=100&str1=hello&str2=world")
        actual_data: list[str] = ['1', '2', 'hello', '4', 'world', 'hello', '7', '8', 'hello', 'world', '11', 'hello', '13', '14', 'helloworld', '16', '17', 'hello', '19', 'world', 'hello', '22', '23', 'hello', 'world', '26', 'hello', '28', '29', 'helloworld', '31', '32', 'hello', '34', 'world', 'hello', '37', '38', 'hello', 'world', '41', 'hello', '43', '44', 'helloworld', '46', '47', 'hello', '49', 'world', 'hello', '52', '53', 'hello', 'world', '56', 'hello', '58', '59', 'helloworld', '61', '62', 'hello', '64', 'world', 'hello', '67', '68', 'hello', 'world', '71', 'hello', '73', '74', 'helloworld', '76', '77', 'hello', '79', 'world', 'hello', '82', '83', 'hello', 'world', '86', 'hello', '88', '89', 'helloworld', '91', '92', 'hello', '94', 'world', 'hello', '97', '98', 'hello', 'world']
        self.assertEqual(received_data, actual_data)

    def test_fb_06(self):
        received_data: list[str] = get_data("http://127.0.0.1:5000/fizzbuzz?int1=2&int2=3&limit=10&str1=hello&str2=world")
        actual_data: list[str] = ["1", "hello", "world", "hello", "5", "helloworld", "7", "hello", "world", "hello"]
        self.assertEqual(received_data, actual_data)

    def test_fb_07(self):
        received_data: list[str] = get_data("http://127.0.0.1:5000/fizzbuzz?int1=2&int2=3&limit=10&str1=hello&str2=world")
        actual_data: list[str] = ["1", "hello", "world", "hello", "5", "helloworld", "7", "hello", "world", "hello"]
        self.assertEqual(received_data, actual_data)

    def test_fb_08(self):
        received_data: list[str] = get_data("http://127.0.0.1:5000/fizzbuzz?int1=3&int2=5&limit=10&str1=fizz&str2=buzz")
        actual_data = ["1", "2", "fizz", "4", "buzz", "fizz", "7", "8", "fizz", "buzz"]
        self.assertEqual(received_data, actual_data)
    
    def test_stats(self):
        received_data = get_data("http://127.0.0.1:5000/stats")
        actual_data = {"frequent_req_hits":2,"max_hits_params":{"int1":2,"int2":3,"limit":10,"str1":"hello","str2":"world"}}
        self.assertEqual(received_data, actual_data)
    
if __name__ == "__main__":
    unittest.main()

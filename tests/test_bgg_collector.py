import unittest
import sys
import requests
from mock import patch
sys.path.append("../")

import bgg_collector
from bs4 import BeautifulSoup



class CollectorTest(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @patch("requests.Response.text")
    @patch("requests.get")
    def test_get_games(self, get_mock, text_mock):
        with open("test_html.html") as td:
            test_data = td.read()

        get_mock.return_value = requests.Response()
        #get_mock.return_value.text = test_data
        text_mock = test_data

        game_list = bgg_collector.extract_games_from_page(1,"all")
        self.assertEquals(len(game_list),100)

    def test_get_entry(self):
        self.assertTrue(False)

    def test_get_games_on_page(self):
        self.assertTrue(False)


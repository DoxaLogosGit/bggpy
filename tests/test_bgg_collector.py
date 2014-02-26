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

    @patch("bgg_collector.get_page_text")
    def test_get_games(self, get_mock):
        with open("test_html.html") as td:
            test_data = td.read()

        get_mock.return_value = test_data
        game_list = bgg_collector.extract_games_from_page(1, "all")
        self.assertEquals(len(game_list), 100)

    def test_get_entry(self):

        expected_entry = {"gameid":"12333",
                          "title":"Twilight Struggle",
                          "year":"2005"}
        soup_parse = BeautifulSoup("<div id='status_objectname1'></div><div id='results_objectname1' style='z-index:1000;' onclick=''><a  href=\"/boardgame/12333/twilight-struggle\"   >Twilight Struggle</a><span class='smallerfont dull'>(2005)</span></div>")
        rough_cut = soup_parse.find_all('div', attrs={"style":"z-index:1000;"})

        for tag in rough_cut:
            test_entry = bgg_collector.extract_game_from_entry(tag)

        self.assertEquals(expected_entry, test_entry)

    @patch("bgg_collector.get_page_text")
    def test_get_games_on_page(self, get_mock):
        with open("test_html.html") as td:
            test_data = td.read()

        get_mock.return_value = test_data

        games = bgg_collector.get_list_of_top_games(100)
        self.assertEquals(len(games), 100)


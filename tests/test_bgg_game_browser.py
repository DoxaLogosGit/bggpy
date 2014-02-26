import unittest
import sys
import requests
from bs4 import BeautifulSoup
from mock import patch
sys.path.append("../")

import bgg_game_browser


class CollectorTest(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @patch("bgg_game_browser.get_page_text")
    def test_get_games_on_page(self, get_mock):
        with open("tests/test_html.html") as td:
            test_data = td.read()

        get_mock.return_value = test_data
        game_list = bgg_game_browser.extract_games_from_page(1, "all")
        self.assertEquals(len(game_list), 100)

    def test_get_entry(self):

        expected_entry = {"gameid":"12333",
                          "title":"Twilight Struggle",
                          "year":"2005"}
        soup_parse = BeautifulSoup("<div id='status_objectname1'></div><div id='results_objectname1' style='z-index:1000;' onclick=''><a  href=\"/boardgame/12333/twilight-struggle\"   >Twilight Struggle</a><span class='smallerfont dull'>(2005)</span></div>")
        rough_cut = soup_parse.find_all('div', attrs={"style":"z-index:1000;"})

        for tag in rough_cut:
            test_entry = bgg_game_browser.extract_game_from_entry(tag)

        self.assertEquals(expected_entry, test_entry)

    def test_get_entry_with_na_year1(self):

        expected_entry = {"gameid":"12333",
                          "title":"Twilight Struggle",
                          "year":"N/A"}
        soup_parse = BeautifulSoup("<div id='status_objectname1'></div><div id='results_objectname1' style='z-index:1000;' onclick=''><a  href=\"/boardgame/12333/twilight-struggle\"   >Twilight Struggle</a><span> </span></div>")
        rough_cut = soup_parse.find_all('div', attrs={"style":"z-index:1000;"})

        for tag in rough_cut:
            test_entry = bgg_game_browser.extract_game_from_entry(tag)

        self.assertEquals(expected_entry, test_entry)

    def test_get_entry_with_na_year2(self):

        expected_entry = {"gameid":"12333",
                          "title":"Twilight Struggle",
                          "year":"N/A"}
        soup_parse = BeautifulSoup("<div id='status_objectname1'></div><div id='results_objectname1' style='z-index:1000;' onclick=''><a  href=\"/boardgame/12333/twilight-struggle\"   >Twilight Struggle</a> blahblah</div>")
        rough_cut = soup_parse.find_all('div', attrs={"style":"z-index:1000;"})

        for tag in rough_cut:
            test_entry = bgg_game_browser.extract_game_from_entry(tag)

        self.assertEquals(expected_entry, test_entry)


    @patch("bgg_game_browser.get_page_text")
    def test_get_games(self, get_mock):
        with open("tests/test_html.html") as td:
            test_data = td.read()

        get_mock.return_value = test_data

        games = bgg_game_browser.get_list_of_top_games(100)
        self.assertEquals(len(games), 100)

    @patch("bgg_game_browser.get_page_text")
    def test_get_games_300(self, get_mock):
        with open("tests/test_html.html") as td:
            test_data = td.read()

        get_mock.return_value = test_data

        games = bgg_game_browser.get_list_of_top_games(300)
        self.assertEquals(len(games), 300)

    @patch("bgg_game_browser.get_page_text")
    def test_get_games_355(self, get_mock):
        with open("tests/test_html.html") as td:
            test_data = td.read()

        get_mock.return_value = test_data

        games = bgg_game_browser.get_list_of_top_games(355)
        self.assertEquals(len(games), 355)

    @patch("bgg_game_browser.get_page_text")
    def test_get_games_45(self, get_mock):
        with open("tests/test_html.html") as td:
            test_data = td.read()

        get_mock.return_value = test_data

        games = bgg_game_browser.get_list_of_top_games(45)
        self.assertEquals(len(games), 45)

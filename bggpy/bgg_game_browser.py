import requests
from bs4 import BeautifulSoup
import re


##globals
CATEGORIES = { "all" : "",
              "abstracts": "abstracts/",
              "customizable": "cgs/",
              "childrens": "childrensgames/",
              "family": "familygames/",
              "party": "partygames/",
              "strategy": "strategygames/",
              "thematic": "thematic/",
              "war": "wargames/"}

BASE_URL = "http://boardgamegeek.com/{0}browse/boardgame/page/{1}"

NUM_PATTERN = re.compile("\d+")

def get_page_text(page_num, category):
    """
        For now this function is here for ease of unit testing
    """
    page = requests.get(BASE_URL.format(CATEGORIES[category], str(page_num + 1)))
    return page.text

def extract_game_from_entry(tag):
    """
    This function will extract the pertinent game information out of the
    beautiful soup "tag" of filtered data from the web page

    :param: tag - beautiful soup HTML entry that has the game data

    :return: a dict of game title, game id, year publish
    """
    #get contents of tag
    contents = tag.contents
    #strip "returns"
    contents = [x for x in contents if x != u'\n']
    entry_dict = {}
    # get id
    match = NUM_PATTERN.search(contents[0].attrs['href'])
    entry_dict["gameid"] = match.group(0)
    # get game title
    entry_dict["title"] = contents[0].text
    # get year
    try:
        match = NUM_PATTERN.search(contents[1].text)
    except:
        entry_dict["year"] = "N/A"
        return entry_dict

    try:
        entry_dict["year"] = match.group(0)
    except AttributeError:
        entry_dict["year"] = "N/A"

    return entry_dict


def extract_games_from_page(page_num, category, stop_at=100):
    """
    This function will retrieve the BGG game page and pull out all the games 
    on the page.  If stop_at is not 100, it will cut the list short, since the
    page always has 100 games on it.

    :param: page_num - the page number
    :param: category - what category of game is it
    :param: stop_at - the number to stop at before 100

    :return: a list of games with their gameid in rank order
    """
    page = get_page_text(page_num, category)

    soup_parse = BeautifulSoup(page)

    #find the games 
    rough_cut = soup_parse.find_all('div', attrs={"style":"z-index:1000;"})
    game_list = []
    for index, rough_entry in enumerate(rough_cut):
        game_list.append(extract_game_from_entry(rough_entry))
        if index + 1 == stop_at:
            break

    return game_list

def get_list_of_top_games(number_of_games, category="all"):
    """
    This function will retrieve the top number of games based on the current
    BGG rankings.

    :param: number_of_games = how many games to retrieve

    :return: a list of games with their gameid in rank order
    """

    #determine the number of pages to retrieve
    number_of_pages = number_of_games / 100
    extra_games = number_of_games % 100


    games = []
    for page in xrange(number_of_pages):
        games.extend(extract_games_from_page(page, category))

    #grab extra
    if extra_games != 0 and number_of_pages != 0:
        games.extend(extract_games_from_page(number_of_pages + 1, category, stop_at=extra_games))
    elif extra_games != 0 and number_of_pages == 0:
        games.extend(extract_games_from_page(number_of_pages, category, stop_at=extra_games))

    return games



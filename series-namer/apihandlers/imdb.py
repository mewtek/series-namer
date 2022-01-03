""" General API handler for calls to the IMDB Api on https://imdb-api.com"""
import requests as r

# Global variables
apiKey = "k_nc0lr1hf"

def search_series(searchterm:str):
    """
    Returns a list of series from a search term.
    """
    if (searchterm == None or searchterm == "" or searchterm == " "):
        return
    
    url = f"https://imdb-api.com/api/SearchSeries/{apiKey}/{searchterm}"
    d = r.get(url=url).json()

def search_id(id:str):
    """
    Returns a series based off an IMDb ID.
    Use search_series() for searching via text.
    """
    pass


def search_season(id:str, season:int):
    """
    Returns all the episodes from a specific season
    of a series.
    """
    url = f"https://imdb-api.com/api/SearchSeason/{apiKey}/{id}/{season}"
    d = r.get(url=url).json()
    
# coding: utf-8

# First, you need to import the quasar module
# Make sure you declare Quasar as dependency in the addon.xml or it won't work
# You can read it at:
# https://github.com/scakemyer/plugin.video.quasar/blob/master/resources/site-packages/quasar/provider.py
from quasar import provider


# Raw search
# query is always a string
def search(query):
    # Will issue a GET call to http://foo.bar/search?q=query
    # (properly urlencoded)
    resp = provider.GET("http://foo.bar/search", params={
        "q": query,
    })
    return provider.extract_magnets(resp.data)
# To parse JSON you can do:
#     items = resp.json()
# To parse XML you can do:
#     dom = resp.xml()
# If you have RSS, you can let Quasar parse it for you with:
#     return provider.parse_rss(resp.xml())


# Movie Payload Sample
# Note that "titles" keys are countries, not languages
# The titles are also normalized (accents removed, lower case etc...)
# {
#     "imdb_id": "tt1254207",
#     "title": "big buck bunny",
#     "year": 2008,
#     "titles": {
#         "es": "el gran conejo",
#         "nl": "peach open movie project",
#         "ru": "большои кролик",
#         "us": "big buck bunny short 2008"
#     }
# }
def search_movie(movie):
        return search("%(title)s %(year)d" % movie)


# Episode Payload Sample
# {
#     "imdb_id": "tt0092400",
#     "tvdb_id": "76385",
#     "title": "married with children",
#     "season": 1,
#     "episode": 1,
#     "titles": null
# }
def search_episode(episode):
    return search("%(title)s S%(season)02dE%(episode)02d" % episode)


# Episode Payload Sample
# {
#     "imdb_id": "tt0092400",
#     "tvdb_id": "76385",
#     "title": "married with children",
#     "season": 1,
#     "titles": null
# }
def search_season(season):
    return search("%(title)s Season %(season)d" % season)


# This registers your module for use
provider.register(search, search_movie, search_episode, search_season)

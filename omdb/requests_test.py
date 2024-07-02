import os
import requests

DJANGO_OMDB_KEY = "125edb1d"
# params = {"apikey": os.environ["DJANGO_OMDB_KEY"], "t": "star wars"}
params = {"apikey": DJANGO_OMDB_KEY, "t": "star wars"}

resp = requests.get("https://omdbapi.com/", params=params)

print(resp.json())
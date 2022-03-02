import requests


def connection():
    con = requests.get('http://0.0.0.0:1234/anuncios_copy/default/create')
    return con

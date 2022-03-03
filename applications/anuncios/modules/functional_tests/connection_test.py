import requests


def connection_anuncios_copy():
    con = requests.get('http://0.0.0.0:1234/anuncios_copy/default/index')
    return con

def connection_anuncios():
    con = requests.get('http://0.0.0.0:1234/anuncios/default/indes')
    return con
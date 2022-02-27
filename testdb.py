import requests


page = requests.get('http://0.0.0.0:8000/anuncios/default/index')
print(page[0])
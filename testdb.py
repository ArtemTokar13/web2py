import requests


page = requests.get('http://0.0.0.0:1234/anuncios_copy/default/create')
print(page.text)
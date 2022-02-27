import request


page = request.get('http://0.0.0.0:8000/anuncios/default/index')
print(page.text)
import requests


def testDB():
    page = requests.get('http://0.0.0.0:1234/anuncios_copy/default/create')
    print(page.text)
    
if __name__ == '__main__':
    testDB()
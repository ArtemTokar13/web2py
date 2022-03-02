import requests


def testDB():
    page = requests.get('http://0.0.0.0:1234/anuncios_copy/default/create')
    if page:
        return 'Success'
    else:
        return 'No connection'
    
if __name__ == '__main__':
    print(testDB())
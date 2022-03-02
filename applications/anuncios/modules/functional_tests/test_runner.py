# -*- coding: utf-8 -*-

'''
Created on 23 sept. 2020

@author: nico

Ejecución:
    
    python web2py.py --no-banner -S anuncios -R applications/anuncios/private/run_functional_tests.py
'''

import unittest
import os
import requests


def testDB():
    page = requests.get('http://0.0.0.0:1234/anuncios_copy/default/create')
    if page:
        print('Success')
    else:
        print('No connection')
    


    
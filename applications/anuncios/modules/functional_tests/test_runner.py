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
from connection_test import connection_anuncios_copy, connection_anuncios


class TestConnect(unittest.TestCase):

    def setUp(self):
        self.res1 = connection_anuncios_copy()
        self.res2 = connection_anuncios()

    def test_response_correct_status_code_1(self):
        self.assertEqual(200, self.res1.status_code)
        
    def test_response_correct_status_code_2(self):
        self.assertEqual(200, self.res2.status_code)
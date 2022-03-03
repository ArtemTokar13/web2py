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
from connection_test import connection_anuncios_copy


class TestConnect(unittest.TestCase):

    def setUp(self):
        self.res = connection_anuncios_copy()

    def test_response_correct_status_code(self):
        self.assertEqual(200, self.res.status_code)
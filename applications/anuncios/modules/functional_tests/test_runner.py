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
from .connection_test import connection


class TestConnect(unittest.TestCase):

    def setUp(self):
        self.res = connection()

    def test_response_correct_status_code(self):
        self.assertEqual(200, self.res.status_code)
#
# def connection_test():
#     page = connection()
#     if page:
#         print(page.status_code)
#         print('Success')
#     else:
#         print('No connection')
#
# # def db_test(unittest.TestCase):
# #     from 

    
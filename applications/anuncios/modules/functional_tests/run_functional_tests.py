# -*- coding: utf-8 -*-

'''
Created on 23 sept. 2020

@author: nico

Ejecución:
    
    python web2py.py --no-banner -S anuncios -R applications/anuncios/modules/functional_tests/run_functional_tests.py

'''

import unittest

from test_runner import TestConnect
# from dev_imports_para_eclipse import *
# from applications.anuncios.models.db_anuncios import db


if __name__ == '__main__':
    unittest.main()
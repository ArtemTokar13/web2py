# -*- coding: utf-8 -*-

'''
Created on 23 sept. 2020

@author: nico

Ejecución:
    
    python web2py.py --no-banner -S h3o -R applications/h3o/private/run_functional_tests.py

'''


from applications.anuncios.modules.functional_tests import test_runner


if __name__ == '__main__':
    test_runner.run_tests(recreate_database=False)
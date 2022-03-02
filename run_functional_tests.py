# -*- coding: utf-8 -*-

'''
Created on 23 sept. 2020

@author: nico

Ejecución:
    
    python web2py.py --no-banner -S h3o -R applications/anuncios/private/run_functional_tests.py

'''


from applications.anuncios.modules.functional_tests.test_runner import TestConnect


if __name__ == '__main__':
    unittest.main()
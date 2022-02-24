# encoding: utf-8
'''
Created on 2016-12-01

@author: nico

Funciones para chequear valores y tipos. 
'''

if False:
    from dev_imports_para_eclipse import *

from decimal import Decimal
import re

EMPTY_BIN_SEQ = b'' 

def str_is_empty(s):
    """ Indica si un campo de texto obtenido de base de datos
    o una cadena obtenida de un control HTML (valor de un SELECT en un POST por ejemplo)
    esta vacia (valor None o cadena vacia). """
    return s is None or s == EMPTY_BIN_SEQ or len(s.strip()) == 0 

def is_empty(v):
    """ Indica si un valor arbitrario obtenido de base de datos
    o de un control HTML (valor de un SELECT en un POST por ejemplo)
    esta vacia: valor None, cadena vacia o cadena que solo tiene espacios en blanco. """
    return v is None or v == EMPTY_BIN_SEQ or len(str(v).strip()) == 0


def is_file_extension(filename, ext_list):
    """ Devuelve True si la extensión del nombre del fichero
    es una de las indicadas. """
    f_ext = filename.lower().split('.')[-1]
    return f_ext in ext_list

def is_equal_fuzzy(v1, v2, fuzzy_dif=Decimal('0.02')):
    """ Indica si dos valores numéricos son iguales.
    
    fuzzy_dif - diferencia máxima que puede haber entre los valores sin que sean considerados diferentes
    """
    is_equal = v1 == v2
    if not is_equal and fuzzy_dif != 0:
        try:
            dif = abs(abs(v1) - abs(v2))
            is_equal = dif <=abs(fuzzy_dif)
        except:
            pass
    return is_equal

def is_valid_vat_nr(vat_nr, country_id):
    """ Comprueba si el formato de un DNI/NIf es válido. """
    from constants import COUNTRY_SPAIN_ID
    is_valid = False
    if country_id == COUNTRY_SPAIN_ID:
        try:
            clean_vat_nr = vat_nr.replace(' -_','').strip()
            # documentación formatos NIF: 
            #    http://www.juntadeandalucia.es/servicios/madeja/contenido/recurso/677
            #    https://marosavat.com/es/formatos-de-nif-en-europa/
            NIF_1_REGEX = "^(ES)?[a-zA-Z]\d{8}$"          # prefijo ES opcional + letra (A, B, C, D, E, F, G, H, J, K, L, M) + 8 dígitos (el último dígito es de control)
            NIF_2_REGEX = "^(ES)?[a-zA-Z]\d{7}[a-zA-Z]$"  # prefijo ES opcional + letra (P, Q, R, S, U, V, N, W) + 7 dígitos + letra control
            DNI_REGEX = "^[0-9]{8}[TRWAGMYFPDXBNJZSQVHLCKE]$"   # DNI normal
            """ Los NIE, según la Orden de 7 de febrero de 1997, inicialmente constaban de X + 8 números + dígito de control, 
            la Orden INT/2058/2008 redujo de 8 a 7 los números para que tuvieran la misma longitud que los NIF y CIF, 
            pero esta Orden mantiene la validez de los NIE X de 8 dígitos anteriores ya asignados. """ 
            NIE_1_REGEX = "^[xX]\d{8}[0-9a-zA-Z]$"
            NIE_2_REGEX = "^[xXyYzZ]\d{7}[0-9a-zA-Z]$"
            full_regex = '|'.join('({})'.format(s) for s in [NIF_1_REGEX, 
                                                             NIF_2_REGEX,
                                                             DNI_REGEX, 
                                                             NIE_1_REGEX,
                                                             NIE_2_REGEX])
            regex_obj = re.compile(full_regex)
            is_valid = regex_obj.match(clean_vat_nr) is not None
        except:
            pass
    else:
        is_valid = vat_nr is not None and len(vat_nr) > 6
    return is_valid

def is_date_between(test_date, min_date=None, max_date=None):
    """ Devuelve True si la test_date está entre min_date y max_date 
    o es igual a alguna de ellas. """
    is_higher_than_min = min_date is None or test_date >= min_date
    is_lower_than_max = max_date is None or test_date <= max_date
    return is_higher_than_min and is_lower_than_max 
    
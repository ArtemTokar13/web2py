# -*- coding: utf-8 -*-
'''
Created on 20/11/2013

@author: nico
'''

# fichero a importar en los controladores:
# if False: import * from dev_imports_para_eclipse
# para que el resaltado de sintaxis funciones en Eclipse

if False:
    from gluon.globals import *
    from gluon.html import *
    from gluon.http import *
    from gluon.tools import *
    from gluon.sql import *
    from gluon.validators import *
    from gluon.languages import translator as T
    from gluon.sqlhtml import SQLFORM, SQLTABLE, form_factory
    from gluon.dal import DAL
    from gluon.dal.objects import Table, Field
    from gluon.compileapp import LOAD
    from gluon import pydal
    session = Session()
    request = Request()
    response = Response()
    crud = Crud()
    db = DAL('sqlite://storage.sqlite')
    #from models.db import db, auth
    auth = Auth(globals(),None)
    from gluon.cache import Cache
    cache = Cache(request)
    IS_POST = request.env.request_method == 'POST'

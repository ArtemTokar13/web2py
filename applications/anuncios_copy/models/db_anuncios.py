db = DAL('sqlite://storage.sqlite')

from gluon.tools import *
auth = Auth(db)
auth.define_tables()
crud = Crud(db)

db.define_table('anuncio',
               Field('title'),
               Field('body', 'text'),
               Field('price', 'decimal(5, 2)'),
               Field('negociacion', 'boolean', default=False),
               Field('created_on', 'datetime', default=request.now),
               Field('created_by', db.auth_user, default=auth.user_id),
               Field('contacto', 'string', default=None, required=False),
               format='%(title)s')

db.anuncio.title.requires = IS_NOT_IN_DB(db, 'anuncio.title')
db.anuncio.body.requires = IS_NOT_EMPTY()
db.anuncio.created_by.readable = db.anuncio.created_by.writable = False
db.anuncio.created_on.readable = db.anuncio.created_on.writable = False

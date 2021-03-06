from gluon.tools import Crud
from gluon.tools import Auth

auth = Auth(db)

auth.define_tables()

db = DAL("sqlite://storage.sqlite")

db.define_table('image',
               Field('title', unique=True),
               Field('file', 'upload'),
               format = '%(title)s'
               )

db.define_table('comment',
               Field('image_id', db.image),
               Field('author'),
               Field('email'),
               Field('body', 'text')
               )

db.image.title.requires = IS_NOT_IN_DB(db, db.image.title)
db.comment.image_id.requires = IS_IN_DB(db, db.image.id, '%(title)s')
db.comment.author.requires = IS_NOT_EMPTY()
db.comment.email.requires = IS_EMAIL()
db.comment.body.requires = IS_NOT_EMPTY()

db.comment.image_id.writable = db.comment.image_id.readable = False

crud = Crud(db)

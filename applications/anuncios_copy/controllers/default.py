def index():
    message = 'Bienvenido al Anuncios!'
    anuncios = db().select(db.anuncio.id, db.anuncio.title, db.anuncio.created_by, orderby=db.anuncio.title)
    return dict(message=message, anuncios=anuncios)

@auth.requires_login()
def create():
    form = crud.create(db.anuncio, next=URL('index'))
    return dict(form=form)

def show():
    this_anuncio = db.anuncio(request.args(0)) or redirect(URL('index'))
    return dict(anuncio=this_anuncio)

@auth.requires_login()
def edit():
    this_anuncio = db.anuncio(request.args(0)) or redirect(URL('index'))
    if this_anuncio.created_by == auth.user.id:
        message = 'YES!'
        form = crud.update(db.anuncio, this_anuncio, next=URL('show', args=request.args))
        return dict(form=form, message=message)
    message = 'Usted no tiene permiso de cambiar este anuncio'
    return dict(message=message)

def search():
     return dict(form=FORM(INPUT(_id='keyword',_name='keyword',
              _onkeyup="ajax('callback', ['keyword'], 'target');")),
              target_div=DIV(_id='target'))

def callback():
     "an ajax callback that returns a <ul> of links to wiki pages"
     query = db.anuncio.title.contains(request.vars.keyword)
     anuncios = db(query).select(orderby=db.anuncio.title)
     links = [A(a.title, _href=URL('show',args=a.id)) for a in anuncios]
     return UL(*links)

# ---- API (example) -----
@auth.requires_login()
def api_get_user_email():
    if not request.env.request_method == 'GET': raise HTTP(403)
    return response.json({'status':'success', 'email':auth.user.email})

# ---- Smart Grid (example) -----
@auth.requires_membership('admin') # can only be accessed by members of admin groupd
def grid():
    response.view = 'generic.html' # use a generic view
    tablename = request.args(0)
    if not tablename in db.tables: raise HTTP(403)
    grid = SQLFORM.smartgrid(db[tablename], args=[tablename], deletable=False, editable=False)
    return dict(grid=grid)

# ---- Embedded wiki (example) ----
def wiki():
    auth.wikimenu() # add the wiki to the menu
    return auth.wiki() 

# ---- Action for login/register/etc (required for auth) -----
def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/bulk_register
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    also notice there is http://..../[app]/appadmin/manage/auth to allow administrator to manage users
    """
    return dict(form=auth())

# ---- action to server uploaded static content (required) ---
@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)

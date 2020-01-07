from bottle import default_app, route

@route('/')
def webapp_root():
    return ('<html><body><h1>Bottle is a fast, simple and lightweight WSGI micro web-framework for Python.</h1></body></html>')

application = default_app()
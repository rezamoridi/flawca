from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = 'adavavd adwd awhsjt'

    from .views import views
    from .auth import auth
    from .library import library

    app.register_blueprint(library, url_prefix='/')
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')


    return app
from logging import INFO, Formatter
from logging.handlers import RotatingFileHandler
import os
from datetime import datetime

from flask import Flask, current_app, request, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import flask_sijax

# initialize extensiions
db = SQLAlchemy()
migrate = Migrate()

def date_format(value, format):
    return value.strftime(format)

def create_app():
    app = Flask(
        __name__,
        template_folder='./templates',
        static_folder='./static'
    )

    # config
    app_settings = os.getenv('APP_SETTINGS', 'app.config.DevelopmentConfig')
    app.config.from_object(app_settings)

    # set up extensions
    db.init_app(app)
    migrate.init_app(app, db)

    # register Blueprint
    from app.views import index
    app.register_blueprint(index.app, url_prefix='')

    # Jinja2
    app.jinja_env.filters['strftime'] = date_format

    # Sijax
    flask_sijax.Sijax(app)

    # log
    # @app.before_first_request
    # def make_logger():
    #     handler = RotatingFileHandler('server_log.log', maxBytes=100000, backupCount=5)
    #     handler.setFormatter(Formatter("[%(asctime)s] %(levelname)s - %(message)s"))
    #
    #     current_app.logger.addHandler(handler)
    #     current_app.logger.setLevel(INFO)
    #
    #     current_app.logger.info('------- Logger Initialized -------')
    #
    # @app.before_request
    # def before_request():
    #     current_app.logger.info('Request from {0} [ {1} {2} ]'.format(request.host, request.method, request.url))
    #     current_app.logger.info('Request values : '.format(request.values))
    #
    # @app.after_request
    # def after_request(response):
    #     current_app.logger.info('Respond : {0}'.format(response.status))
    #
    #     response.headers['X-Powered-By'] = app.config['SERVICE_NAME']
    #
    #     return response
    #
    # @app.teardown_appcontext
    # def teardown_appcontext(exception):
    #     if not exception:
    #         current_app.logger.info('Teardown appcontext successfully.')

    # error handler
    @app.errorhandler(403)
    def handle_403(e):
        return render_template('403.html')

    @app.errorhandler(404)
    def handle_404(e):
        return render_template('404.html')

    @app.errorhandler(500)
    def handle_500(e):
        return render_template('500.html')


    return app

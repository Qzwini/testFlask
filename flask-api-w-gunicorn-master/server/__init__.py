import functools
from flask import Flask, render_template, jsonify, request
# from dotenv import load_dotenv
from flask_jwt_extended import jwt_required, JWTManager, create_access_token, get_jwt_identity, decode_token
from flask_cors import CORS, cross_origin
import datetime
import flask_bcrypt
import os
from .models import db, User
import eventlet
eventlet.monkey_patch()


def create_app(debug=False):
    """Create an application."""
    # initialize Flask
    app = Flask(__name__, static_folder='static',
                template_folder='templates')
    app.debug = debug
    jwt = JWTManager(app)
    # load_dotenv(verbose=True)
    app.config['JWT_SECRET_KEY'] = os.environ.get('SECRET')
    app.config['JWT_ACCESS_TOKEN_EXPIRES'] = datetime.timedelta(days=1)
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
    app.config['CORS_HEADERS'] = 'Content-Type'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://postgres:1234@localhost/fjwt'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    # ROOMS = ["finance", "warehouse", "accounts",
    #          "global"]  # dict to track active rooms

    from .routes.user import user_blueprint
    from .routes.main import main
    app.register_blueprint(user_blueprint)
    app.register_blueprint(main)

    # socketio.init_app(app, async_mode='eventlet',
    #                   message_queue='redis://', cors_allowed_origins="*")
    db.init_app(app)

    with app.app_context():
        db.create_all()

    return app

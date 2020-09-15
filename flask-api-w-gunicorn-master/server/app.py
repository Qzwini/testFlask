# import functools
# from flask import Flask, render_template, jsonify, request
# from flask_socketio import join_room, emit, send, disconnect
# from sockets import SocketIO
# # from dotenv import load_dotenv
# from flask_jwt_extended import jwt_required, JWTManager, create_access_token, get_jwt_identity, decode_token
# from flask_cors import CORS, cross_origin
# import datetime
# import flask_bcrypt
# import os
# from middleware import authenticated_only
# from models import db, User
# from routes.user import user_blueprint


# # initialize Flask
# app = Flask(__name__)
# jwt = JWTManager(app)
# # load_dotenv(verbose=True)
# app.config['JWT_SECRET_KEY'] = os.environ.get('SECRET')
# app.config['JWT_ACCESS_TOKEN_EXPIRES'] = datetime.timedelta(days=1)
# app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
# app.config['CORS_HEADERS'] = 'Content-Type'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://postgres:1234@localhost/fjwt'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# socketio = SocketIO(app)
# ROOMS = ["finance", "warehouse", "accounts",
#          "global"]  # dict to track active rooms
# db.init_app(app)
# socketio.init_app(app)
# with app.app_context():
#     db.create_all()


# app.register_blueprint(user_blueprint)


# @app.route('/')
# def index():
#     """Serve the index HTML"""
#     return render_template('index.html')


# @socketio.on('create')
# @authenticated_only
# def on_create(data):
#     # """Create a game lobby"""
#     # gm = game.Info(
#     #     size=data['size'],
#     #     teams=data['teams'],
#     #     dictionary=data['dictionary'])
#     # room = gm.game_id
#     # ROOMS[room] = gm
#     print(data, request.args.get('token'))
#     room = ROOMS[3]
#     join_room(room)
#     emit('join_room', {'room': room})


# @socketio.on('my event')
# @authenticated_only
# def handle_my_custom_event(data):
#     emit('my response', {'message': '{0} has joined'},
#          broadcast=True)


# if __name__ == '__main__':
#     socketio.run(app, debug=True)

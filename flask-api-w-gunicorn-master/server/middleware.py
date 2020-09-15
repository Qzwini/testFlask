import functools
from flask import Flask, jsonify, request
from flask_socketio import disconnect
from flask_jwt_extended import decode_token


def authenticated_only(f):
    @functools.wraps(f)
    def wrapped(*args, **kwargs):
        if not request.args.get('token'):
            disconnect()
        else:
            try:
                # decode_token(request.args.get('token'))
                print(request.args.get('token'))
                return f(*args, **kwargs)
            except:
                disconnect()
    return wrapped

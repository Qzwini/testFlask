from flask import Flask, render_template, jsonify, request, Blueprint
from ..middleware import authenticated_only
# from .. import socketio
from ..models import User


main = Blueprint('main_blueprint', __name__)


@main.route('/')
def index():
    """Serve the index HTML"""
    data = User.query.all()
    result = [d.__dict__ for d in data]
    for i in range(len(result)):
        del result[i]['_sa_instance_state']
    # print(result)
    # return render_template('index.html')
    return jsonify(result)


@main.route('/test')
def test():
    return jsonify("test")

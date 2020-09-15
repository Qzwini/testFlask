# facebook/views/profile.py

from flask import Blueprint, render_template, request, jsonify
from ..middleware import authenticated_only
from ..models import db, User
# from flask_socketio import emit, join_room, send
# from .main import ROOMS
# from .. import socketio


user_blueprint = Blueprint('user_blueprint', __name__)


@user_blueprint.route('/')
def index():
    """Serve the index HTML"""
    data = User.query.all()
    result = [d.__dict__ for d in data]
    for i in range(len(result)):
        del result[i]['_sa_instance_state']
    # print(result)
    # return render_template('index.html')
    return jsonify(result)


@user_blueprint.route('/<user_url_slug>')
def timeline(user_url_slug):
    # Do some stuff
    return render_template('profile/timeline.html')


@user_blueprint.route('/new', methods=['GET', 'POST'])
def new():
    if request.method == 'POST':
        if not request.form['name'] or not request.form['city'] or not request.form['addr']:
            return jsonify('Please enter all the fields', 'error')
        else:
            try:
                new_user = User(request.form['name'], request.form['city'],
                                request.form['addr'], request.form['pin'])

                db.session.add(new_user)
                db.session.commit()
                # emit('message', {'data': 'changed'})
                return jsonify('done!')
            except Exception as e:
                print(e)
                return jsonify('err')
    return render_template('form.html')

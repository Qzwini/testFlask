# start app with
pip install virtualenv
source env/bin/activate
pip install -r requirements.txt
gunicorn --worker-class eventlet -w 5 start:app
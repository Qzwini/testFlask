#!/bin/env python
# from server import create_app, socketio
from server import create_app

app = create_app(debug=True)

if __name__ == '__main__':
    # socketio.run(app)
    app.run()

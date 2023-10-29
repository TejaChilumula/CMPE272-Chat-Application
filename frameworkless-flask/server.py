from flask import Flask, render_template
from flask_socketio import SocketIO, emit, send

appFlask = Flask(__name__)
socketio = SocketIO(appFlask, cors_allowed_origins="*")

@appFlask.route('/')
def index():
    return render_template('index.html')

@socketio.on('connect')
def test_connect():
    socketio.emit('after connect', {'data':'Let us learn Web Socket in Flask'})


@socketio.on('chat')
def handle_message(data):
    print(data)
    socketio.emit('chat', data['data'])

if __name__ == '__main__':
    socketio.run(appFlask, allow_unsafe_werkzeug=True, host='0.0.0.0')
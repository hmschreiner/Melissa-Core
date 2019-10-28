# from flask import Flask, render_template
# from flask_socketio import SocketIO

# t-800 modules
from t800.profile_loader import load_profile
from t800.tts import tts
from t800.brain import query
from t800.microphone import get_speak_as_text

# app = Flask(__name__)
# socketio = SocketIO(app)

# @app.route("/")
# def hello():
#     return render_template('index.html')


# @socketio.on('user speaks')
# def handle_json(json):
#     speech_text = json['data']
#     print('T-800 thinks you said: ' + speech_text)

#     if speech_text is None:
#         pass
#     else:
#         query(speech_text)

def main():
    message = get_speak_as_text()
#     # tts('what day is it')
    print(message.encode('utf-8'))
    query(message)
    # socketio.run(app)


if __name__ == '__main__':
    main()

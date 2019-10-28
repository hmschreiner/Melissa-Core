import speech_recognition as sr


def get_speak_as_text():
    print('\n\n\nListening... \n\n\n')
    rec = sr.Recognizer()

    with sr.Microphone() as speaks:
        phrase = rec.listen(speaks)

    print('\n\n\n I heard ya! \n\n\n')

    try:
        return rec.recognize_google(phrase, language='en')
    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print("Could not process audio {0}".format(e))

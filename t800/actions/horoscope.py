from horoscope_generator import HoroscopeGenerator

# T-800
from t800.tts import tts

WORDS = {
    'tell_horoscope': {
        'groups': [
            ['tell', 'future'],
            ['say', 'wise'],
            ['how', 'day'],
            ['hows', 'day'],
            ['how', 'today'],
            ['hows', 'today'],
            'horoscope'
        ]
    }
}


def tell_horoscope(text):
    tts(HoroscopeGenerator.format_sentence(HoroscopeGenerator.get_sentence()))

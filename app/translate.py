import requests
from flask_babel import _
from app import app

def translate(text, source_language, dest_language):
    if 'MS_TRANSLATOR_KEY' not in app.config or \
            not app.config['MS_TRANSLATOR_KEY']:
        raise RuntimeError('MS_TRANSLATOR_KEY is not set')
    auth = {
        'Ocp-Apim-Subscription-Key': app.config['MS_TRANSLATOR_KEY'],
        'Ocp-Apim-Subscription-Region': app.config['MS_TRANSLATOR_REGION']
    }
    r = requests.post(
        'https://api.cognitive.microsofttranslator.com/translate?api-version=3.0&from={}&to={}'.format(
            source_language, dest_language),
        headers=auth,
        json=[{'Text': text}]
    )
    if r.status_code != 200:
        raise RuntimeError('Translation failed: {}'.format(r.text))
    return r.json()[0]['translations'][0]['text']
import requests
import json

URL_AUTH = 'https://developers.lingvolive.com/api/v1.1/authenticate'
URL_TRANSLATE = 'https://developers.lingvolive.com/api/v1/Minicard'
KEY = 'Ключ для доступа к API'

def get_a_word_translation(key: str) -> str:
    headers_auth = {'Authorization': 'Basic ' + KEY}
    auth = requests.post(URL_AUTH, headers=headers_auth)
    if auth.status_code == 200:
        token = auth.text
        headers_translate = {
            'Authorization': 'Bearer ' + token
        }
        params = {
            'text': key,
            'srcLang': 1033,
            'dstLang': 1049
        }
        req = requests.get(
            URL_TRANSLATE, headers=headers_translate, params=params)
        res = req.json()
        try:
            value = res['Translation']['Translation']
            return value
        except TypeError:
            if res == 'Incoming request rate exceeded for 50000 chars per day pricing tier':
                return res
            else:
                return None
    else:
        print('Error!' + str(auth.status_code))

if __name__ == "__main__":
    not_translated_words_test = ['victim', 'home', 'root']
    translated_words_test = {}
    for en in not_translated_words_test:
        ru = get_a_word_translation(en)
        if ru == 'Incoming request rate exceeded for 50000 chars per day pricing tier':
            break
        translated_words_test[en] = ru
        print('data/translated_words_test.json',
                          translated_words_test)
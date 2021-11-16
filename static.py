import json
import os


def token_saver(token):
    with open('Shikimori/user/token.json', 'w') as f:
        f.write(json.dumps(token))


def token_loader():
    if os.path.exists('Shikimori/user/token.json'):
        with open('Shikimori/user/token.json') as f:
            return json.load(f)
    return {}

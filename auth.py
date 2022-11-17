import oauthlib.oauth2.rfc6749.errors
from requests_oauthlib import OAuth2Session
from static import token_loader

URL = 'https://shikimori.one'
URL_TOKEN = 'https://shikimori.one/oauth/token'


class Auth:
    def __init__(self, token=None, token_saver=None, scope=None):
        self.client_id = '7EeEXaUt0p1XUUAiWt5G5ya1_SUsugzCnIIgfSDMjPg'
        self.client_secret = 'jq-Qwoqu-_f6lOXp7ZBh5cLnLaGZ4uEchRL-_8_sTxI'
        self.redirect_uri = 'urn:ietf:wg:oauth:2.0:oob'
        self.extra = {'client_id': self.client_id, 'client_secret': self.client_secret}
        self.token_saver = token_saver
        self.tokens = token_loader()
        self.headers = {'User-Agent': 'Anilight', 'Authorization': f'Bearer {self.tokens.get("access_token")}'}
        self.client = self.get_client(scope, self.redirect_uri, token)

    def get_client(self, scope, redirect_uri, token):
        client = OAuth2Session(self.client_id, auto_refresh_url=URL_TOKEN, auto_refresh_kwargs=self.extra,
                               scope=scope, redirect_uri=redirect_uri, token=token,
                               token_updater=self.token_saver)
        client.headers.update(self.headers)
        return client

    def get_auth_url(self):
        auth_url = URL + '/oauth/authorize'
        return self.client.authorization_url(auth_url)[0]

    def fetch_token(self, code):
        try:
            self.client.fetch_token(URL_TOKEN, code, client_secret=self.client_secret)
        except oauthlib.oauth2.rfc6749.errors.InvalidGrantError:
            return None
        self.token_saver(self.token)
        return self.token

    def refresh_token(self):
        if not token_loader():
            return None
        self.client.headers.clear()
        self.client.headers.update({'User-Agent': 'Anilight'})
        self.client.refresh_token(URL_TOKEN, refresh_token=token_loader().get('refresh_token'))
        self.token_saver(self.token)
        self.client.headers.update({'Authorization': f'Bearer {token_loader().get("access_token")}'})
        return self.token

    def get(self, url, params=None):
        return self.client.request('GET', url, params)

    @property
    def token(self):
        return self.client.token

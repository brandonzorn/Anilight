import os


class Shikimori:
    def __init__(self):
        self.animes = []
        self.animes_login = []
        self.anime_names_search = []
        self.anime_episodes_login = {}
        self.whoami = {}
        self.start()

    @staticmethod
    def start():
        wd = os.getcwd()
        if not os.path.isdir(f'{wd}/Shikimori'):
            os.mkdir(f'{wd}/Shikimori')
        if not os.path.isdir(f'{wd}/Shikimori/user'):
            os.mkdir(f'{wd}/Shikimori/user')
        if not os.path.isdir(f'{wd}/Shikimori/images'):
            os.mkdir(f'{wd}/Shikimori/images')

    def get_content(self, html):
        self.animes = []
        if html.status_code == 200:
            for i in html.json():
                self.animes.append(i)

    def get_content_login(self, html):
        self.animes_login = []
        if html.status_code == 200:
            for i in html.json():
                self.animes_login.append(i)

    def ret_anime(self):
        a = []
        for i in self.animes:
            if i.get('russian') == '':
                a.append(i.get('name'))
            else:
                a.append(i.get('russian'))
        return a

    def ret_anime_login(self):
        a = []
        for i in self.animes_login:
            if i.get('russian') == '':
                a.append(i.get('name'))
            else:
                a.append(i.get('russian'))
        return a

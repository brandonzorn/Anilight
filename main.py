import webbrowser
import requests
import sys
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from functools import partial
from threading import Thread
from pathlib import Path
from auth import Auth
from forms import shikimoriUI, shikimoriUIlogin, shikimoriUIlogdialog
from shikimori import Shikimori
from static import *

URL = 'https://shikimori.one'
URL_API = 'https://shikimori.one/api'
URL_TOKEN = 'https://shikimori.one/oauth/token'
HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0'}


class App:
    def __init__(self):
        self.session = Auth(token_saver=token_saver)
        self.Shikimori = Shikimori()
        self.cur_window = 'shikimori_main'
        self.token = None
        self.tokens = token_loader()
        self.pages = None
        self.link = None
        self.is_login = False
        self.current_page = 1
        self.current_page_login = 1
        self.current_list_login = None
        self.selected_anime = None
        self.anime_names_search = []
        self.anime_episodes_login = {}
        self.whoami = {}
        self.params = {'limit': 50, 'page': self.current_page, 'order': 'status'}
        self.params_login = {}

        self.Form = QWidget()
        self.Form_login = QWidget()
        self.Form_login_dialog = QWidget()
        self.window = QStackedWidget()
        self.ui = shikimoriUI.Ui_Dialog()
        self.ui_login = shikimoriUIlogin.Ui_Dialog()
        self.ui_login_dialog = shikimoriUIlogdialog.Ui_Dialog()
        self.ui.setupUi(self.Form)
        self.ui_login.setupUi(self.Form_login)
        self.ui_login_dialog.setupUi(self.Form_login_dialog)
        self.window.addWidget(self.Form)
        self.window.addWidget(self.Form_login)
        self.window.show()
        self.sorts = {self.ui.sort_id: 'id', self.ui.sort_type: 'kind', self.ui.sort_name: 'name',
                      self.ui.sort_date: 'aired_on', self.ui.sort_raiting: 'ranked', self.ui.sort_popular: 'popularity',
                      self.ui.sort_status: 'status', self.ui.sort_episodes: 'episodes'}
        self.types = {self.ui.type_tv: 'tv', self.ui.type_film: 'movie', self.ui.type_ova: 'ova',
                      self.ui.type_ona: 'ona', self.ui.type_special: 'special', self.ui.type_music: 'music',
                      self.ui.type_tv13: 'tv_13', self.ui.type_tv24: 'tv_24', self.ui.type_tv48: 'tv_48'}
        self.statuses = {self.ui.status_anons: 'anons', self.ui.status_ongoing: 'ongoing',
                         self.ui.status_release: 'released'}
        self.durations = {self.ui.episodes_10m: 'S', self.ui.episodes_29m: 'D', self.ui.episodes_30m: 'F'}
        self.ratings = {self.ui.raiting_g: 'g', self.ui.raiting_pg: 'pg', self.ui.raiting_pg13: 'pg_13',
                        self.ui.raiting_r17: 'r', self.ui.raiting_rp: 'r_plus', self.ui.raiting_rx: 'rx'}
        self.icon_path = os.path.join(Path(__file__).parent, 'images/icon.png')
        self.window.setWindowTitle('Shikimori Main')
        self.window.setWindowIcon(QIcon(self.icon_path))
        self.Form_login_dialog.setWindowIcon(QIcon(self.icon_path))
        self.ui.prev_page.clicked.connect(partial(self.change_page, '-'))
        self.ui.next_page.clicked.connect(partial(self.change_page, '+'))
        self.ui.filter_apply.clicked.connect(self.filter)
        self.ui.filter_reset.clicked.connect(self.filter_reset)
        self.ui.btn_search.clicked.connect(self.search)
        self.ui_login.btn_search.clicked.connect(self.search)
        self.ui.btn_login.clicked.connect(self.clicked_login)
        self.ui.list_anime.doubleClicked.connect(lambda: Thread(target=self.clicked).start())
        self.ui_login.btn_main.clicked.connect(self.clicked_main)
        self.ui_login.btn_account.clicked.connect(self.clicked_account)
        self.ui_login.btn_planned.clicked.connect(partial(self.change_list_login, 'p'))
        self.ui_login.btn_watching.clicked.connect(partial(self.change_list_login, 'w'))
        self.ui_login.btn_completed.clicked.connect(partial(self.change_list_login, 'c'))
        self.ui_login.btn_rewatching.clicked.connect(partial(self.change_list_login, 'r'))
        self.ui_login.btn_on_hold.clicked.connect(partial(self.change_list_login, 'o'))
        self.ui_login.btn_dropped.clicked.connect(partial(self.change_list_login, 'd'))
        self.ui_login.prev_page.clicked.connect(partial(self.change_page_login, '-'))
        self.ui_login.next_page.clicked.connect(partial(self.change_page_login, '+'))
        self.ui_login.animes.doubleClicked.connect(lambda: Thread(target=self.clicked).start())
        self.ui_login_dialog.btn_get.clicked.connect(self.login)
        self.ui_login_dialog.btn_login.clicked.connect(self.clicked_account_login)
        self.start()
        self.get_content()

    @staticmethod
    def get_html(url, params=None):
        return requests.get(url, headers=HEADERS, params=params)

    def start(self):
        self.session.headers.clear()
        self.session.headers.update({'User-Agent': 'Shikimori',
                                     'Authorization': f'Bearer {self.tokens.get("access_token")}'})
        self.whoami.update(self.session.get('https://shikimori.one/api/users/whoami').json())
        if self.whoami.get('state') == 'unauthorized':
            self.session.refresh_token()
            self.tokens = token_loader()
            self.whoami = self.session.get('https://shikimori.one/api/users/whoami').json()
            if self.whoami.get('state') == 'unauthorized':
                self.is_login = False
                return None
        self.is_login = True
        self.ui_login.username.setText(self.whoami.get('nickname'))

    def get_content(self):
        self.ui.list_anime.clear()
        self.params.update({'page': self.current_page})
        url = f'{URL_API}/animes'
        html = self.get_html(url, self.params)
        self.Shikimori.get_content(html)
        [self.ui.list_anime.addItem(i) for i in self.Shikimori.ret_anime()]

    def get_content_login(self):
        self.ui_login.animes.clear()
        if not self.current_list_login or not self.is_login:
            return None
        url = f'{URL_API}/animes'
        self.params_login.update({'page': self.current_page_login, 'limit': 50, 'order': 'name'})
        html = self.session.get(url, self.params_login)
        self.Shikimori.get_content_login(html)
        [self.ui_login.animes.addItem(i) for i in self.Shikimori.ret_anime_login()]

    def search(self):
        self.current_page = 1
        if self.cur_window == 'shikimori_main':
            self.params.update({'search': self.ui.line_search.text()})
            self.get_content()
        elif self.cur_window == 'shikimori_account':
            self.params_login.update({'search': self.ui_login.txt_search.text()})
            self.get_content_login()

    def clicked(self):
        if self.cur_window == 'shikimori_main':
            cur_list = self.Shikimori.animes
            cur_list_index = self.ui.list_anime.currentIndex()
        elif self.cur_window == 'shikimori_account':
            cur_list = self.Shikimori.animes_login
            cur_list_index = self.ui_login.animes.currentIndex()
        else:
            cur_list = self.Shikimori.animes
            cur_list_index = self.ui.list_anime.currentIndex()
        img_url = cur_list[cur_list_index.row()].get('image').get('original')
        img_id = img_url.rfind('?')
        r = self.get_html(f'{URL}{img_url}')
        with open(f'Shikimori/images/{img_url[img_id + 1:]}.jpg', 'wb') as f:
            f.write(r.content)

    def clicked_main(self):
        self.cur_window = 'shikimori_main'
        self.window.setWindowTitle('Shikimori Main')
        self.window.setCurrentIndex(0)

    def clicked_login(self):
        self.cur_window = 'shikimori_account'
        self.window.setWindowTitle('Shikimori Account')
        self.window.setCurrentIndex(1)

    def clicked_account(self):
        self.Form_login_dialog.setWindowTitle('Login')
        self.Form_login_dialog.setMinimumSize(450, 150)
        self.Form_login_dialog.setMaximumSize(450, 150)
        self.Form_login_dialog.show()

    def clicked_account_login(self):
        code = self.ui_login_dialog.txt_login.text()
        self.session.fetch_token(code)
        self.whoami.update(self.session.get('https://shikimori.one/api/users/whoami').json())
        if self.whoami.get('nickname'):
            self.is_login = True
            self.Form_login_dialog.close()
        else:
            self.is_login = False
        self.ui_login.username.setText(self.whoami.get('nickname'))

    def login(self):
        webbrowser.open_new_tab(self.session.get_auth_url())
        self.ui_login_dialog.btn_login.setEnabled(True)

    def change_page(self, page):
        if page == '+':
            self.current_page += 1
        elif self.current_page > 1:
            self.current_page -= 1
        else:
            return None
        self.ui.label_page.setText(f'Страница {self.current_page}')
        self.get_content()

    def change_page_login(self, page):
        if not self.current_list_login:
            return None
        if page == '+':
            self.current_page_login += 1
        elif self.current_page_login > 1:
            self.current_page_login -= 1
        else:
            return None
        self.ui_login.lbl_page.setText(f'Страница {self.current_page_login}')
        self.get_content_login()

    def change_list_login(self, lists=''):
        if not self.is_login:
            return None
        self.ui_login.animes.clear()
        self.current_page_login = 1
        self.params_login = {'page': self.current_page_login, 'limit': 50, 'order': 'name'}
        self.ui_login.lbl_page.setText(f'Страница {self.current_page_login}')
        if lists == 'p':
            self.params_login.update({'mylist': 'planned'})
        elif lists == 'w':
            self.params_login.update({'mylist': 'watching'})
        elif lists == 'c':
            self.params_login.update({'mylist': 'completed'})
        elif lists == 'r':
            self.params_login.update({'mylist': 'rewatching'})
        elif lists == 'o':
            self.params_login.update({'mylist': 'on_hold'})
        elif lists == 'd':
            self.params_login.update({'mylist': 'dropped'})
        self.current_list_login = self.params_login.get('mylist')
        self.get_content_login()

    def filter(self):
        self.current_page = 1
        self.ui.label_page.setText(f'Страница {self.current_page}')
        self.params = {'limit': 50}
        for i in self.sorts:
            if i.isChecked():
                self.params.update({'order': self.sorts.get(i)})
        a = ','.join([self.types.get(i) for i in self.types if i.isChecked()])
        if len(a) != 0:
            self.params.update({'kind': a})
        a = ','.join([self.statuses.get(i) for i in self.statuses if i.isChecked()])
        if len(a) != 0:
            self.params.update({'status': a})
        a = ','.join([self.durations.get(i) for i in self.durations if i.isChecked()])
        if len(a) != 0:
            self.params.update({'duration': a})
        a = ','.join([self.ratings.get(i) for i in self.ratings if i.isChecked()])
        if len(a) != 0:
            self.params.update({'rating': a})
        if self.ui.line_search.text() != '':
            self.params.update({'search': self.ui.line_search.text()})
        self.get_content()

    def filter_reset(self):
        self.current_page = 1
        self.ui.label_page.setText(f'Страница {self.current_page}')
        self.params = {'limit': 50, 'order': 'status'}
        self.ui.sort_status.setChecked(True)
        self.ui.line_search.setText('')
        [i.setChecked(False) for i in self.types]
        [i.setChecked(False) for i in self.statuses]
        [i.setChecked(False) for i in self.durations]
        [i.setChecked(False) for i in self.ratings]
        self.get_content()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    a = App()
    sys.exit(app.exec())

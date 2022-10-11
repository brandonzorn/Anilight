from PySide6.QtWidgets import QWidget
from data.ui.shikimoriUI import Ui_Dialog


class Facial(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
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
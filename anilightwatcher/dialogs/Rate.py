from PySide6.QtWidgets import QDialog
from anilightwatcher.items import Manga
from anilightwatcher.utils.catalog_manager import get_catalog, get_lib_catalog

from const.lists import lib_lists_en, lib_lists_ru
from data.ui.rate import Ui_Dialog


class FormRate(QDialog):
    def __init__(self):
        super().__init__(None)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.lib_list_box.addItems([i.capitalize() for i in lib_lists_ru])
        self.ui.update_btn.clicked.connect(self.send_rate)
        self.ui.cancel_btn.clicked.connect(lambda: self.close())
        self.ui.delete_btn.clicked.connect(self.delete_rate)
        self.catalog = None
        self.manga = None
        self.user_rate = None

    def setup(self, manga: Manga):
        self.manga = manga
        self.setWindowTitle(f'{self.manga.get_name()}')
        self.catalog = get_lib_catalog(get_catalog(manga.catalog_id))()
        if not self.catalog.check_user_rate(self.manga):
            self.catalog.create_user_rate(self.manga)
        self.user_rate = self.catalog.get_user_rate(self.manga)
        self.ui.score_box.setValue(self.user_rate.score)
        self.ui.chapters_box.setValue(self.user_rate.chapters)
        if self.manga.chapters:
            self.ui.chapters_box.setMaximum(self.manga.chapters)
        self.ui.lib_list_box.setCurrentIndex(lib_lists_en.index(self.user_rate.status))

    def send_rate(self):
        self.user_rate.score = self.ui.score_box.value()
        self.user_rate.chapters = self.ui.chapters_box.value()
        self.user_rate.status = lib_lists_en[self.ui.lib_list_box.currentIndex()]
        self.catalog.update_user_rate(self.user_rate)
        self.close()

    def delete_rate(self):
        self.catalog.delete_user_rate(self.user_rate)
        self.close()

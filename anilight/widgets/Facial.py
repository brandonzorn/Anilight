from PySide6.QtWidgets import QWidget
from data.ui.facial import Ui_Form


class Facial(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.current_page = 1
        self.ui.prev_btn.clicked.connect(lambda: self.change_page('-'))
        self.ui.next_btn.clicked.connect(lambda: self.change_page('+'))

    def change_page(self, page):
        if page == '+':
            self.current_page += 1
        elif self.current_page > 1:
            self.current_page -= 1
        else:
            return None
        self.ui.page_label.setText(f'Страница {self.current_page}')
        self.get_content()

    def search(self):
        self.current_page = 1

    def get_content(self):
        pass

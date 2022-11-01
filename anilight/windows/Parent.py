from PySide6.QtWidgets import QMainWindow

from anilight.widgets.Facial import Facial
from anilight.widgets.Library import Library
from anilight.widgets.Shikimori import Shikimori
from data.ui.mainWindow import Ui_MainWindow


class ParentWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.Form_facial = Facial()
        self.Form_shikimori = Shikimori()
        self.Form_library = Library()

        self.ui.btn_library.clicked.connect(lambda: self.change_widget(self.Form_library))
        self.ui.btn_main.clicked.connect(lambda: self.change_widget(self.Form_facial))
        self.ui.btn_shikimori.clicked.connect(lambda: self.change_widget(self.Form_shikimori))
        self.ui.btn_history.clicked.connect(lambda: self.change_widget(None))

    def change_widget(self, widget):
        if self.ui.top_item.currentWidget():
            self.ui.top_item.removeWidget(self.ui.top_item.currentWidget())
        self.ui.top_item.addWidget(widget)

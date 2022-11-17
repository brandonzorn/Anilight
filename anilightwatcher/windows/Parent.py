from PySide6.QtWidgets import QMainWindow

from anilightwatcher.widgets import FormShikimori, FormLibrary, FormFacial, FormHistory, FormInfo
from data.ui.mainWindow import Ui_MainWindow


class ParentWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.Form_facial = FormFacial()
        self.Form_library = FormLibrary()
        self.Form_shikimori = FormShikimori()
        self.Form_history = FormHistory()

        self.ui.btn_main.clicked.connect(lambda: self.change_widget(self.Form_facial))
        self.ui.btn_library.clicked.connect(lambda: self.change_widget(self.Form_library))
        self.ui.btn_shikimori.clicked.connect(lambda: self.change_widget(self.Form_shikimori))
        self.ui.btn_history.clicked.connect(lambda: self.change_widget(self.Form_history))

        self.change_widget(self.Form_facial)

    def change_widget(self, widget):
        if self.ui.top_item.currentWidget() == widget:
            return
        widget.setup()
        widget.ui.items_list.doubleClicked.disconnect()
        widget.ui.items_list.doubleClicked.connect(lambda: self.open_info(widget.get_current_manga()))
        if self.ui.top_item.currentWidget():
            self.ui.top_item.removeWidget(self.ui.top_item.currentWidget())
        self.ui.top_item.addWidget(widget)
        self.ui.top_item.setCurrentWidget(widget)

    def open_info(self, manga):
        info = FormInfo()
        info.setup(manga)
        info.ui.back_btn.clicked.connect(self.back)
        self.ui.side_menu_widget.hide()
        self.ui.top_item.addWidget(info)
        self.ui.top_item.setCurrentWidget(info)

    def back(self):
        self.ui.side_menu_widget.show()
        self.ui.top_item.currentWidget().deleteLater()
        self.ui.top_item.removeWidget(self.ui.top_item.currentWidget())

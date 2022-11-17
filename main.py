import sys

from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import *

from anilightwatcher.utils import init_app_paths
from anilightwatcher.windows.Parent import ParentWindow
from const.app import APP_NAME, APP_VERSION
from const.icons import app_icon_path


class App(ParentWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Anilight")
        self.show()


if __name__ == '__main__':
    QApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.RoundPreferFloor)
    QApplication.setStyle('Fusion')
    app = QApplication(sys.argv)
    app.setApplicationDisplayName(APP_NAME)
    app.setApplicationVersion(APP_VERSION)
    app.setWindowIcon(QIcon(app_icon_path))
    app_paths = [APP_NAME]
    init_app_paths(app_paths)
    a = App()
    sys.exit(app.exec())

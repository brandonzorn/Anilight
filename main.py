import sys
from PySide6.QtWidgets import *
from anilight.windows.Parent import ParentWindow


class App(ParentWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Shikimori')
        # self.setWindowIcon(QIcon(self.icon_path))
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    a = App()
    sys.exit(app.exec())

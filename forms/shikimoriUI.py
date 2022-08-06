# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'shikimoriUI.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QDialog, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QListWidget,
    QListWidgetItem, QPushButton, QRadioButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(815, 610)
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(45, 45, 45, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Light, brush1)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush1)
        palette.setBrush(QPalette.Active, QPalette.Dark, brush1)
        palette.setBrush(QPalette.Active, QPalette.Mid, brush1)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette.setBrush(QPalette.Active, QPalette.Shadow, brush1)
        brush2 = QBrush(QColor(0, 133, 62, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Highlight, brush2)
        palette.setBrush(QPalette.Active, QPalette.AlternateBase, brush1)
        palette.setBrush(QPalette.Active, QPalette.ToolTipBase, brush1)
        brush3 = QBrush(QColor(236, 240, 241, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ToolTipText, brush3)
        brush4 = QBrush(QColor(199, 203, 203, 128))
        brush4.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush4)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Dark, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Shadow, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Highlight, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush4)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Dark, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Shadow, brush1)
        brush5 = QBrush(QColor(0, 120, 215, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Highlight, brush5)
        palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        Dialog.setPalette(palette)
        Dialog.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(45, 45, 45);")
        self.gridLayout_2 = QGridLayout(Dialog)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.btn_main = QPushButton(Dialog)
        self.btn_main.setObjectName(u"btn_main")
        self.btn_main.setStyleSheet(u"background-color: rgb(0, 133, 52);\n"
"color: rgb(255, 255, 255);")

        self.verticalLayout_2.addWidget(self.btn_main)

        self.btn_login = QPushButton(Dialog)
        self.btn_login.setObjectName(u"btn_login")
        self.btn_login.setStyleSheet(u"background-color: rgb(0, 133, 52);\n"
"color: rgb(255, 255, 255);")

        self.verticalLayout_2.addWidget(self.btn_login)

        self.btn_desu = QPushButton(Dialog)
        self.btn_desu.setObjectName(u"btn_desu")
        self.btn_desu.setStyleSheet(u"background-color: rgb(0, 133, 52);\n"
"color: rgb(255, 255, 255);")

        self.verticalLayout_2.addWidget(self.btn_desu)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)


        self.gridLayout_2.addLayout(self.verticalLayout_2, 0, 0, 1, 1)

        self.list_anime = QListWidget(Dialog)
        self.list_anime.setObjectName(u"list_anime")
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Light, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Midlight, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Dark, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Mid, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Text, brush)
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Shadow, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Highlight, brush2)
        palette1.setBrush(QPalette.Active, QPalette.AlternateBase, brush1)
        palette1.setBrush(QPalette.Active, QPalette.ToolTipBase, brush1)
        palette1.setBrush(QPalette.Active, QPalette.ToolTipText, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Active, QPalette.PlaceholderText, brush4)
#endif
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Light, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Midlight, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Dark, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Mid, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Shadow, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Highlight, brush2)
        palette1.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush4)
#endif
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Light, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Midlight, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Dark, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Mid, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Shadow, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Highlight, brush5)
        palette1.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.list_anime.setPalette(palette1)
        self.list_anime.setAutoFillBackground(False)

        self.gridLayout_2.addWidget(self.list_anime, 0, 1, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.sort_date = QRadioButton(Dialog)
        self.sort_date.setObjectName(u"sort_date")

        self.gridLayout.addWidget(self.sort_date, 4, 0, 1, 1)

        self.raiting_r17 = QCheckBox(Dialog)
        self.raiting_r17.setObjectName(u"raiting_r17")
        self.raiting_r17.setChecked(False)
        self.raiting_r17.setTristate(False)

        self.gridLayout.addWidget(self.raiting_r17, 16, 1, 1, 1)

        self.label_status = QLabel(Dialog)
        self.label_status.setObjectName(u"label_status")

        self.gridLayout.addWidget(self.label_status, 18, 0, 1, 1)

        self.sort_name = QRadioButton(Dialog)
        self.sort_name.setObjectName(u"sort_name")

        self.gridLayout.addWidget(self.sort_name, 3, 0, 1, 1)

        self.raiting_g = QCheckBox(Dialog)
        self.raiting_g.setObjectName(u"raiting_g")
        self.raiting_g.setChecked(False)
        self.raiting_g.setTristate(False)

        self.gridLayout.addWidget(self.raiting_g, 15, 0, 1, 1)

        self.episodes_29m = QCheckBox(Dialog)
        self.episodes_29m.setObjectName(u"episodes_29m")
        self.episodes_29m.setChecked(False)
        self.episodes_29m.setTristate(False)

        self.gridLayout.addWidget(self.episodes_29m, 12, 1, 1, 1)

        self.type_special = QCheckBox(Dialog)
        self.type_special.setObjectName(u"type_special")
        self.type_special.setChecked(False)
        self.type_special.setTristate(False)

        self.gridLayout.addWidget(self.type_special, 8, 0, 1, 1)

        self.status_ongoing = QCheckBox(Dialog)
        self.status_ongoing.setObjectName(u"status_ongoing")
        self.status_ongoing.setChecked(False)
        self.status_ongoing.setTristate(False)

        self.gridLayout.addWidget(self.status_ongoing, 19, 1, 1, 1)

        self.label_sort = QLabel(Dialog)
        self.label_sort.setObjectName(u"label_sort")

        self.gridLayout.addWidget(self.label_sort, 0, 0, 1, 1)

        self.type_music = QCheckBox(Dialog)
        self.type_music.setObjectName(u"type_music")
        self.type_music.setChecked(False)
        self.type_music.setTristate(False)

        self.gridLayout.addWidget(self.type_music, 8, 1, 1, 1)

        self.label_episodes = QLabel(Dialog)
        self.label_episodes.setObjectName(u"label_episodes")

        self.gridLayout.addWidget(self.label_episodes, 11, 0, 1, 1)

        self.raiting_pg13 = QCheckBox(Dialog)
        self.raiting_pg13.setObjectName(u"raiting_pg13")
        self.raiting_pg13.setChecked(False)
        self.raiting_pg13.setTristate(False)

        self.gridLayout.addWidget(self.raiting_pg13, 16, 0, 1, 1)

        self.sort_id = QRadioButton(Dialog)
        self.sort_id.setObjectName(u"sort_id")

        self.gridLayout.addWidget(self.sort_id, 1, 0, 1, 1)

        self.type_ona = QCheckBox(Dialog)
        self.type_ona.setObjectName(u"type_ona")
        self.type_ona.setChecked(False)
        self.type_ona.setTristate(False)

        self.gridLayout.addWidget(self.type_ona, 7, 1, 1, 1)

        self.status_release = QCheckBox(Dialog)
        self.status_release.setObjectName(u"status_release")
        self.status_release.setChecked(False)
        self.status_release.setTristate(False)

        self.gridLayout.addWidget(self.status_release, 19, 0, 1, 1)

        self.type_tv13 = QCheckBox(Dialog)
        self.type_tv13.setObjectName(u"type_tv13")
        self.type_tv13.setChecked(False)
        self.type_tv13.setTristate(False)

        self.gridLayout.addWidget(self.type_tv13, 9, 0, 1, 1)

        self.type_tv = QCheckBox(Dialog)
        self.type_tv.setObjectName(u"type_tv")
        self.type_tv.setChecked(False)
        self.type_tv.setTristate(False)

        self.gridLayout.addWidget(self.type_tv, 6, 0, 1, 1)

        self.raiting_rx = QCheckBox(Dialog)
        self.raiting_rx.setObjectName(u"raiting_rx")
        self.raiting_rx.setChecked(False)
        self.raiting_rx.setTristate(False)

        self.gridLayout.addWidget(self.raiting_rx, 17, 1, 1, 1)

        self.type_film = QCheckBox(Dialog)
        self.type_film.setObjectName(u"type_film")
        self.type_film.setChecked(False)
        self.type_film.setTristate(False)

        self.gridLayout.addWidget(self.type_film, 6, 1, 1, 1)

        self.episodes_10m = QCheckBox(Dialog)
        self.episodes_10m.setObjectName(u"episodes_10m")
        self.episodes_10m.setChecked(False)
        self.episodes_10m.setTristate(False)

        self.gridLayout.addWidget(self.episodes_10m, 12, 0, 1, 1)

        self.raiting_pg = QCheckBox(Dialog)
        self.raiting_pg.setObjectName(u"raiting_pg")
        self.raiting_pg.setChecked(False)
        self.raiting_pg.setTristate(False)

        self.gridLayout.addWidget(self.raiting_pg, 15, 1, 1, 1)

        self.episodes_30m = QCheckBox(Dialog)
        self.episodes_30m.setObjectName(u"episodes_30m")
        self.episodes_30m.setChecked(False)
        self.episodes_30m.setTristate(False)

        self.gridLayout.addWidget(self.episodes_30m, 13, 0, 1, 1)

        self.type_tv24 = QCheckBox(Dialog)
        self.type_tv24.setObjectName(u"type_tv24")
        self.type_tv24.setChecked(False)
        self.type_tv24.setTristate(False)

        self.gridLayout.addWidget(self.type_tv24, 9, 1, 1, 1)

        self.sort_popular = QRadioButton(Dialog)
        self.sort_popular.setObjectName(u"sort_popular")

        self.gridLayout.addWidget(self.sort_popular, 2, 1, 1, 1)

        self.label_type = QLabel(Dialog)
        self.label_type.setObjectName(u"label_type")

        self.gridLayout.addWidget(self.label_type, 5, 0, 1, 1)

        self.sort_raiting = QRadioButton(Dialog)
        self.sort_raiting.setObjectName(u"sort_raiting")

        self.gridLayout.addWidget(self.sort_raiting, 1, 1, 1, 1)

        self.sort_episodes = QRadioButton(Dialog)
        self.sort_episodes.setObjectName(u"sort_episodes")

        self.gridLayout.addWidget(self.sort_episodes, 4, 1, 1, 1)

        self.status_anons = QCheckBox(Dialog)
        self.status_anons.setObjectName(u"status_anons")
        self.status_anons.setChecked(False)
        self.status_anons.setTristate(False)

        self.gridLayout.addWidget(self.status_anons, 20, 0, 1, 1)

        self.type_ova = QCheckBox(Dialog)
        self.type_ova.setObjectName(u"type_ova")
        self.type_ova.setChecked(False)
        self.type_ova.setTristate(False)

        self.gridLayout.addWidget(self.type_ova, 7, 0, 1, 1)

        self.sort_type = QRadioButton(Dialog)
        self.sort_type.setObjectName(u"sort_type")

        self.gridLayout.addWidget(self.sort_type, 2, 0, 1, 1)

        self.type_tv48 = QCheckBox(Dialog)
        self.type_tv48.setObjectName(u"type_tv48")
        self.type_tv48.setChecked(False)
        self.type_tv48.setTristate(False)

        self.gridLayout.addWidget(self.type_tv48, 10, 0, 1, 1)

        self.label_raiting = QLabel(Dialog)
        self.label_raiting.setObjectName(u"label_raiting")

        self.gridLayout.addWidget(self.label_raiting, 14, 0, 1, 1)

        self.raiting_rp = QCheckBox(Dialog)
        self.raiting_rp.setObjectName(u"raiting_rp")
        self.raiting_rp.setChecked(False)
        self.raiting_rp.setTristate(False)

        self.gridLayout.addWidget(self.raiting_rp, 17, 0, 1, 1)

        self.sort_status = QRadioButton(Dialog)
        self.sort_status.setObjectName(u"sort_status")
        self.sort_status.setChecked(True)

        self.gridLayout.addWidget(self.sort_status, 3, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 21, 0, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)


        self.gridLayout_2.addLayout(self.verticalLayout, 0, 2, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.line_search = QLineEdit(Dialog)
        self.line_search.setObjectName(u"line_search")
        self.line_search.setStyleSheet(u"background-color: rgb(45, 45, 45);\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout_2.addWidget(self.line_search)

        self.btn_search = QPushButton(Dialog)
        self.btn_search.setObjectName(u"btn_search")
        self.btn_search.setStyleSheet(u"background-color: rgb(0, 133, 52);\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout_2.addWidget(self.btn_search)

        self.prev_page = QPushButton(Dialog)
        self.prev_page.setObjectName(u"prev_page")
        self.prev_page.setStyleSheet(u"background-color: rgb(0, 133, 52);\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout_2.addWidget(self.prev_page)

        self.label_page = QLabel(Dialog)
        self.label_page.setObjectName(u"label_page")

        self.horizontalLayout_2.addWidget(self.label_page)

        self.next_page = QPushButton(Dialog)
        self.next_page.setObjectName(u"next_page")
        self.next_page.setStyleSheet(u"background-color: rgb(0, 133, 52);\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout_2.addWidget(self.next_page)


        self.gridLayout_2.addLayout(self.horizontalLayout_2, 1, 1, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.filter_reset = QPushButton(Dialog)
        self.filter_reset.setObjectName(u"filter_reset")
        self.filter_reset.setStyleSheet(u"background-color: rgb(0, 133, 52);\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout.addWidget(self.filter_reset)

        self.filter_apply = QPushButton(Dialog)
        self.filter_apply.setObjectName(u"filter_apply")
        self.filter_apply.setStyleSheet(u"background-color: rgb(0, 133, 52);\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout.addWidget(self.filter_apply)


        self.gridLayout_2.addLayout(self.horizontalLayout, 1, 2, 1, 1)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.btn_main.setText(QCoreApplication.translate("Dialog", u"Main", None))
        self.btn_login.setText(QCoreApplication.translate("Dialog", u"Login", None))
        self.btn_desu.setText(QCoreApplication.translate("Dialog", u"Desu", None))
        self.sort_date.setText(QCoreApplication.translate("Dialog", u"\u0414\u0430\u0442\u0430 \u0432\u044b\u0445\u043e\u0434\u0430", None))
        self.raiting_r17.setText(QCoreApplication.translate("Dialog", u"R-17", None))
        self.label_status.setText(QCoreApplication.translate("Dialog", u"\u0421\u0442\u0430\u0442\u0443\u0441", None))
        self.sort_name.setText(QCoreApplication.translate("Dialog", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435", None))
        self.raiting_g.setText(QCoreApplication.translate("Dialog", u"G", None))
        self.episodes_29m.setText(QCoreApplication.translate("Dialog", u"\u0414\u043e 30 \u043c\u0438\u043d", None))
        self.type_special.setText(QCoreApplication.translate("Dialog", u"\u0421\u043f\u0435\u0448\u043b", None))
        self.status_ongoing.setText(QCoreApplication.translate("Dialog", u"\u041e\u043d\u0433\u043e\u0438\u043d\u0433", None))
        self.label_sort.setText(QCoreApplication.translate("Dialog", u"\u0421\u043e\u0440\u0442\u0438\u0440\u043e\u0432\u043a\u0430", None))
        self.type_music.setText(QCoreApplication.translate("Dialog", u"\u041c\u0443\u0437\u044b\u043a\u0430", None))
        self.label_episodes.setText(QCoreApplication.translate("Dialog", u"\u042d\u043f\u0438\u0437\u043e\u0434\u044b", None))
        self.raiting_pg13.setText(QCoreApplication.translate("Dialog", u"PG-13", None))
        self.sort_id.setText(QCoreApplication.translate("Dialog", u"ID", None))
        self.type_ona.setText(QCoreApplication.translate("Dialog", u"ONA", None))
        self.status_release.setText(QCoreApplication.translate("Dialog", u"\u0420\u0435\u043b\u0438\u0437", None))
        self.type_tv13.setText(QCoreApplication.translate("Dialog", u"TV 13", None))
        self.type_tv.setText(QCoreApplication.translate("Dialog", u"TV", None))
        self.raiting_rx.setText(QCoreApplication.translate("Dialog", u"Rx", None))
        self.type_film.setText(QCoreApplication.translate("Dialog", u"\u0424\u0438\u043b\u044c\u043c", None))
        self.episodes_10m.setText(QCoreApplication.translate("Dialog", u"\u0414\u043e 10 \u043c\u0438\u043d", None))
        self.raiting_pg.setText(QCoreApplication.translate("Dialog", u"PG", None))
        self.episodes_30m.setText(QCoreApplication.translate("Dialog", u"\u0411\u043e\u043b\u044c\u0448\u0435 30 \u043c\u0438\u043d", None))
        self.type_tv24.setText(QCoreApplication.translate("Dialog", u"TV 24", None))
        self.sort_popular.setText(QCoreApplication.translate("Dialog", u"\u041f\u043e\u043f\u0443\u043b\u044f\u0440\u043d\u043e\u0441\u0442\u044c", None))
        self.label_type.setText(QCoreApplication.translate("Dialog", u"\u0422\u0438\u043f", None))
        self.sort_raiting.setText(QCoreApplication.translate("Dialog", u"\u0420\u0435\u0439\u0442\u0438\u043d\u0433", None))
        self.sort_episodes.setText(QCoreApplication.translate("Dialog", u"\u042d\u043f\u0438\u0437\u043e\u0434\u044b", None))
        self.status_anons.setText(QCoreApplication.translate("Dialog", u"\u0410\u043d\u043e\u043d\u0441", None))
        self.type_ova.setText(QCoreApplication.translate("Dialog", u"OVA", None))
        self.sort_type.setText(QCoreApplication.translate("Dialog", u"\u0422\u0438\u043f", None))
        self.type_tv48.setText(QCoreApplication.translate("Dialog", u"TV 48", None))
        self.label_raiting.setText(QCoreApplication.translate("Dialog", u"\u0420\u0435\u0439\u0442\u0438\u043d\u0433", None))
        self.raiting_rp.setText(QCoreApplication.translate("Dialog", u"R+", None))
        self.sort_status.setText(QCoreApplication.translate("Dialog", u"\u0421\u0442\u0430\u0442\u0443\u0441", None))
        self.btn_search.setText(QCoreApplication.translate("Dialog", u"\u041f\u043e\u0438\u0441\u043a", None))
        self.prev_page.setText(QCoreApplication.translate("Dialog", u"<", None))
        self.label_page.setText(QCoreApplication.translate("Dialog", u" \u0421\u0442\u0440\u0430\u043d\u0438\u0446\u0430 1", None))
        self.next_page.setText(QCoreApplication.translate("Dialog", u">", None))
        self.filter_reset.setText(QCoreApplication.translate("Dialog", u"\u0421\u0431\u0440\u043e\u0441\u0438\u0442\u044c", None))
        self.filter_apply.setText(QCoreApplication.translate("Dialog", u"\u041f\u0440\u0438\u043c\u0435\u043d\u0438\u0442\u044c", None))
    # retranslateUi


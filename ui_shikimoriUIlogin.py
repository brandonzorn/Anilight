# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'shikimoriUIloginifPaTs.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(698, 511)
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
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.btn_dropped = QPushButton(Dialog)
        self.btn_dropped.setObjectName(u"btn_dropped")
        self.btn_dropped.setStyleSheet(u"background-color: rgb(0, 127, 50);")

        self.gridLayout.addWidget(self.btn_dropped, 5, 6, 1, 1)

        self.btn_login = QPushButton(Dialog)
        self.btn_login.setObjectName(u"btn_login")
        self.btn_login.setStyleSheet(u"background-color: rgb(0, 133, 52);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.btn_login, 1, 0, 1, 1)

        self.btn_completed = QPushButton(Dialog)
        self.btn_completed.setObjectName(u"btn_completed")
        self.btn_completed.setStyleSheet(u"background-color: rgb(0, 133, 52);")

        self.gridLayout.addWidget(self.btn_completed, 3, 6, 1, 1)

        self.txt_search = QLineEdit(Dialog)
        self.txt_search.setObjectName(u"txt_search")

        self.gridLayout.addWidget(self.txt_search, 7, 1, 1, 1)

        self.lbl = QLabel(Dialog)
        self.lbl.setObjectName(u"lbl")

        self.gridLayout.addWidget(self.lbl, 6, 6, 1, 1)

        self.btn_options = QPushButton(Dialog)
        self.btn_options.setObjectName(u"btn_options")
        self.btn_options.setStyleSheet(u"background-color: rgb(0, 133, 52);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.btn_options, 2, 0, 1, 1)

        self.username = QLabel(Dialog)
        self.username.setObjectName(u"username")

        self.gridLayout.addWidget(self.username, 7, 0, 1, 1)

        self.btn_on_hold = QPushButton(Dialog)
        self.btn_on_hold.setObjectName(u"btn_on_hold")
        self.btn_on_hold.setStyleSheet(u"background-color: rgb(0, 132, 52);")

        self.gridLayout.addWidget(self.btn_on_hold, 4, 6, 1, 1)

        self.prev_page = QPushButton(Dialog)
        self.prev_page.setObjectName(u"prev_page")
        self.prev_page.setStyleSheet(u"background-color: rgb(0, 133, 52);")

        self.gridLayout.addWidget(self.prev_page, 7, 3, 1, 1)

        self.lbl_page = QLabel(Dialog)
        self.lbl_page.setObjectName(u"lbl_page")

        self.gridLayout.addWidget(self.lbl_page, 7, 4, 1, 1)

        self.btn_rewatching = QPushButton(Dialog)
        self.btn_rewatching.setObjectName(u"btn_rewatching")
        self.btn_rewatching.setStyleSheet(u"background-color: rgb(0, 133, 52);")

        self.gridLayout.addWidget(self.btn_rewatching, 2, 6, 1, 1)

        self.animes = QListWidget(Dialog)
        self.animes.setObjectName(u"animes")

        self.gridLayout.addWidget(self.animes, 0, 1, 7, 5)

        self.btn_main = QPushButton(Dialog)
        self.btn_main.setObjectName(u"btn_main")
        self.btn_main.setStyleSheet(u"background-color: rgb(0, 133, 52);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.btn_main, 0, 0, 1, 1)

        self.btn_account = QPushButton(Dialog)
        self.btn_account.setObjectName(u"btn_account")
        self.btn_account.setStyleSheet(u"background-color: rgb(0, 127, 50);")

        self.gridLayout.addWidget(self.btn_account, 7, 6, 1, 1)

        self.btn_watching = QPushButton(Dialog)
        self.btn_watching.setObjectName(u"btn_watching")
        self.btn_watching.setStyleSheet(u"background-color: rgb(0, 133, 52);")

        self.gridLayout.addWidget(self.btn_watching, 1, 6, 1, 1)

        self.lbl_username = QLabel(Dialog)
        self.lbl_username.setObjectName(u"lbl_username")
        self.lbl_username.setStyleSheet(u"font: 87 9pt \"Segoe UI Black\";")

        self.gridLayout.addWidget(self.lbl_username, 6, 0, 1, 1)

        self.next_page = QPushButton(Dialog)
        self.next_page.setObjectName(u"next_page")
        self.next_page.setStyleSheet(u"background-color: rgb(0, 133, 52);")

        self.gridLayout.addWidget(self.next_page, 7, 5, 1, 1)

        self.btn_planned = QPushButton(Dialog)
        self.btn_planned.setObjectName(u"btn_planned")
        self.btn_planned.setStyleSheet(u"background-color: rgb(0, 133, 52);")

        self.gridLayout.addWidget(self.btn_planned, 0, 6, 1, 1)

        self.btn_search = QPushButton(Dialog)
        self.btn_search.setObjectName(u"btn_search")
        self.btn_search.setStyleSheet(u"background-color: rgb(0, 127, 50);")

        self.gridLayout.addWidget(self.btn_search, 7, 2, 1, 1)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.btn_dropped.setText(QCoreApplication.translate("Dialog", u"\u0411\u0440\u043e\u0448\u0435\u043d\u043e", None))
        self.btn_login.setText(QCoreApplication.translate("Dialog", u"Login", None))
        self.btn_completed.setText(QCoreApplication.translate("Dialog", u"\u041f\u0440\u043e\u0441\u043c\u043e\u0442\u0440\u0435\u043d\u043e", None))
        self.lbl.setText("")
        self.btn_options.setText(QCoreApplication.translate("Dialog", u"Options", None))
        self.username.setText("")
        self.btn_on_hold.setText(QCoreApplication.translate("Dialog", u"\u041e\u0442\u043b\u043e\u0436\u0435\u043d\u043e", None))
        self.prev_page.setText(QCoreApplication.translate("Dialog", u"<", None))
        self.lbl_page.setText(QCoreApplication.translate("Dialog", u"\u0421\u0442\u0440\u0430\u043d\u0438\u0446\u0430 1", None))
        self.btn_rewatching.setText(QCoreApplication.translate("Dialog", u"\u041f\u0435\u0440\u0435\u0441\u043c\u0430\u0442\u0440\u0438\u0432\u0430\u044e", None))
        self.btn_main.setText(QCoreApplication.translate("Dialog", u"Main", None))
        self.btn_account.setText(QCoreApplication.translate("Dialog", u"\u0410\u043a\u043a\u0430\u0443\u043d\u0442", None))
        self.btn_watching.setText(QCoreApplication.translate("Dialog", u"\u0421\u043c\u043e\u0442\u0440\u044e", None))
        self.lbl_username.setText("")
        self.next_page.setText(QCoreApplication.translate("Dialog", u">", None))
        self.btn_planned.setText(QCoreApplication.translate("Dialog", u"\u0417\u0430\u043f\u043b\u0430\u043d\u0438\u0440\u043e\u0432\u0430\u043d\u043e", None))
        self.btn_search.setText(QCoreApplication.translate("Dialog", u"\u041f\u043e\u0438\u0441\u043a", None))
    # retranslateUi


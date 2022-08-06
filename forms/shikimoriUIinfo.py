# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'shikimoriUIinfo.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QGraphicsView, QGridLayout,
    QLabel, QPushButton, QSizePolicy, QTextBrowser,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(698, 513)
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
        self.widget_2 = QWidget(Dialog)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.widget_2.setStyleSheet(u"background-color: rgb(29, 31, 33);")
        self.gridLayout_2 = QGridLayout(self.widget_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.textBrowser_2 = QTextBrowser(self.widget_2)
        self.textBrowser_2.setObjectName(u"textBrowser_2")

        self.gridLayout_2.addWidget(self.textBrowser_2, 0, 2, 1, 1)

        self.graphicsView = QGraphicsView(self.widget_2)
        self.graphicsView.setObjectName(u"graphicsView")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.graphicsView.sizePolicy().hasHeightForWidth())
        self.graphicsView.setSizePolicy(sizePolicy1)
        self.graphicsView.setLayoutDirection(Qt.LeftToRight)

        self.gridLayout_2.addWidget(self.graphicsView, 0, 1, 1, 1)

        self.textBrowser = QTextBrowser(self.widget_2)
        self.textBrowser.setObjectName(u"textBrowser")

        self.gridLayout_2.addWidget(self.textBrowser, 1, 1, 1, 2)


        self.gridLayout.addWidget(self.widget_2, 1, 1, 1, 1)

        self.btn_main = QPushButton(Dialog)
        self.btn_main.setObjectName(u"btn_main")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btn_main.sizePolicy().hasHeightForWidth())
        self.btn_main.setSizePolicy(sizePolicy2)
        self.btn_main.setStyleSheet(u"background-color: rgb(0, 133, 52);\n"
"color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.btn_main, 0, 0, 1, 1)

        self.widget = QWidget(Dialog)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"background-color: rgb(29, 31, 33);")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 0, 561, 21))

        self.gridLayout.addWidget(self.widget, 0, 1, 1, 1)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.textBrowser.setHtml(QCoreApplication.translate("Dialog", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">\u0412\u0440\u0435\u043c\u044f \u0438\u0434\u0451\u0442, \u0430 \u0443\u0447\u0435\u043d\u0438\u043a\u0438 \u043c\u0430\u043b\u0435\u043d\u044c\u043a\u043e\u0439 \u0448\u043a\u043e\u043b\u044b \u0410\u0441\u0430\u0445\u0438\u0433\u0430\u043e\u043a\u0430, \u0440\u0430\u0441\u043f\u043e\u043b\u043e\u0436\u0435\u043d\u043d\u043e\u0439 \u0432 \u043e\u0434\u043d\u043e\u0439 \u0438\u0437 \u0433\u043b\u0443\u0431\u0438\u043d\u043e\u043a \u042f\u043f\u043e\u043d\u0438\u0438, \u043f\u043e-\u043f\u0440\u0435\u0436\u043d\u0435\u043c\u0443"
                        " \u043d\u0430\u0441\u043b\u0430\u0436\u0434\u0430\u044e\u0442\u0441\u044f \u0431\u0435\u0437\u043c\u044f\u0442\u0435\u0436\u043d\u044b\u043c\u0438 \u0431\u0443\u0434\u043d\u044f\u043c\u0438. \u041a\u0443\u043f\u0430\u044f\u0441\u044c \u0432 \u043b\u0443\u0447\u0430\u0445 \u043b\u0435\u0442\u043d\u0435\u0433\u043e \u0441\u043e\u043b\u043d\u0446\u0430, \u0441\u043a\u0440\u044b\u0432\u0430\u044f\u0441\u044c \u043e\u0442 \u0436\u0430\u0440\u044b \u0441\u0440\u0435\u0434\u0438 \u0442\u0435\u043d\u0438\u0441\u0442\u044b\u0445 \u0430\u043b\u043b\u0435\u0439, \u0440\u0435\u0431\u044f\u0442\u0430 \u0448\u0443\u043c\u044f\u0442 \u0438 \u0434\u0443\u0440\u0430\u0447\u0430\u0442\u0441\u044f. \u0410 \u043d\u0430 \u0441\u043c\u0435\u043d\u0443 \u0441\u0442\u0430\u0440\u044b\u043c \u0438\u0433\u0440\u0430\u043c \u0438 \u0437\u0430\u043d\u044f\u0442\u0438\u044f\u043c \u043f\u0440\u0438\u0445\u043e\u0434\u044f\u0442 \u043d\u043e\u0432\u044b\u0435, \u0431\u0443\u0434\u044c \u0442\u043e \u043d\u0430\u0431\u043b\u044e\u0434\u0435"
                        "\u043d\u0438\u0435 \u0437\u0430 \u0446\u0432\u0435\u0442\u0443\u0449\u0435\u0439 \u0432\u0438\u0448\u043d\u0435\u0439, \u0433\u043e\u043d\u043a\u0438 \u043d\u0430\u043f\u0435\u0440\u0435\u0433\u043e\u043d\u043a\u0438 \u2014 \u043d\u0435\u043f\u0440\u0435\u043c\u0435\u043d\u043d\u043e \u0431\u043e\u0441\u0438\u043a\u043e\u043c \u2014 \u043f\u043e \u043e\u0431\u043c\u0435\u043b\u0435\u0432\u0448\u0435\u043c\u0443 \u0440\u0443\u0441\u043b\u0443 \u0440\u0435\u043a\u0438, \u0432\u044b\u043a\u0430\u043f\u044b\u0432\u0430\u043d\u0438\u0435 \u043a\u0430\u0440\u0442\u043e\u0444\u0435\u043b\u044f \u0438\u043b\u0438 \u0441\u0442\u0440\u043e\u0438\u0442\u0435\u043b\u044c\u0441\u0442\u0432\u043e \u0437\u0438\u043c\u043d\u0435\u0433\u043e \u0436\u0438\u043b\u0438\u0449\u0430 \u044d\u0441\u043a\u0438\u043c\u043e\u0441\u043e\u0432 \u2014 \u0438\u0433\u043b\u0443. \u0412\u0435\u0434\u044c \u043d\u0435\u0442 \u043d\u0438\u0447\u0435\u0433\u043e \u043b\u0443\u0447\u0448\u0435 \u043f\u0440\u0438\u044f\u0442\u043d\u043e\u0439 \u043f"
                        "\u043e\u0432\u0441\u0435\u0434\u043d\u0435\u0432\u043d\u043e\u0441\u0442\u0438, \u0433\u0434\u0435 \u043c\u0438\u043d\u0443\u0442\u044b \u0441\u043a\u043b\u0430\u0434\u044b\u0432\u0430\u044e\u0442\u0441\u044f \u0432 \u0447\u0430\u0441\u044b \u043d\u0435\u0437\u0430\u0431\u044b\u0432\u0430\u0435\u043c\u043e\u0433\u043e \u0432\u0440\u0435\u043c\u044f\u043f\u0440\u0435\u043f\u0440\u043e\u0432\u043e\u0436\u0434\u0435\u043d\u0438\u044f, \u043f\u043b\u0435\u0447\u043e\u043c \u043a \u043f\u043b\u0435\u0447\u0443 \u0441 \u0438\u0441\u043a\u0440\u0435\u043d\u043d\u0438\u043c\u0438 \u0434\u0440\u0443\u0437\u044c\u044f\u043c\u0438. \u0418 \u0432\u043e\u0442, \u043a\u043e\u0433\u0434\u0430 \u043a\u0430\u0436\u0435\u0442\u0441\u044f, \u0431\u0443\u0434\u0442\u043e \u0438\u0441\u0442\u043e\u0440\u0438\u044f \u043e\u0441\u0442\u0430\u043d\u043e\u0432\u0438\u043b\u0430\u0441\u044c \u043d\u0430 \u043c\u0435\u0441\u0442\u0435, \u043d\u0443\u0436\u043d\u043e \u043f\u0440\u043e\u0441\u0442\u043e \u0432\u043d\u0438\u043c\u0430\u0442"
                        "\u0435\u043b\u044c\u043d\u043e \u043f\u0440\u0438\u0433\u043b\u044f\u0434\u0435\u0442\u044c\u0441\u044f, \u0438 \u043d\u0435 \u0437\u0430\u043c\u0435\u0442\u0438\u0448\u044c, \u043a\u0430\u043a \u0443\u0436\u0435 \u043d\u0430\u0448\u0451\u043b \u043e\u0442\u0434\u044b\u0445 \u0434\u043b\u044f \u0434\u0443\u0448\u0438. \u0414\u0443\u0448\u0438, \u0443\u043c\u0438\u0440\u043e\u0442\u0432\u043e\u0440\u0451\u043d\u043d\u043e\u0439 \u043f\u0440\u0438\u044f\u0442\u043d\u043e\u0439 \u0438 \u0442\u0440\u043e\u0433\u0430\u0442\u0435\u043b\u044c\u043d\u043e\u0439 \u043e\u0431\u044b\u0434\u0435\u043d\u043d\u043e\u0441\u0442\u044c\u044e \u0434\u0435\u0440\u0435\u0432\u0435\u043d\u0441\u043a\u043e\u0439 \u0433\u043b\u0443\u0431\u0438\u043d\u043a\u0438.</span></p></body></html>", None))
        self.btn_main.setText(QCoreApplication.translate("Dialog", u"\u041d\u0430\u0437\u0430\u0434", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u0414\u0435\u0440\u0435\u0432\u0435\u043d\u0441\u043a\u0430\u044f \u0433\u043b\u0443\u0431\u0438\u043d\u043a\u0430 2 ", None))
    # retranslateUi


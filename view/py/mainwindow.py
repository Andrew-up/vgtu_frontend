# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLayout,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QStatusBar, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(747, 613)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_4 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetMinimumSize)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(-1, -1, -1, 0)
        self.logo_company_main = QLabel(self.centralwidget)
        self.logo_company_main.setObjectName(u"logo_company_main")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.logo_company_main.sizePolicy().hasHeightForWidth())
        self.logo_company_main.setSizePolicy(sizePolicy)
        self.logo_company_main.setMinimumSize(QSize(0, 10))
        self.logo_company_main.setStyleSheet(u"background-color: rgb(50, 255, 39);")

        self.horizontalLayout.addWidget(self.logo_company_main)

        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout_2 = QHBoxLayout(self.widget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.notification_button_main = QPushButton(self.widget)
        self.notification_button_main.setObjectName(u"notification_button_main")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.notification_button_main.sizePolicy().hasHeightForWidth())
        self.notification_button_main.setSizePolicy(sizePolicy1)

        self.horizontalLayout_2.addWidget(self.notification_button_main)

        self.icon_profile_main = QPushButton(self.widget)
        self.icon_profile_main.setObjectName(u"icon_profile_main")
        sizePolicy1.setHeightForWidth(self.icon_profile_main.sizePolicy().hasHeightForWidth())
        self.icon_profile_main.setSizePolicy(sizePolicy1)

        self.horizontalLayout_2.addWidget(self.icon_profile_main)

        self.authorized_user = QPushButton(self.widget)
        self.authorized_user.setObjectName(u"authorized_user")
        sizePolicy1.setHeightForWidth(self.authorized_user.sizePolicy().hasHeightForWidth())
        self.authorized_user.setSizePolicy(sizePolicy1)

        self.horizontalLayout_2.addWidget(self.authorized_user)

        self.login_exit = QPushButton(self.widget)
        self.login_exit.setObjectName(u"login_exit")
        sizePolicy1.setHeightForWidth(self.login_exit.sizePolicy().hasHeightForWidth())
        self.login_exit.setSizePolicy(sizePolicy1)

        self.horizontalLayout_2.addWidget(self.login_exit)


        self.horizontalLayout.addWidget(self.widget)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.verticalLayout_4.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, 5, -1, -1)
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout_2.addWidget(self.pushButton)


        self.verticalLayout_4.addLayout(self.verticalLayout_2)

        self.stacked_widget_main = QStackedWidget(self.centralwidget)
        self.stacked_widget_main.setObjectName(u"stacked_widget_main")

        self.verticalLayout_4.addWidget(self.stacked_widget_main)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 747, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.logo_company_main.setText(QCoreApplication.translate("MainWindow", u"\u041b\u043e\u0433\u043e\u0442\u0438\u043f \u041d\u041e\u0412\u0410\u042f \u0412\u0415\u0420\u0421\u0418\u042f", None))
        self.notification_button_main.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0432\u0435\u0434\u043e\u043c\u043b\u0435\u043d\u0438\u044f", None))
        self.icon_profile_main.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043a\u043e\u043d\u043a\u0430", None))
        self.authorized_user.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0432\u0430\u043d\u043e\u0432 \u0418\u0432\u0430\u043d \u0418\u0432\u0430\u043d\u043e\u0432\u0438\u0447", None))
        self.login_exit.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0445\u043e\u0434", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0432\u0435\u0440\u0438\u0442\u044c \u043e\u0431\u043d\u043e\u0432\u043b\u0435\u043d\u0438\u044f", None))
    # retranslateUi


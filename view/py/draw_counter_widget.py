# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'draw_counter_widget.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(542, 531)
        self.verticalLayout_2 = QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 50, -1, -1)

        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, 0, -1, -1)
        self.zoom_plus = QPushButton(Form)
        self.zoom_plus.setObjectName(u"zoom_plus")
        self.zoom_plus.setEnabled(True)

        self.horizontalLayout_3.addWidget(self.zoom_plus)

        self.zoom_minus = QPushButton(Form)
        self.zoom_minus.setObjectName(u"zoom_minus")
        self.zoom_minus.setEnabled(True)

        self.horizontalLayout_3.addWidget(self.zoom_minus)

        self.clear_countor_button = QPushButton(Form)
        self.clear_countor_button.setObjectName(u"clear_countor_button")
        self.clear_countor_button.setEnabled(False)

        self.horizontalLayout_3.addWidget(self.clear_countor_button)

        self.countor_close_button = QPushButton(Form)
        self.countor_close_button.setObjectName(u"countor_close_button")

        self.horizontalLayout_3.addWidget(self.countor_close_button)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.cancel_button = QPushButton(Form)
        self.cancel_button.setObjectName(u"cancel_button")
        self.cancel_button.setEnabled(False)

        self.horizontalLayout.addWidget(self.cancel_button)

        self.save_button = QPushButton(Form)
        self.save_button.setObjectName(u"save_button")

        self.horizontalLayout.addWidget(self.save_button)

        self.select_categorical_disease_button = QPushButton(Form)
        self.select_categorical_disease_button.setObjectName(u"select_categorical_disease_button")

        self.horizontalLayout.addWidget(self.select_categorical_disease_button)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, 10, -1, 10)
        self.area_countor_label = QLabel(Form)
        self.area_countor_label.setObjectName(u"area_countor_label")

        self.verticalLayout_3.addWidget(self.area_countor_label)

        self.type_disease_label = QLabel(Form)
        self.type_disease_label.setObjectName(u"type_disease_label")

        self.verticalLayout_3.addWidget(self.type_disease_label)


        self.verticalLayout_2.addLayout(self.verticalLayout_3)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.zoom_plus.setText(QCoreApplication.translate("Form", u"+", None))
        self.zoom_minus.setText(QCoreApplication.translate("Form", u"-", None))
        self.clear_countor_button.setText(QCoreApplication.translate("Form", u"\u041e\u0447\u0438\u0441\u0442\u0438\u0442\u044c \u043a\u043e\u043d\u0442\u0443\u0440", None))
        self.countor_close_button.setText(QCoreApplication.translate("Form", u"\u0417\u0430\u043c\u043a\u043d\u0443\u0442\u044c \u043a\u043e\u043d\u0442\u0443\u0440", None))
        self.cancel_button.setText(QCoreApplication.translate("Form", u"\u041e\u0442\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.save_button.setText(QCoreApplication.translate("Form", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.select_categorical_disease_button.setText(QCoreApplication.translate("Form", u"\u0423\u043a\u0430\u0437\u0430\u0442\u044c \u0431\u043e\u043b\u0435\u0437\u043d\u044c", None))
        self.area_countor_label.setText(QCoreApplication.translate("Form", u"\u041f\u043b\u043e\u0449\u0430\u0434\u044c \u043a\u043e\u043d\u0442\u0443\u0440\u0430", None))
        self.type_disease_label.setText(QCoreApplication.translate("Form", u"\u0422\u0438\u043f \u0431\u043e\u043b\u0435\u0437\u043d\u0438", None))
    # retranslateUi


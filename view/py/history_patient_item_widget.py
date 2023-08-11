# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'history_patient_item_widget.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(218, 308)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setStyleSheet(u"QWidget#Form{\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"")
        self.verticalLayout_3 = QVBoxLayout(Form)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"QWidget#widget{\n"
"background-color:  rgb(199, 199, 199) ;\n"
"padding: 10px;\n"
"border: solid 2px #1B7530;\n"
"border-radius: 10px;\n"
"}\n"
"")
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.patient_history_item_image = QLabel(self.widget)
        self.patient_history_item_image.setObjectName(u"patient_history_item_image")
        self.patient_history_item_image.setMinimumSize(QSize(180, 180))
        self.patient_history_item_image.setMaximumSize(QSize(180, 180))
        self.patient_history_item_image.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout.addWidget(self.patient_history_item_image)

        self.patient_history_item_date = QLabel(self.widget)
        self.patient_history_item_date.setObjectName(u"patient_history_item_date")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.patient_history_item_date.sizePolicy().hasHeightForWidth())
        self.patient_history_item_date.setSizePolicy(sizePolicy1)
        self.patient_history_item_date.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout.addWidget(self.patient_history_item_date)

        self.patient_history_item_comment = QLabel(self.widget)
        self.patient_history_item_comment.setObjectName(u"patient_history_item_comment")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.patient_history_item_comment.sizePolicy().hasHeightForWidth())
        self.patient_history_item_comment.setSizePolicy(sizePolicy2)
        self.patient_history_item_comment.setStyleSheet(u"background-color: rgb(170, 153, 255);")

        self.verticalLayout.addWidget(self.patient_history_item_comment)

        self.pushButton = QPushButton(self.widget)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout.addWidget(self.pushButton)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.verticalLayout_3.addWidget(self.widget)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.patient_history_item_image.setText(QCoreApplication.translate("Form", u"\u0424\u043e\u0442\u043e ", None))
        self.patient_history_item_date.setText(QCoreApplication.translate("Form", u"\u0414\u0430\u0442\u0430: 22.09.2022", None))
        self.patient_history_item_comment.setText(QCoreApplication.translate("Form", u"\u041a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0439 \u0432\u0440\u0430\u0447\u0430: \u0432\u0441\u0435 \n"
" \u043d\u043e\u0440\u043c", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u041f\u043e\u0434\u0440\u043e\u0431\u043d\u0435\u0435", None))
    # retranslateUi


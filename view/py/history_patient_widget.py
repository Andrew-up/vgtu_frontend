# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'history_patient_widget.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
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
    QScrollArea, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(587, 459)
        self.verticalLayout_3 = QVBoxLayout(Form)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")

        self.verticalLayout_2.addWidget(self.label)

        self.history_patient_fullname_patient = QLabel(Form)
        self.history_patient_fullname_patient.setObjectName(u"history_patient_fullname_patient")

        self.verticalLayout_2.addWidget(self.history_patient_fullname_patient)

        self.history_patient_diagnosis_patient = QLabel(Form)
        self.history_patient_diagnosis_patient.setObjectName(u"history_patient_diagnosis_patient")

        self.verticalLayout_2.addWidget(self.history_patient_diagnosis_patient)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.history_patient_button_prev = QPushButton(Form)
        self.history_patient_button_prev.setObjectName(u"history_patient_button_prev")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.history_patient_button_prev.sizePolicy().hasHeightForWidth())
        self.history_patient_button_prev.setSizePolicy(sizePolicy)
        self.history_patient_button_prev.setIconSize(QSize(16, 16))

        self.horizontalLayout_2.addWidget(self.history_patient_button_prev)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.scrollArea = QScrollArea(Form)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 397, 365))
        self.verticalLayout_5 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer)

        self.history_patient_layout_list_healing = QHBoxLayout()
        self.history_patient_layout_list_healing.setObjectName(u"history_patient_layout_list_healing")
        self.history_patient_layout_list_healing.setContentsMargins(-1, 10, -1, 10)

        self.verticalLayout_5.addLayout(self.history_patient_layout_list_healing)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_2)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_4.addWidget(self.scrollArea)


        self.horizontalLayout_2.addLayout(self.verticalLayout_4)

        self.history_patient_button_next = QPushButton(Form)
        self.history_patient_button_next.setObjectName(u"history_patient_button_next")
        self.history_patient_button_next.setEnabled(True)
        sizePolicy.setHeightForWidth(self.history_patient_button_next.sizePolicy().hasHeightForWidth())
        self.history_patient_button_next.setSizePolicy(sizePolicy)
        self.history_patient_button_next.setAutoFillBackground(False)

        self.horizontalLayout_2.addWidget(self.history_patient_button_next)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)


        self.verticalLayout.addLayout(self.verticalLayout_2)


        self.verticalLayout_3.addLayout(self.verticalLayout)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u0418\u0441\u0442\u043e\u0440\u0438\u044f \u043b\u0435\u0447\u0435\u043d\u0438\u044f", None))
        self.history_patient_fullname_patient.setText(QCoreApplication.translate("Form", u"\u041f\u0435\u0442\u0440\u043e\u0432 \u041f\u0435\u0442\u0440 \u041f\u0435\u0442\u0440\u043e\u0432\u0438\u0447", None))
        self.history_patient_diagnosis_patient.setText(QCoreApplication.translate("Form", u"\u0414\u0438\u0430\u0433\u043d\u043e\u0437: \u043e\u0436\u043e\u0433 3 \u0441\u0442\u0435\u043f\u0435\u043d\u0438", None))
        self.history_patient_button_prev.setText(QCoreApplication.translate("Form", u"<", None))
        self.history_patient_button_next.setText(QCoreApplication.translate("Form", u">", None))
    # retranslateUi


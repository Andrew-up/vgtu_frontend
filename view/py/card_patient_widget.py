# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'card_patient_widget.ui'
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
        Form.resize(478, 652)
        self.verticalLayout_5 = QVBoxLayout(Form)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")

        self.verticalLayout_3.addWidget(self.label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.card_image_patient = QLabel(Form)
        self.card_image_patient.setObjectName(u"card_image_patient")
        self.card_image_patient.setMinimumSize(QSize(70, 100))
        self.card_image_patient.setStyleSheet(u"background-color: rgb(96, 191, 255);")

        self.verticalLayout_2.addWidget(self.card_image_patient)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_3)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.card_fullname_patient = QLabel(Form)
        self.card_fullname_patient.setObjectName(u"card_fullname_patient")

        self.verticalLayout.addWidget(self.card_fullname_patient)

        self.verticalSpacer_2 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.card_gender_patient = QLabel(Form)
        self.card_gender_patient.setObjectName(u"card_gender_patient")

        self.verticalLayout.addWidget(self.card_gender_patient)

        self.card_date_birth_patient = QLabel(Form)
        self.card_date_birth_patient.setObjectName(u"card_date_birth_patient")

        self.verticalLayout.addWidget(self.card_date_birth_patient)

        self.card_age_patient = QLabel(Form)
        self.card_age_patient.setObjectName(u"card_age_patient")

        self.verticalLayout.addWidget(self.card_age_patient)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(-1, 0, -1, -1)
        self.card_address_patient = QLabel(Form)
        self.card_address_patient.setObjectName(u"card_address_patient")

        self.verticalLayout_4.addWidget(self.card_address_patient)

        self.card_phone_patient = QLabel(Form)
        self.card_phone_patient.setObjectName(u"card_phone_patient")

        self.verticalLayout_4.addWidget(self.card_phone_patient)

        self.card_oms_patient = QLabel(Form)
        self.card_oms_patient.setObjectName(u"card_oms_patient")

        self.verticalLayout_4.addWidget(self.card_oms_patient)

        self.card_snils_patient = QLabel(Form)
        self.card_snils_patient.setObjectName(u"card_snils_patient")

        self.verticalLayout_4.addWidget(self.card_snils_patient)

        self.card_document_patient = QLabel(Form)
        self.card_document_patient.setObjectName(u"card_document_patient")

        self.verticalLayout_4.addWidget(self.card_document_patient)

        self.card_diagnosis_patient = QLabel(Form)
        self.card_diagnosis_patient.setObjectName(u"card_diagnosis_patient")

        self.verticalLayout_4.addWidget(self.card_diagnosis_patient)

        self.card_healing_date_start_patient = QLabel(Form)
        self.card_healing_date_start_patient.setObjectName(u"card_healing_date_start_patient")

        self.verticalLayout_4.addWidget(self.card_healing_date_start_patient)

        self.card_healing_date_end_patient = QLabel(Form)
        self.card_healing_date_end_patient.setObjectName(u"card_healing_date_end_patient")

        self.verticalLayout_4.addWidget(self.card_healing_date_end_patient)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_4)

        self.delete_patient_button = QPushButton(Form)
        self.delete_patient_button.setObjectName(u"delete_patient_button")

        self.verticalLayout_4.addWidget(self.delete_patient_button)


        self.verticalLayout_3.addLayout(self.verticalLayout_4)


        self.verticalLayout_5.addLayout(self.verticalLayout_3)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u041a\u0430\u0440\u0442\u0430 \u043f\u0430\u0446\u0438\u0435\u043d\u0442\u0430", None))
        self.card_image_patient.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.card_fullname_patient.setText(QCoreApplication.translate("Form", u"\u041f\u0435\u0442\u0440\u043e\u0432 \u041f\u0435\u0442\u0440 \u041f\u0435\u0442\u0440\u043e\u0432\u0438\u0447", None))
        self.card_gender_patient.setText(QCoreApplication.translate("Form", u"\u041f\u043e\u043b: ", None))
        self.card_date_birth_patient.setText(QCoreApplication.translate("Form", u"\u0414\u0430\u0442\u0430 \u0440\u043e\u0436\u0434\u0435\u043d\u0438: ", None))
        self.card_age_patient.setText(QCoreApplication.translate("Form", u"\u0412\u043e\u0437\u0440\u0430\u0441\u0442: ", None))
        self.card_address_patient.setText(QCoreApplication.translate("Form", u"\u041c\u0435\u0441\u0442\u043e \u0440\u0435\u0433\u0438\u0441\u0442\u0440\u0430\u0446\u0438\u0438: ", None))
        self.card_phone_patient.setText(QCoreApplication.translate("Form", u"\u0422\u0435\u043b\u0435\u0444\u043e\u043d: ", None))
        self.card_oms_patient.setText(QCoreApplication.translate("Form", u"\u041f\u043e\u043b\u0438\u0441 \u041e\u041c\u0421: ", None))
        self.card_snils_patient.setText(QCoreApplication.translate("Form", u"\u0421\u041d\u0418\u041b\u0421: ", None))
        self.card_document_patient.setText(QCoreApplication.translate("Form", u"\u0414\u043e\u043a\u0443\u043c\u0435\u043d\u0442: ", None))
        self.card_diagnosis_patient.setText(QCoreApplication.translate("Form", u"\u0414\u0438\u0430\u0433\u043d\u043e\u0437: ", None))
        self.card_healing_date_start_patient.setText(QCoreApplication.translate("Form", u"\u0414\u0430\u0442\u0430 \u043d\u0430\u0447\u0430\u043b\u0430 \u043b\u0435\u0447\u0435\u043d\u0438\u044f: ", None))
        self.card_healing_date_end_patient.setText(QCoreApplication.translate("Form", u"\u0414\u0430\u0442\u0430 \u043e\u043a\u043e\u043d\u0447\u0430\u043d\u0438\u044f \u043b\u0435\u0447\u0435\u043d\u0438\u044f:", None))
        self.delete_patient_button.setText(QCoreApplication.translate("Form", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u043f\u0430\u0446\u0438\u0435\u043d\u0442\u0430", None))
    # retranslateUi


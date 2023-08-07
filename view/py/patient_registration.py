# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'patient_registration.ui'
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
from PySide6.QtWidgets import (QApplication, QDateEdit, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(529, 580)
        self.verticalLayout_2 = QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.firstname_patient = QLineEdit(Form)
        self.firstname_patient.setObjectName(u"firstname_patient")

        self.verticalLayout.addWidget(self.firstname_patient)

        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.lastname_patient = QLineEdit(Form)
        self.lastname_patient.setObjectName(u"lastname_patient")

        self.verticalLayout.addWidget(self.lastname_patient)

        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout.addWidget(self.label_3)

        self.middle_name_patient = QLineEdit(Form)
        self.middle_name_patient.setObjectName(u"middle_name_patient")

        self.verticalLayout.addWidget(self.middle_name_patient)

        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout.addWidget(self.label_4)

        self.date_of_birth_patient = QDateEdit(Form)
        self.date_of_birth_patient.setObjectName(u"date_of_birth_patient")

        self.verticalLayout.addWidget(self.date_of_birth_patient)

        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout.addWidget(self.label_5)

        self.address_patient = QLineEdit(Form)
        self.address_patient.setObjectName(u"address_patient")

        self.verticalLayout.addWidget(self.address_patient)

        self.label_6 = QLabel(Form)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout.addWidget(self.label_6)

        self.phone_patient = QLineEdit(Form)
        self.phone_patient.setObjectName(u"phone_patient")

        self.verticalLayout.addWidget(self.phone_patient)

        self.label_7 = QLabel(Form)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout.addWidget(self.label_7)

        self.polis_oms_patient = QLineEdit(Form)
        self.polis_oms_patient.setObjectName(u"polis_oms_patient")

        self.verticalLayout.addWidget(self.polis_oms_patient)

        self.label_8 = QLabel(Form)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout.addWidget(self.label_8)

        self.snils_patient = QLineEdit(Form)
        self.snils_patient.setObjectName(u"snils_patient")

        self.verticalLayout.addWidget(self.snils_patient)

        self.label_9 = QLabel(Form)
        self.label_9.setObjectName(u"label_9")

        self.verticalLayout.addWidget(self.label_9)

        self.document_patient = QLineEdit(Form)
        self.document_patient.setObjectName(u"document_patient")

        self.verticalLayout.addWidget(self.document_patient)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(10, 10, 10, 10)
        self.clear_all_button = QPushButton(Form)
        self.clear_all_button.setObjectName(u"clear_all_button")

        self.horizontalLayout_2.addWidget(self.clear_all_button)

        self.get_random_patient_button = QPushButton(Form)
        self.get_random_patient_button.setObjectName(u"get_random_patient_button")

        self.horizontalLayout_2.addWidget(self.get_random_patient_button)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.registration_button = QPushButton(Form)
        self.registration_button.setObjectName(u"registration_button")

        self.verticalLayout.addWidget(self.registration_button)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u0418\u043c\u044f", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u0424\u0430\u043c\u0438\u043b\u0438\u044f", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u041e\u0442\u0447\u0435\u0441\u0442\u0432\u043e", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"\u0414\u0430\u0442\u0430 \u0440\u043e\u0436\u0434\u0435\u043d\u0438\u044f", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"\u0410\u0434\u0440\u0435\u0441", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"\u0422\u0435\u043b\u0435\u0444\u043e\u043d", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"\u041f\u043e\u043b\u0438\u0441 \u041e\u041c\u0421", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"\u0421\u041d\u0418\u041b\u0421", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"\u0414\u043e\u043a\u0443\u043c\u0435\u043d\u0442", None))
        self.clear_all_button.setText(QCoreApplication.translate("Form", u"\u041e\u0447\u0438\u0441\u0442\u0438\u0442\u044c \u0432\u0441\u0451", None))
        self.get_random_patient_button.setText(QCoreApplication.translate("Form", u"\u0421\u043b\u0443\u0447\u0430\u0439\u043d\u044b\u0439 \u043f\u0430\u0446\u0438\u0435\u043d\u0442", None))
        self.registration_button.setText(QCoreApplication.translate("Form", u"\u0420\u0435\u0433\u0438\u0441\u0442\u0440\u0430\u0446\u0438\u044f", None))
    # retranslateUi


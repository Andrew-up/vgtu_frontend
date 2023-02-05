# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'patient_table_item.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(263, 44)
        self.verticalLayout_3 = QVBoxLayout(Form)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.patient_table_item_fullname = QPushButton(Form)
        self.patient_table_item_fullname.setObjectName(u"patient_table_item_fullname")

        self.horizontalLayout.addWidget(self.patient_table_item_fullname)

        self.patient_table_item_snils = QPushButton(Form)
        self.patient_table_item_snils.setObjectName(u"patient_table_item_snils")

        self.horizontalLayout.addWidget(self.patient_table_item_snils)


        self.verticalLayout_3.addLayout(self.horizontalLayout)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.patient_table_item_fullname.setText(QCoreApplication.translate("Form", u"\u0424\u0418\u041e", None))
        self.patient_table_item_snils.setText(QCoreApplication.translate("Form", u"\u0421\u041d\u0418\u041b\u0421", None))
    # retranslateUi


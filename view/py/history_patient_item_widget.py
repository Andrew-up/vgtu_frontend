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
from PySide6.QtWidgets import (QApplication, QLabel, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(200, 237)
        self.verticalLayout_2 = QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.patient_history_item_image = QLabel(Form)
        self.patient_history_item_image.setObjectName(u"patient_history_item_image")
        self.patient_history_item_image.setMinimumSize(QSize(70, 70))

        self.verticalLayout.addWidget(self.patient_history_item_image)

        self.patient_history_item_date = QLabel(Form)
        self.patient_history_item_date.setObjectName(u"patient_history_item_date")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.patient_history_item_date.sizePolicy().hasHeightForWidth())
        self.patient_history_item_date.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.patient_history_item_date)

        self.patient_history_item_comment = QLabel(Form)
        self.patient_history_item_comment.setObjectName(u"patient_history_item_comment")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.patient_history_item_comment.sizePolicy().hasHeightForWidth())
        self.patient_history_item_comment.setSizePolicy(sizePolicy1)

        self.verticalLayout.addWidget(self.patient_history_item_comment)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.patient_history_item_image.setText(QCoreApplication.translate("Form", u"\u0424\u043e\u0442\u043e ", None))
        self.patient_history_item_date.setText(QCoreApplication.translate("Form", u"\u0414\u0430\u0442\u0430: 22.09.2022", None))
        self.patient_history_item_comment.setText(QCoreApplication.translate("Form", u"\u041a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0439 \u0432\u0440\u0430\u0447\u0430: \u0432\u0441\u0435 \n"
" \u043d\u043e\u0440\u043c", None))
    # retranslateUi


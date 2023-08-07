# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'view_patient_widget.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QPushButton,
    QSizePolicy, QSpacerItem, QStackedWidget, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(430, 387)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.verticalLayout_4 = QVBoxLayout(Form)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.view_patient_go_mainmenu = QPushButton(Form)
        self.view_patient_go_mainmenu.setObjectName(u"view_patient_go_mainmenu")

        self.verticalLayout_2.addWidget(self.view_patient_go_mainmenu)

        self.view_patient_go_card_patient = QPushButton(Form)
        self.view_patient_go_card_patient.setObjectName(u"view_patient_go_card_patient")

        self.verticalLayout_2.addWidget(self.view_patient_go_card_patient)

        self.line_2 = QFrame(Form)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.line_2)

        self.view_patient_go_history_healing = QPushButton(Form)
        self.view_patient_go_history_healing.setObjectName(u"view_patient_go_history_healing")

        self.verticalLayout_2.addWidget(self.view_patient_go_history_healing)

        self.line = QFrame(Form)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.line)

        self.view_patient_go_wound_treatment = QPushButton(Form)
        self.view_patient_go_wound_treatment.setObjectName(u"view_patient_go_wound_treatment")

        self.verticalLayout_2.addWidget(self.view_patient_go_wound_treatment)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.stacked_widget_view_patient = QStackedWidget(Form)
        self.stacked_widget_view_patient.setObjectName(u"stacked_widget_view_patient")
        sizePolicy.setHeightForWidth(self.stacked_widget_view_patient.sizePolicy().hasHeightForWidth())
        self.stacked_widget_view_patient.setSizePolicy(sizePolicy)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.stacked_widget_view_patient.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.stacked_widget_view_patient.addWidget(self.page_2)

        self.horizontalLayout.addWidget(self.stacked_widget_view_patient)


        self.verticalLayout_4.addLayout(self.horizontalLayout)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.view_patient_go_mainmenu.setText(QCoreApplication.translate("Form", u"\u0412\u0435\u0440\u043d\u0443\u0442\u044c\u0441\u044f \u043a \u0441\u043f\u0438\u0441\u043a\u0443", None))
        self.view_patient_go_card_patient.setText(QCoreApplication.translate("Form", u"\u041a\u0430\u0440\u0442\u0430 \u043f\u0430\u0446\u0438\u0435\u043d\u0442\u0430", None))
        self.view_patient_go_history_healing.setText(QCoreApplication.translate("Form", u"\u0418\u0441\u0442\u043e\u0440\u0438\u044f \u043b\u0435\u0447\u0435\u043d\u0438\u044f", None))
        self.view_patient_go_wound_treatment.setText(QCoreApplication.translate("Form", u"\u041e\u0431\u0440\u0430\u0431\u043e\u0442\u043a\u0430 \u0440\u0430\u043d\u044b", None))
    # retranslateUi


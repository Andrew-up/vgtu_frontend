# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'list_patient_widget.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLayout,
    QLineEdit, QPushButton, QScrollArea, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(312, 453)
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_2.addWidget(self.label_2)

        self.widget_2 = QWidget(Form)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMinimumSize(QSize(0, 50))
        self.verticalLayout_6 = QVBoxLayout(self.widget_2)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, 10, -1, 10)
        self.pushButton_6 = QPushButton(self.widget_2)
        self.pushButton_6.setObjectName(u"pushButton_6")

        self.horizontalLayout_3.addWidget(self.pushButton_6)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_4)

        self.pushButton_7 = QPushButton(self.widget_2)
        self.pushButton_7.setObjectName(u"pushButton_7")

        self.horizontalLayout_3.addWidget(self.pushButton_7)


        self.verticalLayout_6.addLayout(self.horizontalLayout_3)


        self.verticalLayout_2.addWidget(self.widget_2)

        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setEnabled(True)
        self.widget.setMinimumSize(QSize(0, 0))
        self.verticalLayout_5 = QVBoxLayout(self.widget)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(1, 1, 1, 1)
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(-1, 10, -1, 10)
        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)

        self.horizontalLayout_5.addWidget(self.label_3)

        self.lineEdit = QLineEdit(self.widget)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout_5.addWidget(self.lineEdit)


        self.verticalLayout_5.addLayout(self.horizontalLayout_5)


        self.verticalLayout_2.addWidget(self.widget)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_6.setContentsMargins(-1, 10, -1, 10)
        self.pushButton_8 = QPushButton(Form)
        self.pushButton_8.setObjectName(u"pushButton_8")

        self.horizontalLayout_6.addWidget(self.pushButton_8)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer)

        self.update_patients = QPushButton(Form)
        self.update_patients.setObjectName(u"update_patients")

        self.horizontalLayout_6.addWidget(self.update_patients)


        self.verticalLayout_2.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, 10, -1, -1)
        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_4)

        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.ListPatientTableLayout = QVBoxLayout()
        self.ListPatientTableLayout.setObjectName(u"ListPatientTableLayout")
        self.ListPatientTableLayout.setContentsMargins(-1, 5, -1, 5)
        self.scrollArea = QScrollArea(Form)
        self.scrollArea.setObjectName(u"scrollArea")
        sizePolicy1 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy1)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 286, 196))
        self.verticalLayout_3 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")

        self.verticalLayout_3.addLayout(self.verticalLayout_4)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.ListPatientTableLayout.addWidget(self.scrollArea)


        self.verticalLayout_2.addLayout(self.ListPatientTableLayout)


        self.verticalLayout.addLayout(self.verticalLayout_2)


        self.horizontalLayout.addLayout(self.verticalLayout)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u0421\u043f\u0438\u0441\u043e\u043a \u043f\u0430\u0446\u0438\u0435\u043d\u0442\u043e\u0432", None))
        self.pushButton_6.setText(QCoreApplication.translate("Form", u"\u0421\u043e\u0440\u0442\u0438\u0440\u043e\u0432\u043a\u0430", None))
        self.pushButton_7.setText(QCoreApplication.translate("Form", u"\u0424\u0438\u043b\u044c\u0442\u0440\u0430\u0446\u0438\u044f", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u041b\u0443\u043f\u04301", None))
        self.pushButton_8.setText(QCoreApplication.translate("Form", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u043f\u0430\u0446\u0438\u0435\u043d\u0442\u0430", None))
        self.update_patients.setText(QCoreApplication.translate("Form", u"\u041e\u0431\u043d\u043e\u0432\u0438\u0442\u044c \u0441\u043f\u0438\u0441\u043e\u043a", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"\u0424\u0418\u041e", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u0421\u041d\u0418\u041b\u0421", None))
    # retranslateUi


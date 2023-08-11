# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'more_info_model_cnn.ui'
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
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(542, 356)
        self.verticalLayout_2 = QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)

        self.date_training = QLabel(Form)
        self.date_training.setObjectName(u"date_training")

        self.horizontalLayout_2.addWidget(self.date_training)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_3.addWidget(self.label_3)

        self.status_training = QLabel(Form)
        self.status_training.setObjectName(u"status_training")

        self.horizontalLayout_3.addWidget(self.status_training)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_4.addWidget(self.label_4)

        self.version_model = QLabel(Form)
        self.version_model.setObjectName(u"version_model")

        self.horizontalLayout_4.addWidget(self.version_model)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_6 = QLabel(Form)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_5.addWidget(self.label_6)

        self.time_training_model = QLabel(Form)
        self.time_training_model.setObjectName(u"time_training_model")

        self.horizontalLayout_5.addWidget(self.time_training_model)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_8.addWidget(self.label_2)

        self.total_epoch = QLabel(Form)
        self.total_epoch.setObjectName(u"total_epoch")

        self.horizontalLayout_8.addWidget(self.total_epoch)


        self.verticalLayout.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_7 = QLabel(Form)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_9.addWidget(self.label_7)

        self.current_epoch = QLabel(Form)
        self.current_epoch.setObjectName(u"current_epoch")

        self.horizontalLayout_9.addWidget(self.current_epoch)


        self.verticalLayout.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout_6.addWidget(self.pushButton)


        self.verticalLayout.addLayout(self.horizontalLayout_6)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u0414\u0430\u0442\u0430 \u043e\u0431\u0443\u0447\u0435\u043d\u0438\u044f", None))
        self.date_training.setText(QCoreApplication.translate("Form", u"date_training", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u0421\u0442\u0430\u0442\u0443\u0441 \u043e\u0431\u0443\u0447\u0435\u043d\u0438\u044f", None))
        self.status_training.setText(QCoreApplication.translate("Form", u"status_training", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"\u0412\u0435\u0440\u0441\u0438\u044f \u043c\u043e\u0434\u0435\u043b\u0438", None))
        self.version_model.setText(QCoreApplication.translate("Form", u"version_model", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"\u0412\u0440\u0435\u043c\u044f \u043e\u0431\u0443\u0447\u0435\u043d\u0438\u044f", None))
        self.time_training_model.setText(QCoreApplication.translate("Form", u"time_training_model", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u041a\u043e\u043b-\u0432\u043e \u044d\u043f\u043e\u0445 \u043e\u0431\u0443\u0447\u0435\u043d\u0438\u044f", None))
        self.total_epoch.setText(QCoreApplication.translate("Form", u"total_epoch", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"\u0422\u0435\u043a\u0443\u0449\u0430\u044f \u044d\u043f\u043e\u0445\u0430 \u043e\u0431\u0443\u0447\u0435\u043d\u0438\u044f", None))
        self.current_epoch.setText(QCoreApplication.translate("Form", u"current_epoch", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u0417\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c \u043c\u043e\u0434\u0435\u043b\u044c", None))
    # retranslateUi


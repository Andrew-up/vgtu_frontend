# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Retraining_model.ui'
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
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(640, 321)
        self.horizontalLayout_7 = QHBoxLayout(Form)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")

        self.horizontalLayout_4.addWidget(self.label)

        self.total_category_label = QLabel(self.widget)
        self.total_category_label.setObjectName(u"total_category_label")

        self.horizontalLayout_4.addWidget(self.total_category_label)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_5.addWidget(self.label_4)

        self.total_images_label = QLabel(self.widget)
        self.total_images_label.setObjectName(u"total_images_label")

        self.horizontalLayout_5.addWidget(self.total_images_label)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_6.addWidget(self.label_5)

        self.total_annotation_label = QLabel(self.widget)
        self.total_annotation_label.setObjectName(u"total_annotation_label")

        self.horizontalLayout_6.addWidget(self.total_annotation_label)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.pushButton = QPushButton(self.widget)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout.addWidget(self.pushButton)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.verticalLayout_4.addWidget(self.widget)

        self.model_training_false = QWidget(Form)
        self.model_training_false.setObjectName(u"model_training_false")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.model_training_false.sizePolicy().hasHeightForWidth())
        self.model_training_false.setSizePolicy(sizePolicy)
        self.verticalLayout_3 = QVBoxLayout(self.model_training_false)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_2 = QLabel(self.model_training_false)
        self.label_2.setObjectName(u"label_2")
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)

        self.verticalLayout_3.addWidget(self.label_2)


        self.verticalLayout_4.addWidget(self.model_training_false)


        self.horizontalLayout_7.addLayout(self.verticalLayout_4)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u041a\u043e\u043b-\u0432\u043e \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0439 \u0434\u043b\u044f \u043e\u0431\u0443\u0447\u0435\u043d\u0438\u044f:", None))
        self.total_category_label.setText(QCoreApplication.translate("Form", u"total_category_label", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"\u041a\u043e\u043b-\u0432\u043e \u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0439", None))
        self.total_images_label.setText(QCoreApplication.translate("Form", u"total_images_label", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"\u041d\u0430\u0439\u0434\u0435\u043d\u043e \u0430\u043d\u043d\u043e\u0442\u0430\u0446\u0438\u0439", None))
        self.total_annotation_label.setText(QCoreApplication.translate("Form", u"total_annotation_label", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u041e\u0431\u0443\u0447\u0438\u0442\u044c", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u041c\u043e\u0434\u0435\u043b\u044c \u0443\u0436\u0435 \u043e\u0431\u0443\u0447\u0430\u0435\u0442\u0441\u044f, \u043f\u043e\u0434\u043e\u0436\u0434\u0438\u0442\u0435", None))
    # retranslateUi


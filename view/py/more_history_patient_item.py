# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'more_history_patient_item.ui'
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
        Form.resize(781, 460)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.image_original = QLabel(Form)
        self.image_original.setObjectName(u"image_original")
        self.image_original.setMinimumSize(QSize(128, 128))
        self.image_original.setMaximumSize(QSize(256, 256))
        self.image_original.setStyleSheet(u"background-color: rgb(0, 255, 0);")

        self.horizontalLayout.addWidget(self.image_original)

        self.image_predict = QLabel(Form)
        self.image_predict.setObjectName(u"image_predict")
        self.image_predict.setMinimumSize(QSize(128, 128))
        self.image_predict.setMaximumSize(QSize(256, 256))
        self.image_predict.setStyleSheet(u"background-color: rgb(0, 255, 127);")

        self.horizontalLayout.addWidget(self.image_predict)

        self.image_predict_edit_doctor = QLabel(Form)
        self.image_predict_edit_doctor.setObjectName(u"image_predict_edit_doctor")
        self.image_predict_edit_doctor.setMinimumSize(QSize(128, 128))
        self.image_predict_edit_doctor.setMaximumSize(QSize(256, 256))
        self.image_predict_edit_doctor.setStyleSheet(u"background-color: rgb(0, 255, 127);")

        self.horizontalLayout.addWidget(self.image_predict_edit_doctor)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, 0, -1, -1)
        self.label_6 = QLabel(Form)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_3.addWidget(self.label_6)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_3.addWidget(self.label_4)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_4)

        self.label_7 = QLabel(Form)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_3.addWidget(self.label_7)


        self.horizontalLayout_2.addLayout(self.horizontalLayout_3)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)

        self.verticalLayout_2.addWidget(self.label)

        self.label_comment = QLabel(Form)
        self.label_comment.setObjectName(u"label_comment")

        self.verticalLayout_2.addWidget(self.label_comment)

        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)

        self.verticalLayout_2.addWidget(self.label_3)

        self.label_dianosis = QLabel(Form)
        self.label_dianosis.setObjectName(u"label_dianosis")

        self.verticalLayout_2.addWidget(self.label_dianosis)

        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)

        self.verticalLayout_2.addWidget(self.label_5)

        self.label_polygon = QLabel(Form)
        self.label_polygon.setObjectName(u"label_polygon")

        self.verticalLayout_2.addWidget(self.label_polygon)

        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)

        self.verticalLayout_2.addWidget(self.label_2)

        self.label_date = QLabel(Form)
        self.label_date.setObjectName(u"label_date")

        self.verticalLayout_2.addWidget(self.label_date)

        self.label_8 = QLabel(Form)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout_2.addWidget(self.label_8)

        self.area_label = QLabel(Form)
        self.area_label.setObjectName(u"area_label")

        self.verticalLayout_2.addWidget(self.area_label)


        self.verticalLayout.addLayout(self.verticalLayout_2)

        self.button_close = QPushButton(Form)
        self.button_close.setObjectName(u"button_close")

        self.verticalLayout.addWidget(self.button_close)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.image_original.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.image_predict.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.image_predict_edit_doctor.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"\u041e\u0440\u0438\u0433\u0438\u043d\u0430\u043b\u044c\u043d\u043e\u0435 \u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"\u0420\u0430\u0441\u043f\u043e\u0437\u043d\u0430\u043d\u043d\u043e\u0435 \u043d\u0435\u0439\u0440\u043e\u043d\u043d\u043e\u0439 \u0441\u0435\u0442\u044c\u044e", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"\u0418\u0437\u043c\u0435\u043d\u0435\u043d\u043e \u0434\u043e\u043a\u0442\u043e\u0440\u043e\u043c", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u041a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0439:", None))
        self.label_comment.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u0414\u0438\u0430\u0433\u043d\u043e\u0437:", None))
        self.label_dianosis.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"\u041f\u043e\u043b\u0438\u0433\u043e\u043d:", None))
        self.label_polygon.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u0414\u0430\u0442\u0430:", None))
        self.label_date.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"\u041f\u043b\u043e\u0449\u0430\u0434\u044c:", None))
        self.area_label.setText(QCoreApplication.translate("Form", u"area_label", None))
        self.button_close.setText(QCoreApplication.translate("Form", u"\u0417\u0430\u043a\u0440\u044b\u0442\u044c", None))
    # retranslateUi


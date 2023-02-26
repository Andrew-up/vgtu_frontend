# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'wound_healing_widget.ui'
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
from PySide6.QtWidgets import (QApplication, QGroupBox, QHBoxLayout, QLabel,
    QLayout, QPushButton, QRadioButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(820, 687)
        self.verticalLayout_4 = QVBoxLayout(Form)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")

        self.verticalLayout_6.addWidget(self.label)

        self.wound_healing_fullname_client = QLabel(Form)
        self.wound_healing_fullname_client.setObjectName(u"wound_healing_fullname_client")

        self.verticalLayout_6.addWidget(self.wound_healing_fullname_client)

        self.wound_healing_diagnosis_client = QLabel(Form)
        self.wound_healing_diagnosis_client.setObjectName(u"wound_healing_diagnosis_client")

        self.verticalLayout_6.addWidget(self.wound_healing_diagnosis_client)


        self.verticalLayout_4.addLayout(self.verticalLayout_6)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, 5, -1, 5)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, 5, -1, 5)
        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_7 = QVBoxLayout(self.groupBox)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.radio_scan_to_cam = QRadioButton(self.groupBox)
        self.radio_scan_to_cam.setObjectName(u"radio_scan_to_cam")

        self.verticalLayout_7.addWidget(self.radio_scan_to_cam)

        self.radio_scan_to_photo_catalog = QRadioButton(self.groupBox)
        self.radio_scan_to_photo_catalog.setObjectName(u"radio_scan_to_photo_catalog")

        self.verticalLayout_7.addWidget(self.radio_scan_to_photo_catalog)

        self.button_select_ptoho_from_catalog = QPushButton(self.groupBox)
        self.button_select_ptoho_from_catalog.setObjectName(u"button_select_ptoho_from_catalog")

        self.verticalLayout_7.addWidget(self.button_select_ptoho_from_catalog)


        self.verticalLayout_3.addWidget(self.groupBox)

        self.file_name_select_folder = QLabel(Form)
        self.file_name_select_folder.setObjectName(u"file_name_select_folder")

        self.verticalLayout_3.addWidget(self.file_name_select_folder)

        self.wound_healing_start_scan = QPushButton(Form)
        self.wound_healing_start_scan.setObjectName(u"wound_healing_start_scan")

        self.verticalLayout_3.addWidget(self.wound_healing_start_scan)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(-1, 10, -1, 10)
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)

        self.wound_healing_loading_label = QLabel(Form)
        self.wound_healing_loading_label.setObjectName(u"wound_healing_loading_label")

        self.horizontalLayout_4.addWidget(self.wound_healing_loading_label)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_4)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)


        self.horizontalLayout_3.addLayout(self.verticalLayout_3)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)


        self.verticalLayout_4.addLayout(self.horizontalLayout_3)

        self.wound_healing_widget = QWidget(Form)
        self.wound_healing_widget.setObjectName(u"wound_healing_widget")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.wound_healing_widget.sizePolicy().hasHeightForWidth())
        self.wound_healing_widget.setSizePolicy(sizePolicy)
        self.wound_healing_widget.setMinimumSize(QSize(0, 300))
        self.verticalLayout_5 = QVBoxLayout(self.wound_healing_widget)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_5 = QLabel(self.wound_healing_widget)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout.addWidget(self.label_5)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_6 = QSpacerItem(10, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_6)

        self.wound_healing_image = QLabel(self.wound_healing_widget)
        self.wound_healing_image.setObjectName(u"wound_healing_image")
        self.wound_healing_image.setMinimumSize(QSize(250, 250))
        self.wound_healing_image.setMaximumSize(QSize(250, 250))
        self.wound_healing_image.setStyleSheet(u"background-color: rgb(19, 255, 220);")

        self.horizontalLayout.addWidget(self.wound_healing_image)

        self.horizontalSpacer_5 = QSpacerItem(10, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_5)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout_2.setContentsMargins(-1, -1, -1, 0)
        self.widget_2 = QWidget(self.wound_healing_widget)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy1)
        self.widget_2.setMinimumSize(QSize(0, 100))
        self.widget_2.setStyleSheet(u"")
        self.verticalLayout_10 = QVBoxLayout(self.widget_2)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.wound_healing_area_wound = QLabel(self.widget_2)
        self.wound_healing_area_wound.setObjectName(u"wound_healing_area_wound")

        self.verticalLayout_10.addWidget(self.wound_healing_area_wound)

        self.wound_healing_type_wound = QLabel(self.widget_2)
        self.wound_healing_type_wound.setObjectName(u"wound_healing_type_wound")

        self.verticalLayout_10.addWidget(self.wound_healing_type_wound)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_10.addItem(self.verticalSpacer)

        self.wound_healing_layout_result = QVBoxLayout()
        self.wound_healing_layout_result.setObjectName(u"wound_healing_layout_result")
        self.wound_healing_layout_result.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.wound_healing_layout_result.setContentsMargins(-1, 0, -1, -1)
        self.wound_healing_result_is_ok = QLabel(self.widget_2)
        self.wound_healing_result_is_ok.setObjectName(u"wound_healing_result_is_ok")

        self.wound_healing_layout_result.addWidget(self.wound_healing_result_is_ok)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_9)

        self.wound_healing_button_result_yes = QPushButton(self.widget_2)
        self.wound_healing_button_result_yes.setObjectName(u"wound_healing_button_result_yes")
        sizePolicy2 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.wound_healing_button_result_yes.sizePolicy().hasHeightForWidth())
        self.wound_healing_button_result_yes.setSizePolicy(sizePolicy2)
        self.wound_healing_button_result_yes.setMinimumSize(QSize(0, 25))

        self.horizontalLayout_2.addWidget(self.wound_healing_button_result_yes)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_7)

        self.wound_healing_button_result_no = QPushButton(self.widget_2)
        self.wound_healing_button_result_no.setObjectName(u"wound_healing_button_result_no")
        sizePolicy2.setHeightForWidth(self.wound_healing_button_result_no.sizePolicy().hasHeightForWidth())
        self.wound_healing_button_result_no.setSizePolicy(sizePolicy2)
        self.wound_healing_button_result_no.setMinimumSize(QSize(0, 25))
        self.wound_healing_button_result_no.setAutoDefault(False)

        self.horizontalLayout_2.addWidget(self.wound_healing_button_result_no)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_8)


        self.wound_healing_layout_result.addLayout(self.horizontalLayout_2)


        self.verticalLayout_10.addLayout(self.wound_healing_layout_result)

        self.label_9 = QLabel(self.widget_2)
        self.label_9.setObjectName(u"label_9")

        self.verticalLayout_10.addWidget(self.label_9)


        self.verticalLayout_2.addWidget(self.widget_2)

        self.widget = QWidget(self.wound_healing_widget)
        self.widget.setObjectName(u"widget")
        sizePolicy1.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy1)
        self.widget.setMinimumSize(QSize(100, 100))
        self.verticalLayout_8 = QVBoxLayout(self.widget)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setSizeConstraint(QLayout.SetMinimumSize)
        self.wound_healing_layout_strategy = QVBoxLayout()
        self.wound_healing_layout_strategy.setObjectName(u"wound_healing_layout_strategy")
        self.wound_healing_layout_strategy.setContentsMargins(-1, 0, -1, -1)
        self.wound_healing_strategy_healing = QLabel(self.widget)
        self.wound_healing_strategy_healing.setObjectName(u"wound_healing_strategy_healing")

        self.wound_healing_layout_strategy.addWidget(self.wound_healing_strategy_healing)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(-1, 0, -1, -1)
        self.wound_healing_strategy_button_go = QPushButton(self.widget)
        self.wound_healing_strategy_button_go.setObjectName(u"wound_healing_strategy_button_go")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.wound_healing_strategy_button_go.sizePolicy().hasHeightForWidth())
        self.wound_healing_strategy_button_go.setSizePolicy(sizePolicy3)

        self.horizontalLayout_5.addWidget(self.wound_healing_strategy_button_go)

        self.wound_healing_strategy_button_select_list = QPushButton(self.widget)
        self.wound_healing_strategy_button_select_list.setObjectName(u"wound_healing_strategy_button_select_list")
        sizePolicy3.setHeightForWidth(self.wound_healing_strategy_button_select_list.sizePolicy().hasHeightForWidth())
        self.wound_healing_strategy_button_select_list.setSizePolicy(sizePolicy3)

        self.horizontalLayout_5.addWidget(self.wound_healing_strategy_button_select_list)


        self.wound_healing_layout_strategy.addLayout(self.horizontalLayout_5)


        self.verticalLayout_8.addLayout(self.wound_healing_layout_strategy)

        self.wound_healing_layout_process = QVBoxLayout()
        self.wound_healing_layout_process.setObjectName(u"wound_healing_layout_process")
        self.wound_healing_layout_process.setContentsMargins(-1, 5, -1, -1)
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(-1, 5, -1, 5)
        self.label_12 = QLabel(self.widget)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_6.addWidget(self.label_12)

        self.wound_healing_STOP_robot = QPushButton(self.widget)
        self.wound_healing_STOP_robot.setObjectName(u"wound_healing_STOP_robot")
        sizePolicy3.setHeightForWidth(self.wound_healing_STOP_robot.sizePolicy().hasHeightForWidth())
        self.wound_healing_STOP_robot.setSizePolicy(sizePolicy3)
        self.wound_healing_STOP_robot.setMinimumSize(QSize(0, 0))

        self.horizontalLayout_6.addWidget(self.wound_healing_STOP_robot)


        self.wound_healing_layout_process.addLayout(self.horizontalLayout_6)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(-1, 0, -1, -1)
        self.wound_healing_status_end_process = QLabel(self.widget)
        self.wound_healing_status_end_process.setObjectName(u"wound_healing_status_end_process")

        self.verticalLayout_9.addWidget(self.wound_healing_status_end_process)


        self.wound_healing_layout_process.addLayout(self.verticalLayout_9)


        self.verticalLayout_8.addLayout(self.wound_healing_layout_process)


        self.verticalLayout_2.addWidget(self.widget)


        self.horizontalLayout.addLayout(self.verticalLayout_2)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.verticalLayout_5.addLayout(self.verticalLayout)


        self.verticalLayout_4.addWidget(self.wound_healing_widget)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u041e\u0431\u0440\u0430\u0431\u043e\u0442\u043a\u0430 \u0440\u0430\u043d\u044b", None))
        self.wound_healing_fullname_client.setText(QCoreApplication.translate("Form", u"\u041f\u0435\u0442\u0440\u043e\u0432 \u041f\u0435\u0442\u0440 \u041f\u0435\u0442\u0440\u043e\u0432\u0438\u0447", None))
        self.wound_healing_diagnosis_client.setText(QCoreApplication.translate("Form", u"\u0414\u0438\u0430\u0433\u043d\u043e\u0437: \u043e\u0436\u043e\u0433 3 \u0441\u0442\u0435\u043f\u0435\u043d\u0438", None))
        self.groupBox.setTitle("")
        self.radio_scan_to_cam.setText(QCoreApplication.translate("Form", u"\u0421\u043a\u0430\u043d\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435 \u0441 \u043a\u0430\u043c\u0435\u0440\u044b", None))
        self.radio_scan_to_photo_catalog.setText(QCoreApplication.translate("Form", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c \u043a\u0430\u0440\u0442\u0438\u043d\u043a\u0443", None))
        self.button_select_ptoho_from_catalog.setText(QCoreApplication.translate("Form", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c \u0444\u043e\u0442\u043e \u0434\u043b\u044f \u0441\u043a\u0430\u043d\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u044f", None))
        self.file_name_select_folder.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.wound_healing_start_scan.setText(QCoreApplication.translate("Form", u"\u041d\u0430\u0447\u0430\u0442\u044c \u0441\u043a\u0430\u043d\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435", None))
        self.wound_healing_loading_label.setText(QCoreApplication.translate("Form", u"\u0417\u0430\u0433\u0440\u0443\u0437\u043a\u0430...", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"\u041e\u0431\u0440\u0430\u0431\u043e\u0442\u043a\u0430 \u0440\u0430\u043d\u044b", None))
        self.wound_healing_image.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.wound_healing_area_wound.setText(QCoreApplication.translate("Form", u"\u041f\u043b\u043e\u0449\u0430\u0434\u044c: 5 \u043a\u0432 \u0441\u043c", None))
        self.wound_healing_type_wound.setText(QCoreApplication.translate("Form", u"\u0422\u0438\u043f \u0440\u0430\u043d\u044b: \u0433\u043d\u043e\u0439\u043d\u0430\u044f", None))
        self.wound_healing_result_is_ok.setText(QCoreApplication.translate("Form", u"\u0420\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442 \u043a\u043e\u0440\u0440\u0435\u043a\u0442\u0435\u043d? ", None))
        self.wound_healing_button_result_yes.setText(QCoreApplication.translate("Form", u"\u0414\u0430", None))
        self.wound_healing_button_result_no.setText(QCoreApplication.translate("Form", u"\u041d\u0435\u0442", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"\u041a\u043e\u043d\u0442\u0443\u0440 \u0440\u0430\u043d\u044b \u043e\u043f\u0440\u0435\u0434\u0435\u043b\u0435\u043d", None))
        self.wound_healing_strategy_healing.setText(QCoreApplication.translate("Form", u"\u0421\u0442\u0440\u0430\u0442\u0435\u0433\u0438\u044f \u043b\u0435\u0447\u0435\u043d\u0438\u044f: \u043d\u0430\u043d\u0435\u0441\u0442\u0438 2 \u043c\u043b \u043b\u0435\u043a\u0430\u0440\u0441\u0442\u0432\u0430", None))
        self.wound_healing_strategy_button_go.setText(QCoreApplication.translate("Form", u"\u041e\u0431\u0440\u0430\u0431\u043e\u0442\u0430\u0442\u044c", None))
        self.wound_healing_strategy_button_select_list.setText(QCoreApplication.translate("Form", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c \u0432\u0440\u0443\u0447\u043d\u0443\u044e", None))
        self.label_12.setText(QCoreApplication.translate("Form", u"\u0418\u0434\u0435\u0442 \u043f\u0440\u043e\u0446\u0435\u0441\u0441 \u043e\u0431\u0440\u0430\u0431\u043e\u0442\u043a\u0438...", None))
        self.wound_healing_STOP_robot.setText(QCoreApplication.translate("Form", u"\u0421\u0422\u041e\u041f", None))
        self.wound_healing_status_end_process.setText(QCoreApplication.translate("Form", u"\u0413\u041e\u0422\u041e\u0412\u041e", None))
    # retranslateUi


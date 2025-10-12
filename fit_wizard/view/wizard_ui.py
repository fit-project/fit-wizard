#!/usr/bin/env python3
# -*- coding:utf-8 -*-
######
# -----
# Copyright (c) 2023 FIT-Project
# SPDX-License-Identifier: LGPL-3.0-or-later
# -----
######

from PySide6 import QtCore, QtGui, QtWidgets

from fit_wizard.lang import load_translations
from fit_common.core import get_version


class Ui_fit_wizard(object):
    def setupUi(self, fit_wizard):
        fit_wizard.setObjectName("fit_wizard")
        fit_wizard.resize(800, 600)
        fit_wizard.setMinimumSize(QtCore.QSize(800, 600))
        self.styleSheet = QtWidgets.QWidget(parent=fit_wizard)
        self.styleSheet.setStyleSheet(
            "\n"
            "\n"
            "QWidget{\n"
            "    color: rgb(221, 221, 221);\n"
            "    font: 13px;\n"
            "}\n"
            "\n"
            "/* Tooltip */\n"
            "QToolTip {\n"
            "    color: #e06133;\n"
            "    background-color: rgba(33, 37, 43, 180);\n"
            "    border: 1px solid rgb(44, 49, 58);\n"
            "    background-image: none;\n"
            "    background-position: left center;\n"
            "    background-repeat: no-repeat;\n"
            "    border: none;\n"
            "    border-left: 2px solid rgb(224, 97, 51);\n"
            "    text-align: left;\n"
            "    padding-left: 8px;\n"
            "    margin: 0px;\n"
            "}\n"
            "\n"
            "/* Bg App*/\n"
            "#bg_app {    \n"
            "    background-color: rgb(40, 44, 52);\n"
            "    border: 1px solid rgb(44, 49, 58);\n"
            "}\n"
            "\n"
            "/* Title Menu */\n"
            "#title_right_info { font: 13px; }\n"
            "#title_right_info { padding-left: 10px; }\n"
            "\n"
            "\n"
            "/* Content App */\n"
            "#content_top_bg{    \n"
            "    background-color: rgb(33, 37, 43);\n"
            "}\n"
            "#content_bottom{\n"
            "    border-top: 3px solid rgb(44, 49, 58);\n"
            "}\n"
            "\n"
            "/* Top Buttons */\n"
            "#right_buttons_container .QPushButton { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
            "#right_buttons_container .QPushButton:hover { background-color: rgb(44, 49, 57); border-style: solid; border-radius: 4px; }\n"
            "#right_buttons_container .QPushButton:pressed { background-color: rgb(23, 26, 30); border-style: solid; border-radius: 4px; }\n"
            "\n"
            "/* Navigation Buttons */\n"
            "#navigation_buttons_container .QPushButton {background-color: rgb(52, 59, 72); }\n"
            "#navigation_buttons_container .QPushButton:hover { background-color: rgb(44, 49, 57);}\n"
            "#navigation_buttons_container .QPushButton:pressed { background-color: rgb(44, 49, 57);}\n"
            "#navigation_buttons_container .QPushButton:disabled {background-color: rgb(52, 59, 72); color: rgba(255, 255, 255, 10%) }\n"
            "\n"
            "/* Bottom Bar */\n"
            "#bottom_bar { background-color: rgb(44, 49, 58); }\n"
            "#bottom_bar QLabel { font-size: 11px; color: rgb(113, 126, 149); padding-left: 10px; padding-right: 10px; padding-bottom: 2px; }\n"
            "\n"
            "/* LineEdit */\n"
            "QLineEdit {\n"
            "    background-color: rgb(33, 37, 43);\n"
            "    border-radius: 5px;\n"
            "    border: 2px solid rgb(33, 37, 43);\n"
            "    padding-left: 10px;\n"
            "    selection-color: rgb(255, 255, 255);\n"
            "    selection-background-color: rgb(255, 121, 198);\n"
            "}\n"
            "QLineEdit:hover {\n"
            "    border: 2px solid rgb(64, 71, 88);\n"
            "}\n"
            "QLineEdit:focus {\n"
            "    border: 2px solid rgb(91, 101, 124);\n"
            "}\n"
            "\n"
            "/* PlainTextEdit */\n"
            "QPlainTextEdit {\n"
            "    background-color: rgb(27, 29, 35);\n"
            "    border-radius: 5px;\n"
            "    padding: 10px;\n"
            "    selection-color: rgb(255, 255, 255);\n"
            "    selection-background-color: rgb(255, 121, 198);\n"
            "}\n"
            "QPlainTextEdit  QScrollBar:vertical {\n"
            "    width: 8px;\n"
            " }\n"
            "QPlainTextEdit  QScrollBar:horizontal {\n"
            "    height: 8px;\n"
            " }\n"
            "QPlainTextEdit:hover {\n"
            "    border: 2px solid rgb(64, 71, 88);\n"
            "}\n"
            "QPlainTextEdit:focus {\n"
            "    border: 2px solid rgb(91, 101, 124);\n"
            "}\n"
            "\n"
            "/* CheckBox */\n"
            "QCheckBox::indicator {\n"
            "    border: 3px solid rgb(52, 59, 72);\n"
            "    width: 15px;\n"
            "    height: 15px;\n"
            "    border-radius: 10px;\n"
            "    background: rgb(44, 49, 60);\n"
            "    margin:0px 3px 0px 3px;\n"
            "}\n"
            "QCheckBox::indicator:hover {\n"
            "    border: 3px solid rgb(58, 66, 81);\n"
            "}\n"
            "QCheckBox::indicator:checked {\n"
            "    background: 3px solid rgb(52, 59, 72);\n"
            "    border: 3px solid rgb(52, 59, 72);    \n"
            "    background-image: url(:/icons/icons/cil-check-alt.png);\n"
            "}\n"
            "\n"
            "/* ComboBox */\n"
            "QComboBox{\n"
            "    background-color: rgb(33, 37, 43);\n"
            "    border-radius: 5px;\n"
            "    border: 2px solid rgb(33, 37, 43);\n"
            "    padding-bottom: 5px;\n"
            "    padding-top: 5px;\n"
            "    padding-left: 10px;\n"
            "\n"
            "}\n"
            "QComboBox:hover{\n"
            "    border: 2px solid rgb(64, 71, 88);\n"
            "}\n"
            "QComboBox::drop-down {\n"
            "    subcontrol-origin: padding;\n"
            "    subcontrol-position: top right;\n"
            "    width: 25px; \n"
            "    border-left-width: 3px;\n"
            "    border-left-color: rgba(39, 44, 54, 150);\n"
            "    border-left-style: solid;\n"
            "    border-top-right-radius: 3px;\n"
            "    border-bottom-right-radius: 3px;    \n"
            "    background-image: url(:/icons/icons/cil-arrow-bottom.png);\n"
            "    background-position: center;\n"
            "    background-repeat: no-reperat;\n"
            " }\n"
            "\n"
            "QComboBox:!editable{\n"
            "    selection-background-color: rgb(33, 37, 43);\n"
            "}\n"
            "\n"
            "QComboBox QAbstractItemView {\n"
            "    border: none;\n"
            "    background-color: rgb(0, 0, 0);\n"
            "     padding:10px;\n"
            "    selection-background-color: rgb(33, 37, 43);\n"
            "}\n"
            "\n"
            "/* Button */\n"
            "#pages_container QPushButton {\n"
            "    border: 2px solid rgb(52, 59, 72);\n"
            "    border-radius: 5px;    \n"
            "    background-color: rgb(52, 59, 72);\n"
            "}\n"
            "#pages_container QPushButton:hover {\n"
            "    background-color: rgb(57, 65, 80);\n"
            "    border: 2px solid rgb(61, 70, 86);\n"
            "}\n"
            "#pages_container QPushButton:pressed {    \n"
            "    background-color: rgb(35, 40, 49);\n"
            "    border: 2px solid rgb(43, 50, 61);\n"
            "}"
        )
        self.styleSheet.setObjectName("styleSheet")
        self.appMargins = QtWidgets.QVBoxLayout(self.styleSheet)
        self.appMargins.setContentsMargins(10, 10, 10, 10)
        self.appMargins.setSpacing(0)
        self.appMargins.setObjectName("appMargins")
        self.bg_app = QtWidgets.QFrame(parent=self.styleSheet)
        self.bg_app.setStyleSheet("")
        self.bg_app.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.bg_app.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.bg_app.setObjectName("bg_app")
        self.appLayout = QtWidgets.QHBoxLayout(self.bg_app)
        self.appLayout.setContentsMargins(0, 0, 0, 0)
        self.appLayout.setSpacing(0)
        self.appLayout.setObjectName("appLayout")
        self.content_box = QtWidgets.QFrame(parent=self.bg_app)
        self.content_box.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.content_box.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.content_box.setObjectName("content_box")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.content_box)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.content_top_bg = QtWidgets.QFrame(parent=self.content_box)
        self.content_top_bg.setMinimumSize(QtCore.QSize(0, 50))
        self.content_top_bg.setMaximumSize(QtCore.QSize(16777215, 50))
        self.content_top_bg.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.content_top_bg.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.content_top_bg.setObjectName("content_top_bg")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.content_top_bg)
        self.horizontalLayout.setContentsMargins(0, 0, 10, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.left_box = QtWidgets.QFrame(parent=self.content_top_bg)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Preferred,
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.left_box.sizePolicy().hasHeightForWidth())
        self.left_box.setSizePolicy(sizePolicy)
        self.left_box.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.left_box.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.left_box.setObjectName("left_box")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.left_box)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.logo_container_2 = QtWidgets.QFrame(parent=self.left_box)
        self.logo_container_2.setMinimumSize(QtCore.QSize(60, 0))
        self.logo_container_2.setMaximumSize(QtCore.QSize(60, 16777215))
        self.logo_container_2.setObjectName("logo_container_2")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.logo_container_2)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.top_logo = QtWidgets.QLabel(parent=self.logo_container_2)
        self.top_logo.setMinimumSize(QtCore.QSize(42, 42))
        self.top_logo.setMaximumSize(QtCore.QSize(42, 42))
        self.top_logo.setText("")
        self.top_logo.setPixmap(QtGui.QPixmap(":/images/images/logo-42x42.png"))
        self.top_logo.setObjectName("top_logo")
        self.horizontalLayout_8.addWidget(self.top_logo)
        self.horizontalLayout_3.addWidget(self.logo_container_2)
        self.title_right_info = QtWidgets.QLabel(parent=self.left_box)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Preferred,
            QtWidgets.QSizePolicy.Policy.Expanding,
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.title_right_info.sizePolicy().hasHeightForWidth()
        )
        self.title_right_info.setSizePolicy(sizePolicy)
        self.title_right_info.setMaximumSize(QtCore.QSize(16777215, 45))
        self.title_right_info.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignLeading
            | QtCore.Qt.AlignmentFlag.AlignLeft
            | QtCore.Qt.AlignmentFlag.AlignVCenter
        )
        self.title_right_info.setObjectName("title_right_info")
        self.horizontalLayout_3.addWidget(self.title_right_info)
        self.horizontalLayout.addWidget(self.left_box)
        self.right_buttons_container = QtWidgets.QFrame(parent=self.content_top_bg)
        self.right_buttons_container.setMinimumSize(QtCore.QSize(0, 28))
        self.right_buttons_container.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.right_buttons_container.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.right_buttons_container.setObjectName("right_buttons_container")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.right_buttons_container)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verify_timestamp_button = QtWidgets.QPushButton(
            parent=self.right_buttons_container
        )
        self.verify_timestamp_button.setMinimumSize(QtCore.QSize(28, 28))
        self.verify_timestamp_button.setMaximumSize(QtCore.QSize(28, 28))
        self.verify_timestamp_button.setCursor(
            QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor)
        )
        self.verify_timestamp_button.setStyleSheet("QToolTip {font:13px;}")
        self.verify_timestamp_button.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(
            QtGui.QPixmap(
                ":/images/wizard/images/wizard/verify_timestamp-disabled.png"
            ),
            QtGui.QIcon.Mode.Normal,
            QtGui.QIcon.State.Off,
        )
        self.verify_timestamp_button.setIcon(icon)
        self.verify_timestamp_button.setIconSize(QtCore.QSize(20, 20))
        self.verify_timestamp_button.setObjectName("verify_timestamp_button")
        self.horizontalLayout_2.addWidget(self.verify_timestamp_button)
        self.verify_pec_button = QtWidgets.QPushButton(
            parent=self.right_buttons_container
        )
        self.verify_pec_button.setMinimumSize(QtCore.QSize(28, 28))
        self.verify_pec_button.setMaximumSize(QtCore.QSize(28, 28))
        self.verify_pec_button.setStyleSheet("QToolTip {font:13px;}")
        self.verify_pec_button.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(
            QtGui.QPixmap(":/images/wizard/images/wizard/verify_pec-disabled.png"),
            QtGui.QIcon.Mode.Normal,
            QtGui.QIcon.State.Off,
        )
        self.verify_pec_button.setIcon(icon1)
        self.verify_pec_button.setIconSize(QtCore.QSize(20, 20))
        self.verify_pec_button.setObjectName("verify_pec_button")
        self.horizontalLayout_2.addWidget(self.verify_pec_button)
        self.line = QtWidgets.QFrame(parent=self.right_buttons_container)
        self.line.setMinimumSize(QtCore.QSize(0, 40))
        self.line.setMaximumSize(QtCore.QSize(16777215, 40))
        self.line.setStyleSheet("background-color: rgb(40, 44, 52);")
        self.line.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout_2.addWidget(self.line)
        self.configuration_button = QtWidgets.QPushButton(
            parent=self.right_buttons_container
        )
        self.configuration_button.setMinimumSize(QtCore.QSize(28, 28))
        self.configuration_button.setMaximumSize(QtCore.QSize(28, 28))
        self.configuration_button.setCursor(
            QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor)
        )
        self.configuration_button.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(
            QtGui.QPixmap(":/icons/icons/icon_settings-disabled.png"),
            QtGui.QIcon.Mode.Normal,
            QtGui.QIcon.State.Off,
        )
        self.configuration_button.setIcon(icon2)
        self.configuration_button.setIconSize(QtCore.QSize(20, 20))
        self.configuration_button.setObjectName("configuration_button")
        self.horizontalLayout_2.addWidget(self.configuration_button)
        self.minimize_button = QtWidgets.QPushButton(
            parent=self.right_buttons_container
        )
        self.minimize_button.setMinimumSize(QtCore.QSize(28, 28))
        self.minimize_button.setMaximumSize(QtCore.QSize(28, 28))
        self.minimize_button.setCursor(
            QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor)
        )
        self.minimize_button.setToolTip("")
        self.minimize_button.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(
            QtGui.QPixmap(":/icons/icons/icon_minimize-disabled.png"),
            QtGui.QIcon.Mode.Normal,
            QtGui.QIcon.State.Off,
        )
        self.minimize_button.setIcon(icon3)
        self.minimize_button.setIconSize(QtCore.QSize(20, 20))
        self.minimize_button.setObjectName("minimize_button")
        self.horizontalLayout_2.addWidget(self.minimize_button)
        self.close_button = QtWidgets.QPushButton(parent=self.right_buttons_container)
        self.close_button.setMinimumSize(QtCore.QSize(28, 28))
        self.close_button.setMaximumSize(QtCore.QSize(28, 28))
        self.close_button.setCursor(
            QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor)
        )
        self.close_button.setToolTip("")
        self.close_button.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(
            QtGui.QPixmap(":/icons/icons/icon_close-disabled.png"),
            QtGui.QIcon.Mode.Normal,
            QtGui.QIcon.State.Off,
        )
        self.close_button.setIcon(icon4)
        self.close_button.setIconSize(QtCore.QSize(20, 20))
        self.close_button.setObjectName("close_button")
        self.horizontalLayout_2.addWidget(self.close_button)
        self.horizontalLayout.addWidget(
            self.right_buttons_container, 0, QtCore.Qt.AlignmentFlag.AlignRight
        )
        self.verticalLayout_2.addWidget(self.content_top_bg)
        self.content_bottom = QtWidgets.QFrame(parent=self.content_box)
        self.content_bottom.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.content_bottom.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.content_bottom.setObjectName("content_bottom")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.content_bottom)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.content = QtWidgets.QFrame(parent=self.content_bottom)
        self.content.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.content.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.content.setObjectName("content")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.content)
        self.horizontalLayout_4.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pages_container = QtWidgets.QFrame(parent=self.content)
        self.pages_container.setObjectName("pages_container")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.pages_container)
        self.verticalLayout.setContentsMargins(1, -1, 1, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pages = QtWidgets.QStackedWidget(parent=self.pages_container)
        self.pages.setMinimumSize(QtCore.QSize(0, 409))
        self.pages.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.DefaultContextMenu)
        self.pages.setStyleSheet("background: transparent;")
        self.pages.setObjectName("pages")
        self.case_info_page = QtWidgets.QWidget()
        self.case_info_page.setObjectName("case_info_page")
        self.case_info = QtWidgets.QFrame(parent=self.case_info_page)
        self.case_info.setGeometry(QtCore.QRect(0, -2, 761, 409))
        self.case_info.setMaximumSize(QtCore.QSize(16777215, 409))
        self.case_info.setObjectName("case_info")
        self.caseInfo = QtWidgets.QHBoxLayout(self.case_info)
        self.caseInfo.setContentsMargins(1, 1, 1, 1)
        self.caseInfo.setObjectName("caseInfo")
        spacerItem = QtWidgets.QSpacerItem(
            40,
            20,
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Minimum,
        )
        self.caseInfo.addItem(spacerItem)
        self.form = QtWidgets.QFrame(parent=self.case_info)
        self.form.setMinimumSize(QtCore.QSize(460, 0))
        self.form.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.form.setObjectName("form")
        self.form_layout = QtWidgets.QVBoxLayout(self.form)
        self.form_layout.setContentsMargins(0, 0, 0, 0)
        self.form_layout.setSpacing(8)
        self.form_layout.setObjectName("form_layout")
        self.name = QtWidgets.QComboBox(parent=self.form)
        self.name.setMaximumSize(QtCore.QSize(300, 16777215))
        self.name.setAutoFillBackground(False)
        self.name.setStyleSheet("background-color: rgb(33, 37, 43);")
        self.name.setEditable(True)
        self.name.setIconSize(QtCore.QSize(16, 16))
        self.name.setFrame(True)
        self.name.setObjectName("name")
        self.form_layout.addWidget(self.name)
        self.lawyer_name = QtWidgets.QLineEdit(parent=self.form)
        self.lawyer_name.setMinimumSize(QtCore.QSize(0, 30))
        self.lawyer_name.setMaximumSize(QtCore.QSize(300, 16777215))
        self.lawyer_name.setStyleSheet("background-color: rgb(33, 37, 43);")
        self.lawyer_name.setText("")
        self.lawyer_name.setObjectName("lawyer_name")
        self.form_layout.addWidget(self.lawyer_name)
        self.operator = QtWidgets.QLineEdit(parent=self.form)
        self.operator.setMinimumSize(QtCore.QSize(0, 30))
        self.operator.setMaximumSize(QtCore.QSize(300, 16777215))
        self.operator.setStyleSheet("background-color: rgb(33, 37, 43);")
        self.operator.setText("")
        self.operator.setObjectName("operator")
        self.form_layout.addWidget(self.operator)
        self.proceeding_type = QtWidgets.QComboBox(parent=self.form)
        self.proceeding_type.setMaximumSize(QtCore.QSize(300, 16777215))
        self.proceeding_type.setMouseTracking(True)
        self.proceeding_type.setAutoFillBackground(False)
        self.proceeding_type.setStyleSheet("background-color: rgb(33, 37, 43);")
        self.proceeding_type.setEditable(True)
        self.proceeding_type.setCurrentText("")
        self.proceeding_type.setIconSize(QtCore.QSize(16, 16))
        self.proceeding_type.setFrame(True)
        self.proceeding_type.setObjectName("proceeding_type")
        self.form_layout.addWidget(self.proceeding_type)
        self.courthouse = QtWidgets.QLineEdit(parent=self.form)
        self.courthouse.setMinimumSize(QtCore.QSize(0, 30))
        self.courthouse.setMaximumSize(QtCore.QSize(300, 16777215))
        self.courthouse.setStyleSheet("background-color: rgb(33, 37, 43);")
        self.courthouse.setText("")
        self.courthouse.setObjectName("courthouse")
        self.form_layout.addWidget(self.courthouse)
        self.proceeding_number = QtWidgets.QLineEdit(parent=self.form)
        self.proceeding_number.setMinimumSize(QtCore.QSize(0, 30))
        self.proceeding_number.setMaximumSize(QtCore.QSize(300, 16777215))
        self.proceeding_number.setStyleSheet("background-color: rgb(33, 37, 43);")
        self.proceeding_number.setText("")
        self.proceeding_number.setObjectName("proceeding_number")
        self.form_layout.addWidget(self.proceeding_number)
        self.logo_container = QtWidgets.QFrame(parent=self.form)
        self.logo_container.setMinimumSize(QtCore.QSize(0, 0))
        self.logo_container.setMaximumSize(QtCore.QSize(16777215, 30))
        self.logo_container.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.logo_container.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.logo_container.setObjectName("logo_container")
        self.logo_layout = QtWidgets.QHBoxLayout(self.logo_container)
        self.logo_layout.setContentsMargins(0, 0, 0, 0)
        self.logo_layout.setObjectName("logo_layout")
        self.logo = QtWidgets.QLineEdit(parent=self.logo_container)
        self.logo.setMinimumSize(QtCore.QSize(300, 30))
        self.logo.setMaximumSize(QtCore.QSize(300, 16777215))
        self.logo.setStyleSheet("background-color: rgb(33, 37, 43);")
        self.logo.setText("")
        self.logo.setObjectName("logo")
        self.logo_layout.addWidget(self.logo)
        self.label = QtWidgets.QLabel(parent=self.logo_container)
        self.label.setMaximumSize(QtCore.QSize(20, 20))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/icons/icons/info-circle-disabled.png"))
        self.label.setScaledContents(False)
        self.label.setObjectName("label")
        self.logo_layout.addWidget(self.label)
        self.logo_button = QtWidgets.QPushButton(parent=self.logo_container)
        self.logo_button.setMinimumSize(QtCore.QSize(0, 30))
        self.logo_button.setMaximumSize(QtCore.QSize(120, 16777215))
        self.logo_button.setCursor(
            QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor)
        )
        icon5 = QtGui.QIcon()
        icon5.addPixmap(
            QtGui.QPixmap(":/icons/icons/cil-folder-open.png"),
            QtGui.QIcon.Mode.Normal,
            QtGui.QIcon.State.Off,
        )
        self.logo_button.setIcon(icon5)
        self.logo_button.setObjectName("logo_button")
        self.logo_layout.addWidget(self.logo_button)
        self.form_layout.addWidget(self.logo_container)
        self.notes = QtWidgets.QPlainTextEdit(parent=self.form)
        self.notes.setMinimumSize(QtCore.QSize(0, 0))
        self.notes.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.notes.setStyleSheet("background-color: rgb(33, 37, 43);")
        self.notes.setObjectName("notes")
        self.form_layout.addWidget(self.notes)
        self.caseInfo.addWidget(self.form)
        spacerItem1 = QtWidgets.QSpacerItem(
            40,
            20,
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Minimum,
        )
        self.caseInfo.addItem(spacerItem1)
        self.pages.addWidget(self.case_info_page)
        self.tasks_page = QtWidgets.QWidget()
        self.tasks_page.setObjectName("tasks_page")
        self.tasks_container = QtWidgets.QWidget(parent=self.tasks_page)
        self.tasks_container.setGeometry(QtCore.QRect(0, 0, 751, 411))
        self.tasks_container.setObjectName("tasks_container")
        self.horizontalLayoutWidget = QtWidgets.QWidget(parent=self.tasks_container)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 751, 121))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.tasks_row_1 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.tasks_row_1.setSizeConstraint(
            QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint
        )
        self.tasks_row_1.setContentsMargins(0, 10, 0, 10)
        self.tasks_row_1.setSpacing(10)
        self.tasks_row_1.setObjectName("tasks_row_1")
        spacerItem2 = QtWidgets.QSpacerItem(
            5,
            20,
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Minimum,
        )
        self.tasks_row_1.addItem(spacerItem2)
        self.frame_web = QtWidgets.QFrame(parent=self.horizontalLayoutWidget)
        self.frame_web.setMinimumSize(QtCore.QSize(160, 0))
        self.frame_web.setMaximumSize(QtCore.QSize(160, 100))
        self.frame_web.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.frame_web.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.frame_web.setObjectName("frame_web")
        self.verticalLayoutWidget_8 = QtWidgets.QWidget(parent=self.frame_web)
        self.verticalLayoutWidget_8.setGeometry(QtCore.QRect(0, 0, 161, 101))
        self.verticalLayoutWidget_8.setMinimumSize(QtCore.QSize(161, 0))
        self.verticalLayoutWidget_8.setMaximumSize(QtCore.QSize(161, 101))
        self.verticalLayoutWidget_8.setObjectName("verticalLayoutWidget_8")
        self.vlayout_web = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_8)
        self.vlayout_web.setContentsMargins(5, 0, 0, 10)
        self.vlayout_web.setObjectName("vlayout_web")
        self.label_web = QtWidgets.QLabel(parent=self.verticalLayoutWidget_8)
        self.label_web.setMinimumSize(QtCore.QSize(155, 0))
        self.label_web.setMaximumSize(QtCore.QSize(155, 68))
        self.label_web.setText("")
        self.label_web.setPixmap(QtGui.QPixmap(":/images/wizard/images/wizard/web.png"))
        self.label_web.setScaledContents(False)
        self.label_web.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_web.setObjectName("label_web")
        self.vlayout_web.addWidget(self.label_web)
        self.web = QtWidgets.QCheckBox(parent=self.verticalLayoutWidget_8)
        self.web.setMaximumSize(QtCore.QSize(150, 16777215))
        self.web.setChecked(False)
        self.web.setObjectName("web")
        self.vlayout_web.addWidget(self.web)
        self.tasks_row_1.addWidget(self.frame_web)
        self.frame_mail = QtWidgets.QFrame(parent=self.horizontalLayoutWidget)
        self.frame_mail.setMinimumSize(QtCore.QSize(160, 0))
        self.frame_mail.setMaximumSize(QtCore.QSize(160, 100))
        self.frame_mail.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.frame_mail.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.frame_mail.setObjectName("frame_mail")
        self.verticalLayoutWidget_13 = QtWidgets.QWidget(parent=self.frame_mail)
        self.verticalLayoutWidget_13.setGeometry(QtCore.QRect(0, 0, 161, 101))
        self.verticalLayoutWidget_13.setMinimumSize(QtCore.QSize(161, 0))
        self.verticalLayoutWidget_13.setMaximumSize(QtCore.QSize(161, 101))
        self.verticalLayoutWidget_13.setObjectName("verticalLayoutWidget_13")
        self.vlayout_mail = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_13)
        self.vlayout_mail.setContentsMargins(5, 0, 0, 10)
        self.vlayout_mail.setObjectName("vlayout_mail")
        self.label_mail = QtWidgets.QLabel(parent=self.verticalLayoutWidget_13)
        self.label_mail.setMinimumSize(QtCore.QSize(155, 0))
        self.label_mail.setMaximumSize(QtCore.QSize(155, 68))
        self.label_mail.setText("")
        self.label_mail.setPixmap(
            QtGui.QPixmap(":/images/wizard/images/wizard/mail.png")
        )
        self.label_mail.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_mail.setObjectName("label_mail")
        self.vlayout_mail.addWidget(self.label_mail)
        self.mail = QtWidgets.QCheckBox(parent=self.verticalLayoutWidget_13)
        self.mail.setMaximumSize(QtCore.QSize(150, 16777215))
        self.mail.setChecked(False)
        self.mail.setObjectName("mail")
        self.vlayout_mail.addWidget(self.mail)
        self.tasks_row_1.addWidget(self.frame_mail)
        self.frame_instagram = QtWidgets.QFrame(parent=self.horizontalLayoutWidget)
        self.frame_instagram.setMinimumSize(QtCore.QSize(160, 0))
        self.frame_instagram.setMaximumSize(QtCore.QSize(160, 100))
        self.frame_instagram.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.frame_instagram.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.frame_instagram.setObjectName("frame_instagram")
        self.verticalLayoutWidget_14 = QtWidgets.QWidget(parent=self.frame_instagram)
        self.verticalLayoutWidget_14.setGeometry(QtCore.QRect(0, 0, 161, 101))
        self.verticalLayoutWidget_14.setMinimumSize(QtCore.QSize(161, 0))
        self.verticalLayoutWidget_14.setMaximumSize(QtCore.QSize(161, 101))
        self.verticalLayoutWidget_14.setObjectName("verticalLayoutWidget_14")
        self.vlayout_instagram = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_14)
        self.vlayout_instagram.setContentsMargins(5, 0, 0, 10)
        self.vlayout_instagram.setObjectName("vlayout_instagram")
        self.label_instagram = QtWidgets.QLabel(parent=self.verticalLayoutWidget_14)
        self.label_instagram.setMinimumSize(QtCore.QSize(155, 0))
        self.label_instagram.setMaximumSize(QtCore.QSize(155, 68))
        self.label_instagram.setText("")
        self.label_instagram.setPixmap(
            QtGui.QPixmap(":/images/wizard/images/wizard/instagram.png")
        )
        self.label_instagram.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_instagram.setObjectName("label_instagram")
        self.vlayout_instagram.addWidget(self.label_instagram)
        self.instagram = QtWidgets.QCheckBox(parent=self.verticalLayoutWidget_14)
        self.instagram.setMaximumSize(QtCore.QSize(150, 16777215))
        self.instagram.setChecked(False)
        self.instagram.setObjectName("instagram")
        self.vlayout_instagram.addWidget(self.instagram)
        self.tasks_row_1.addWidget(self.frame_instagram)
        self.frame_video = QtWidgets.QFrame(parent=self.horizontalLayoutWidget)
        self.frame_video.setMinimumSize(QtCore.QSize(160, 0))
        self.frame_video.setMaximumSize(QtCore.QSize(160, 100))
        self.frame_video.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.frame_video.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.frame_video.setObjectName("frame_video")
        self.verticalLayoutWidget_18 = QtWidgets.QWidget(parent=self.frame_video)
        self.verticalLayoutWidget_18.setGeometry(QtCore.QRect(0, 0, 161, 101))
        self.verticalLayoutWidget_18.setMinimumSize(QtCore.QSize(161, 0))
        self.verticalLayoutWidget_18.setMaximumSize(QtCore.QSize(161, 101))
        self.verticalLayoutWidget_18.setObjectName("verticalLayoutWidget_18")
        self.vlayout_video = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_18)
        self.vlayout_video.setContentsMargins(5, 0, 0, 10)
        self.vlayout_video.setObjectName("vlayout_video")
        self.label_video = QtWidgets.QLabel(parent=self.verticalLayoutWidget_18)
        self.label_video.setMinimumSize(QtCore.QSize(155, 0))
        self.label_video.setMaximumSize(QtCore.QSize(155, 68))
        self.label_video.setText("")
        self.label_video.setPixmap(
            QtGui.QPixmap(":/images/wizard/images/wizard/video.png")
        )
        self.label_video.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_video.setObjectName("label_video")
        self.vlayout_video.addWidget(self.label_video)
        self.video = QtWidgets.QCheckBox(parent=self.verticalLayoutWidget_18)
        self.video.setMaximumSize(QtCore.QSize(150, 16777215))
        self.video.setChecked(False)
        self.video.setObjectName("video")
        self.vlayout_video.addWidget(self.video)
        self.tasks_row_1.addWidget(self.frame_video)
        spacerItem3 = QtWidgets.QSpacerItem(
            40,
            20,
            QtWidgets.QSizePolicy.Policy.Fixed,
            QtWidgets.QSizePolicy.Policy.Minimum,
        )
        self.tasks_row_1.addItem(spacerItem3)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(parent=self.tasks_container)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(0, 120, 751, 111))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.tasks_row_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.tasks_row_2.setSizeConstraint(
            QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint
        )
        self.tasks_row_2.setContentsMargins(0, 0, 0, 10)
        self.tasks_row_2.setSpacing(10)
        self.tasks_row_2.setObjectName("tasks_row_2")
        spacerItem4 = QtWidgets.QSpacerItem(
            5,
            20,
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Minimum,
        )
        self.tasks_row_2.addItem(spacerItem4)
        self.frame_entire_website = QtWidgets.QFrame(
            parent=self.horizontalLayoutWidget_2
        )
        self.frame_entire_website.setMinimumSize(QtCore.QSize(160, 0))
        self.frame_entire_website.setMaximumSize(QtCore.QSize(160, 100))
        self.frame_entire_website.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.frame_entire_website.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.frame_entire_website.setObjectName("frame_entire_website")
        self.verticalLayoutWidget_11 = QtWidgets.QWidget(
            parent=self.frame_entire_website
        )
        self.verticalLayoutWidget_11.setGeometry(QtCore.QRect(0, 0, 161, 101))
        self.verticalLayoutWidget_11.setMinimumSize(QtCore.QSize(161, 0))
        self.verticalLayoutWidget_11.setMaximumSize(QtCore.QSize(161, 101))
        self.verticalLayoutWidget_11.setObjectName("verticalLayoutWidget_11")
        self.vlayout_entire_website = QtWidgets.QVBoxLayout(
            self.verticalLayoutWidget_11
        )
        self.vlayout_entire_website.setContentsMargins(5, 0, 0, 10)
        self.vlayout_entire_website.setObjectName("vlayout_entire_website")
        self.label_entire_website = QtWidgets.QLabel(
            parent=self.verticalLayoutWidget_11
        )
        self.label_entire_website.setMinimumSize(QtCore.QSize(155, 0))
        self.label_entire_website.setMaximumSize(QtCore.QSize(155, 68))
        self.label_entire_website.setText("")
        self.label_entire_website.setPixmap(
            QtGui.QPixmap(":/images/wizard/images/wizard/entire_website.png")
        )
        self.label_entire_website.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_entire_website.setObjectName("label_entire_website")
        self.vlayout_entire_website.addWidget(self.label_entire_website)
        self.entire_website = QtWidgets.QCheckBox(parent=self.verticalLayoutWidget_11)
        self.entire_website.setMaximumSize(QtCore.QSize(150, 16777215))
        self.entire_website.setChecked(False)
        self.entire_website.setObjectName("entire_website")
        self.vlayout_entire_website.addWidget(self.entire_website)
        self.tasks_row_2.addWidget(self.frame_entire_website)
        spacerItem5 = QtWidgets.QSpacerItem(
            550,
            20,
            QtWidgets.QSizePolicy.Policy.Fixed,
            QtWidgets.QSizePolicy.Policy.Minimum,
        )
        self.tasks_row_2.addItem(spacerItem5)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(parent=self.tasks_container)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(0, 230, 751, 111))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.tasks_row_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.tasks_row_3.setSizeConstraint(
            QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint
        )
        self.tasks_row_3.setContentsMargins(0, 0, 0, 10)
        self.tasks_row_3.setSpacing(10)
        self.tasks_row_3.setObjectName("tasks_row_3")
        spacerItem6 = QtWidgets.QSpacerItem(
            5,
            20,
            QtWidgets.QSizePolicy.Policy.Fixed,
            QtWidgets.QSizePolicy.Policy.Minimum,
        )
        self.tasks_row_3.addItem(spacerItem6)
        spacerItem7 = QtWidgets.QSpacerItem(
            5,
            20,
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Minimum,
        )
        self.tasks_row_3.addItem(spacerItem7)
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(parent=self.tasks_container)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(0, 340, 751, 51))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.row_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.row_4.setSizeConstraint(
            QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint
        )
        self.row_4.setContentsMargins(0, 0, 0, 10)
        self.row_4.setSpacing(10)
        self.row_4.setObjectName("row_4")
        spacerItem8 = QtWidgets.QSpacerItem(
            5,
            20,
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Minimum,
        )
        self.row_4.addItem(spacerItem8)
        self.case_summary_button = QtWidgets.QPushButton(
            parent=self.horizontalLayoutWidget_4
        )
        self.case_summary_button.setMinimumSize(QtCore.QSize(150, 30))
        self.case_summary_button.setCursor(
            QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor)
        )
        self.case_summary_button.setStyleSheet("background-color: rgb(52, 59, 72);")
        self.case_summary_button.setObjectName("case_summary_button")
        self.row_4.addWidget(self.case_summary_button)
        spacerItem9 = QtWidgets.QSpacerItem(
            5,
            20,
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Minimum,
        )
        self.row_4.addItem(spacerItem9)
        self.pages.addWidget(self.tasks_page)
        self.verticalLayout.addWidget(self.pages)
        self.navigation_buttons_container = QtWidgets.QFrame(
            parent=self.pages_container
        )
        self.navigation_buttons_container.setMaximumSize(QtCore.QSize(16777215, 40))
        self.navigation_buttons_container.setObjectName("navigation_buttons_container")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(
            self.navigation_buttons_container
        )
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem10 = QtWidgets.QSpacerItem(
            40,
            20,
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Minimum,
        )
        self.horizontalLayout_6.addItem(spacerItem10)
        self.back_button = QtWidgets.QPushButton(
            parent=self.navigation_buttons_container
        )
        self.back_button.setEnabled(True)
        self.back_button.setMinimumSize(QtCore.QSize(80, 30))
        self.back_button.setCursor(
            QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor)
        )
        self.back_button.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.back_button.setObjectName("back_button")
        self.horizontalLayout_6.addWidget(self.back_button)
        spacerItem11 = QtWidgets.QSpacerItem(
            5,
            20,
            QtWidgets.QSizePolicy.Policy.Minimum,
            QtWidgets.QSizePolicy.Policy.Minimum,
        )
        self.horizontalLayout_6.addItem(spacerItem11)
        self.next_button = QtWidgets.QPushButton(
            parent=self.navigation_buttons_container
        )
        self.next_button.setEnabled(True)
        self.next_button.setMinimumSize(QtCore.QSize(80, 30))
        self.next_button.setCursor(
            QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor)
        )
        self.next_button.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.next_button.setStyleSheet(
            ":disabled {background-color: rgb(52, 59, 72); color: rgba(255, 255, 255, 10%) }"
        )
        self.next_button.setObjectName("next_button")
        self.horizontalLayout_6.addWidget(self.next_button)
        self.verticalLayout.addWidget(self.navigation_buttons_container)
        self.horizontalLayout_4.addWidget(self.pages_container)
        self.verticalLayout_6.addWidget(self.content)
        self.bottom_bar = QtWidgets.QFrame(parent=self.content_bottom)
        self.bottom_bar.setMinimumSize(QtCore.QSize(0, 22))
        self.bottom_bar.setMaximumSize(QtCore.QSize(16777215, 22))
        self.bottom_bar.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.bottom_bar.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.bottom_bar.setObjectName("bottom_bar")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.bottom_bar)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.credits_label = QtWidgets.QLabel(parent=self.bottom_bar)
        self.credits_label.setMaximumSize(QtCore.QSize(16777215, 16))
        self.credits_label.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignLeading
            | QtCore.Qt.AlignmentFlag.AlignLeft
            | QtCore.Qt.AlignmentFlag.AlignVCenter
        )
        self.credits_label.setObjectName("credits_label")
        self.horizontalLayout_5.addWidget(self.credits_label)
        self.version = QtWidgets.QLabel(parent=self.bottom_bar)
        self.version.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignRight
            | QtCore.Qt.AlignmentFlag.AlignTrailing
            | QtCore.Qt.AlignmentFlag.AlignVCenter
        )
        self.version.setObjectName("version")
        self.horizontalLayout_5.addWidget(self.version)
        self.frame_size_grip = QtWidgets.QFrame(parent=self.bottom_bar)
        self.frame_size_grip.setMinimumSize(QtCore.QSize(20, 0))
        self.frame_size_grip.setMaximumSize(QtCore.QSize(20, 16777215))
        self.frame_size_grip.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.frame_size_grip.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_size_grip.setObjectName("frame_size_grip")
        self.horizontalLayout_5.addWidget(self.frame_size_grip)
        self.verticalLayout_6.addWidget(self.bottom_bar)
        self.verticalLayout_2.addWidget(self.content_bottom)
        self.appLayout.addWidget(self.content_box)
        self.appMargins.addWidget(self.bg_app)
        fit_wizard.setCentralWidget(self.styleSheet)

        self.retranslateUi(fit_wizard)
        self.pages.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(fit_wizard)

    def retranslateUi(self, fit_wizard):

        fit_wizard.setWindowTitle("FIT Wizard")
        self.translations = load_translations()
        self.title_right_info.setText(self.translations["TITLE_RIGHT_INFO"])
        self.verify_timestamp_button.setToolTip(
            self.translations["VERIFY_TIMESTAMP_BUTTON"]
        )
        self.verify_pec_button.setToolTip(self.translations["VERIFY_PEC_BUTTON"])
        self.configuration_button.setToolTip(self.translations["cONFIGURATION_BUTTON"])

        self.lawyer_name.setPlaceholderText(self.translations["LAWYER"])
        self.operator.setPlaceholderText(self.translations["OPERATOR"])
        self.courthouse.setPlaceholderText(self.translations["COURTHOUSE"])
        self.proceeding_number.setPlaceholderText(
            self.translations["PROCEEDING_NUMBER"]
        )
        self.logo.setPlaceholderText(self.translations["LOGO"])
        self.logo_button.setText(self.translations["LOGO_BUTTON"])
        self.notes.setPlaceholderText(self.translations["NOTES"])

        self.web.setText(self.translations["TASK_WEB"])
        self.mail.setText(self.translations["TASK_MAIL"])
        self.instagram.setText(self.translations["TASK_INSTAGRAM"])
        self.video.setText(self.translations["TASK_VIDEO"])
        self.entire_website.setText(self.translations["TASK_ENTIRE_WEBSITE"])
        self.case_summary_button.setText(self.translations["CASE_SUMMARY"])
        self.back_button.setText(self.translations["BACK_BUTTON"])
        self.next_button.setText(self.translations["NEXT_BUTTON"])
        self.credits_label.setText("By: fit-project.org")
        self.version.setText(f"v{get_version()}")

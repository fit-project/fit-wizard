#!/usr/bin/env python3
# -*- coding:utf-8 -*-
######
# -----
# Copyright (c) 2023 FIT-Project
# SPDX-License-Identifier: LGPL-3.0-or-later
# -----
######


from PySide6 import QtCore, QtWidgets

from fit_cases.view.case_form_manager import CaseFormManager

from fit_common.gui.error import Error as ErrorView

from fit_verify_pec.view.verify_pec import VerifyPec as VerifyPecView
from fit_verify_pdf_timestamp.view.verify_pdf_timestamp import (
    VerifyPDFTimestamp as VerifyPDFTimestampView,
)

from fit_configurations.utils import show_configuration_dialog
from fit_cases.utils import show_case_info_dialog

from fit_common.core.utils import get_version

from fit_wizard.lang import load_translations

from fit_wizard.view.wizard_ui import (
    Ui_fit_wizard,
)

from fit_assets import resources


class Wizard(QtWidgets.QMainWindow):
    finished = QtCore.Signal(str, dict)

    def __init__(self, parent=None):
        super(Wizard, self).__init__(parent)
        self.selcted_task = None
        self.case_info = {}

        self.translations = load_translations()

        self.__init_ui()

    def __init_ui(self):

        # HIDE STANDARD TITLE BAR
        self.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)

        self.ui = Ui_fit_wizard()
        self.ui.setupUi(self)

        # CUSTOM TOP BAR
        self.ui.left_box.mouseMoveEvent = self.move_window

        # MINIMIZE BUTTON
        self.ui.minimize_button.clicked.connect(self.showMinimized)

        # CLOSE BUTTON
        self.ui.close_button.clicked.connect(self.close)

        # CONFIGURATION BUTTON
        self.ui.configuration_button.clicked.connect(show_configuration_dialog)

        # VERIFY TIMESTAMP BUTTON
        self.ui.verify_timestamp_button.clicked.connect(self.__verify_timestamp)

        # VERIFY PEC BUTTON
        self.ui.verify_pec_button.clicked.connect(self.__verify_pec)

        # PAGES
        self.ui.pages.setCurrentIndex(0)

        # NEXT BUTTON
        self.ui.next_button.setEnabled(False)
        self.ui.next_button.clicked.connect(self.__next_page)

        # BACK BUTTON
        self.ui.back_button.clicked.connect(self.__back_page)
        self.ui.back_button.hide()

        # SET VERSION
        self.ui.version.setText(get_version())

        # PAGE1 CASE INFO FORM
        self.form_manager = CaseFormManager(self.ui.form)
        self.form_manager.name.currentTextChanged.connect(self.__enable_next_button)

        # PAGE2 SELECT TASK
        self.tasks = self.ui.tasks_page.findChildren(QtWidgets.QCheckBox)

        for task in self.tasks:
            task.setAttribute(QtCore.Qt.WidgetAttribute.WA_MacShowFocusRect, 0)
            task.clicked.connect(self.__task_clicked)

        # SUMMARY BUTTON
        self.ui.case_summary_button.clicked.connect(show_case_info_dialog)
        self.ui.case_summary_button.hide()

    def mousePressEvent(self, event):
        self.dragPos = event.globalPosition().toPoint()

    def move_window(self, event):
        if event.buttons() == QtCore.Qt.MouseButton.LeftButton:
            self.move(self.pos() + event.globalPosition().toPoint() - self.dragPos)
            self.dragPos = event.globalPosition().toPoint()
            event.accept()

    def __next_page(self):
        if self.ui.pages.currentIndex() == 0:
            self.ui.pages.setCurrentIndex(self.ui.pages.currentIndex() + 1)
            self.ui.back_button.show()

            if self.ui.pages.currentIndex() == self.ui.pages.count() - 1:
                self.__load_case_info()
                self.ui.next_button.setText("Start")
                self.ui.next_button.setEnabled(False)

        elif self.ui.pages.currentIndex() == self.ui.pages.count() - 1:
            self.__start()

    def __back_page(self):

        if self.ui.pages.currentIndex() > 0:
            self.ui.pages.setCurrentIndex(self.pages.currentIndex() - 1)
            self.ui.next_button.setText("Next >")
            self.__enable_next_button()

        if self.ui.pages.currentIndex() == 0:
            self.__unchecked_tasks()
            self.ui.back_button.hide()

    def __verify_timestamp(self):
        verify_timestamp = VerifyPDFTimestampView(self)
        verify_timestamp.show()

    def __verify_pec(self):
        verify_pec = VerifyPecView(self)
        verify_pec.show()

    def reload_case_info(self):
        self.form_manager.set_case_information()

    def __load_case_info(self):
        self.case_info = self.form_manager.get_current_case_info()

    def __enable_next_button(self):
        if self.form_manager.name.currentText():
            self.ui.next_button.setEnabled(True)
        else:
            self.ui.next_button.setEnabled(False)

    def __unchecked_tasks(self):
        for task in self.tasks:
            task.setChecked(False)

    def __task_clicked(self):
        if self.sender().isChecked():
            for task in self.tasks:
                if task.isChecked() and task != self.sender():
                    task.setChecked(False)

            self.ui.next_button.setEnabled(True)
            self.selcted_task = self.sender().objectName()
        else:
            self.ui.next_button.setEnabled(False)
            self.selcted_task = None

    def __start(self):
        # store information case on the local DB
        try:
            if "id" in self.case_info:
                self.form_manager.controller.cases = self.case_info
            else:
                self.case_info = self.form_manager.controller.add(self.case_info)
                self.form_manager.set_current_cases()
                self.form_manager.set_index_from_case_id(self.case_info["id"])
        except Exception as e:
            error_dlg = ErrorView(
                QtWidgets.QMessageBox.Icon.Warning,
                self.translations["INSERT_UPDATE_CASE_INFO"],
                self.translations["INSERT_UPDATE_CASE_INFO"],
                str(e),
            )
            error_dlg.exec()

        # Send signal to main loop to start the acquisition window
        self.finished.emit(self.selcted_task, self.case_info)
        self.hide()

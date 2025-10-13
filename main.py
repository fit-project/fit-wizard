#!/usr/bin/env python3
# -*- coding:utf-8 -*-
######
# -----
# Copyright (c) 2023 FIT-Project
# SPDX-License-Identifier: LGPL-3.0-or-later
# -----
######

from PySide6.QtWidgets import QApplication
import sys

from fit_wizard.view.wizard import Wizard


def main():
    def start_task():
        print(f"task: {wizard.selcted_task}")
        print(f"case_info: {wizard.case_info}")
        wizard.close()

    app = QApplication(sys.argv)
    wizard = Wizard()
    wizard.finished.connect(start_task)
    wizard.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()

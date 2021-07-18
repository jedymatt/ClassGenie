# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'OptionDialog.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_OptionDialog(object):
    def setupUi(self, OptionDialog):
        if not OptionDialog.objectName():
            OptionDialog.setObjectName(u"OptionDialog")
        OptionDialog.resize(334, 187)
        self.verticalLayout = QVBoxLayout(OptionDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.buttonNewAverage = QPushButton(OptionDialog)
        self.buttonNewAverage.setObjectName(u"buttonNewAverage")

        self.verticalLayout.addWidget(self.buttonNewAverage)

        self.buttonExistingAverage = QPushButton(OptionDialog)
        self.buttonExistingAverage.setObjectName(u"buttonExistingAverage")

        self.verticalLayout.addWidget(self.buttonExistingAverage)


        self.retranslateUi(OptionDialog)

        QMetaObject.connectSlotsByName(OptionDialog)
    # setupUi

    def retranslateUi(self, OptionDialog):
        OptionDialog.setWindowTitle(QCoreApplication.translate("OptionDialog", u"sheetName", None))
        self.buttonNewAverage.setText(QCoreApplication.translate("OptionDialog", u"Enter new average grades", None))
        self.buttonExistingAverage.setText(QCoreApplication.translate("OptionDialog", u"Increase/decrease existing average grades", None))
    # retranslateUi


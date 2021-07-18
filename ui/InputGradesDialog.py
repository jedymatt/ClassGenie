# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'InputGradesDialog.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_InputGradesDialog(object):
    def setupUi(self, InputGradesDialog):
        if not InputGradesDialog.objectName():
            InputGradesDialog.setObjectName(u"InputGradesDialog")
        InputGradesDialog.resize(577, 396)
        self.gridLayout = QGridLayout(InputGradesDialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tableWidget = QTableWidget(InputGradesDialog)
        self.tableWidget.setObjectName(u"tableWidget")

        self.gridLayout.addWidget(self.tableWidget, 0, 0, 5, 1)

        self.pushButton = QPushButton(InputGradesDialog)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout.addWidget(self.pushButton, 4, 1, 1, 1)

        self.label = QLabel(InputGradesDialog)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)

        self.checkBox = QCheckBox(InputGradesDialog)
        self.checkBox.setObjectName(u"checkBox")

        self.gridLayout.addWidget(self.checkBox, 1, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 2, 1, 1, 1)


        self.retranslateUi(InputGradesDialog)

        QMetaObject.connectSlotsByName(InputGradesDialog)
    # setupUi

    def retranslateUi(self, InputGradesDialog):
        InputGradesDialog.setWindowTitle(QCoreApplication.translate("InputGradesDialog", u"Dialog", None))
        self.pushButton.setText(QCoreApplication.translate("InputGradesDialog", u"Generate", None))
        self.label.setText(QCoreApplication.translate("InputGradesDialog", u"Options:", None))
        self.checkBox.setText(QCoreApplication.translate("InputGradesDialog", u"Overwrite all", None))
    # retranslateUi


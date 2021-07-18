# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'InputGradesWidget.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_InputGradesWidget(object):
    def setupUi(self, InputGradesWidget):
        if not InputGradesWidget.objectName():
            InputGradesWidget.setObjectName(u"InputGradesWidget")
        InputGradesWidget.resize(595, 427)
        self.gridLayout = QGridLayout(InputGradesWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(InputGradesWidget)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)

        self.checkBox = QCheckBox(InputGradesWidget)
        self.checkBox.setObjectName(u"checkBox")

        self.gridLayout.addWidget(self.checkBox, 1, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 2, 1, 1, 1)

        self.pushButton = QPushButton(InputGradesWidget)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout.addWidget(self.pushButton, 3, 1, 1, 1)

        self.tableWidget = QTableWidget(InputGradesWidget)
        self.tableWidget.setObjectName(u"tableWidget")

        self.gridLayout.addWidget(self.tableWidget, 0, 0, 4, 1)


        self.retranslateUi(InputGradesWidget)

        QMetaObject.connectSlotsByName(InputGradesWidget)
    # setupUi

    def retranslateUi(self, InputGradesWidget):
        InputGradesWidget.setWindowTitle(QCoreApplication.translate("InputGradesWidget", u"Form", None))
        self.label.setText(QCoreApplication.translate("InputGradesWidget", u"Options:", None))
        self.checkBox.setText(QCoreApplication.translate("InputGradesWidget", u"Fill score blanks only", None))
        self.pushButton.setText(QCoreApplication.translate("InputGradesWidget", u"Generate and Save", None))
    # retranslateUi


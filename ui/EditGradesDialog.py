# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'EditGradesDialog.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_EditGradesDialog(object):
    def setupUi(self, EditGradesDialog):
        if not EditGradesDialog.objectName():
            EditGradesDialog.setObjectName(u"EditGradesDialog")
        EditGradesDialog.resize(312, 188)
        self.gridLayout = QGridLayout(EditGradesDialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.pushButton = QPushButton(EditGradesDialog)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout.addWidget(self.pushButton, 4, 1, 1, 1)

        self.label = QLabel(EditGradesDialog)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 3, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 0, 2, 4, 1)

        self.checkBox = QCheckBox(EditGradesDialog)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setChecked(True)

        self.gridLayout.addWidget(self.checkBox, 2, 0, 1, 1)

        self.spinBox = QSpinBox(EditGradesDialog)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setMinimum(-99)
        self.spinBox.setSingleStep(1)
        self.spinBox.setDisplayIntegerBase(10)

        self.gridLayout.addWidget(self.spinBox, 0, 1, 1, 1)


        self.retranslateUi(EditGradesDialog)

        QMetaObject.connectSlotsByName(EditGradesDialog)
    # setupUi

    def retranslateUi(self, EditGradesDialog):
        EditGradesDialog.setWindowTitle(QCoreApplication.translate("EditGradesDialog", u"Dialog", None))
        self.pushButton.setText(QCoreApplication.translate("EditGradesDialog", u"Generate", None))
        self.label.setText(QCoreApplication.translate("EditGradesDialog", u"Increase/decrease grade offset", None))
        self.checkBox.setText(QCoreApplication.translate("EditGradesDialog", u"Overwrite all", None))
    # retranslateUi


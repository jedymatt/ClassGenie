# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AboutDialog.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_AboutDialog(object):
    def setupUi(self, AboutDialog):
        if not AboutDialog.objectName():
            AboutDialog.setObjectName(u"AboutDialog")
        AboutDialog.resize(270, 207)
        self.verticalLayout = QVBoxLayout(AboutDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.appLabel = QLabel(AboutDialog)
        self.appLabel.setObjectName(u"appLabel")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.appLabel.sizePolicy().hasHeightForWidth())
        self.appLabel.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(28)
        self.appLabel.setFont(font)

        self.verticalLayout.addWidget(self.appLabel)

        self.versionLabel = QLabel(AboutDialog)
        self.versionLabel.setObjectName(u"versionLabel")

        self.verticalLayout.addWidget(self.versionLabel)

        self.labelAuthor = QLabel(AboutDialog)
        self.labelAuthor.setObjectName(u"labelAuthor")

        self.verticalLayout.addWidget(self.labelAuthor, 0, Qt.AlignRight)


        self.retranslateUi(AboutDialog)

        QMetaObject.connectSlotsByName(AboutDialog)
    # setupUi

    def retranslateUi(self, AboutDialog):
        AboutDialog.setWindowTitle(QCoreApplication.translate("AboutDialog", u"About", None))
        self.appLabel.setText(QCoreApplication.translate("AboutDialog", u"<html><head/><body><p align=\"center\">Class Genie</p></body></html>", None))
        self.versionLabel.setText(QCoreApplication.translate("AboutDialog", u"versionLabel", None))
        self.labelAuthor.setText(QCoreApplication.translate("AboutDialog", u"AuthorLabel", None))
    # retranslateUi


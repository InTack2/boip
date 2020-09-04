# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\takum\Documents\mayaqt-generator\boip\gui\sample_gui.ui',
# licensing of 'c:\Users\takum\Documents\mayaqt-generator\boip\gui\sample_gui.ui' applies.
#
# Created: Thu Sep  3 23:23:06 2020
#      by: pyside2-uic  running on PySide2 5.12.5
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets


class Ui_SampleWindowUI(object):
    def setupUi(self, SampleWindowUI):
        SampleWindowUI.setObjectName("SampleWindowUI")
        SampleWindowUI.resize(265, 168)
        self.centralwidget = QtWidgets.QWidget(SampleWindowUI)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.printSelectedObjectNameButton = QtWidgets.QPushButton(self.centralwidget)
        self.printSelectedObjectNameButton.setObjectName("printSelectedObjectNameButton")
        self.gridLayout.addWidget(self.printSelectedObjectNameButton, 2, 0, 1, 1)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 1, 0, 1, 1)
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout.addWidget(self.textBrowser, 0, 0, 1, 1)
        SampleWindowUI.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(SampleWindowUI)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 265, 21))
        self.menubar.setObjectName("menubar")
        SampleWindowUI.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(SampleWindowUI)
        self.statusbar.setObjectName("statusbar")
        SampleWindowUI.setStatusBar(self.statusbar)

        self.retranslateUi(SampleWindowUI)
        QtCore.QMetaObject.connectSlotsByName(SampleWindowUI)

    def retranslateUi(self, SampleWindowUI):
        SampleWindowUI.setWindowTitle(QtWidgets.QApplication.translate("SampleWindowUI", "SampleWindow", None, -1))
        self.printSelectedObjectNameButton.setText(QtWidgets.QApplication.translate("SampleWindowUI", "Output the selected object name.", None, -1))
        self.textBrowser.setHtml(QtWidgets.QApplication.translate("SampleWindowUI", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                                  "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                                  "p, li { white-space: pre-wrap; }\n"
                                                                  "</style></head><body style=\" font-family:\'MS UI Gothic\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                                                  "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Thanks for installing Boip!</p></body></html>", None, -1))

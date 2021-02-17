# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(650, 575)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(640, 480))
        MainWindow.setMaximumSize(QtCore.QSize(800, 600))
        MainWindow.setBaseSize(QtCore.QSize(640, 480))
        MainWindow.setAutoFillBackground(True)
        MainWindow.setStyleSheet("")
        MainWindow.setUnifiedTitleAndToolBarOnMac(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.plainTextEdit = DropArea(self.centralwidget)
        self.plainTextEdit.setLineWrapMode(QtWidgets.QPlainTextEdit.NoWrap)
        self.plainTextEdit.setReadOnly(True)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.verticalLayout_2.addWidget(self.plainTextEdit)
        self.widget_3 = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy)
        self.widget_3.setStyleSheet("\n"
"background-color: white;\n"
"color: black;")
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget_3)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.checkBoxAutoProcess = QtWidgets.QCheckBox(self.widget_3)
        self.checkBoxAutoProcess.setObjectName("checkBoxAutoProcess")
        self.verticalLayout_4.addWidget(self.checkBoxAutoProcess)
        self.pushButtonDownloadDir = QtWidgets.QPushButton(self.widget_3)
        self.pushButtonDownloadDir.setEnabled(True)
        self.pushButtonDownloadDir.setObjectName("pushButtonDownloadDir")
        self.verticalLayout_4.addWidget(self.pushButtonDownloadDir)
        self.verticalLayout_2.addWidget(self.widget_3)
        self.processButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.processButton.sizePolicy().hasHeightForWidth())
        self.processButton.setSizePolicy(sizePolicy)
        self.processButton.setMinimumSize(QtCore.QSize(0, 95))
        self.processButton.setBaseSize(QtCore.QSize(0, 32))
        self.processButton.setAutoFillBackground(False)
        self.processButton.setStyleSheet("border-color: rgb(0, 0, 0);")
        self.processButton.setAutoDefault(False)
        self.processButton.setDefault(True)
        self.processButton.setObjectName("processButton")
        self.verticalLayout_2.addWidget(self.processButton)
        self.gridLayout_2.addLayout(self.verticalLayout_2, 0, 1, 1, 1)
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setAutoFillBackground(False)
        self.progressBar.setStyleSheet("padding: 3px;")
        self.progressBar.setProperty("value", 0)
        self.progressBar.setTextVisible(False)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout_2.addWidget(self.progressBar, 1, 0, 1, 2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setAcceptDrops(False)
        self.textBrowser.setAutoFillBackground(True)
        self.textBrowser.setStyleSheet("padding: 3px ")
        self.textBrowser.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.textBrowser.setOpenExternalLinks(True)
        self.textBrowser.setOpenLinks(True)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout.addWidget(self.textBrowser)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setMinimumSize(QtCore.QSize(0, 22))
        self.widget.setBaseSize(QtCore.QSize(0, 0))
        self.widget.setAutoFillBackground(False)
        self.widget.setStyleSheet("\n"
"background-color: white;\n"
"color: black;")
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setObjectName("gridLayout")
        self.widget_2 = QtWidgets.QWidget(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.widget_2.setStyleSheet("background-color: white;\n"
"color: black;")
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.checkBoxConvert = QtWidgets.QCheckBox(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBoxConvert.sizePolicy().hasHeightForWidth())
        self.checkBoxConvert.setSizePolicy(sizePolicy)
        self.checkBoxConvert.setAutoFillBackground(False)
        self.checkBoxConvert.setChecked(True)
        self.checkBoxConvert.setObjectName("checkBoxConvert")
        self.verticalLayout_3.addWidget(self.checkBoxConvert)
        self.checkBoxRename = QtWidgets.QCheckBox(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBoxRename.sizePolicy().hasHeightForWidth())
        self.checkBoxRename.setSizePolicy(sizePolicy)
        self.checkBoxRename.setObjectName("checkBoxRename")
        self.verticalLayout_3.addWidget(self.checkBoxRename)
        self.gridLayout.addWidget(self.widget_2, 1, 0, 1, 1)
        self.comboBoxPlatform = QtWidgets.QComboBox(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBoxPlatform.sizePolicy().hasHeightForWidth())
        self.comboBoxPlatform.setSizePolicy(sizePolicy)
        self.comboBoxPlatform.setStyleSheet("text-align: right;\n"
"padding: 2px;\n"
"color: black;\n"
"background-color: white;")
        self.comboBoxPlatform.setObjectName("comboBoxPlatform")
        self.comboBoxPlatform.addItem("")
        self.comboBoxPlatform.addItem("")
        self.gridLayout.addWidget(self.comboBoxPlatform, 1, 1, 2, 1)
        self.verticalLayout.addWidget(self.widget)
        self.lineEditTarget = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditTarget.setEnabled(True)
        self.lineEditTarget.setAcceptDrops(False)
        self.lineEditTarget.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.lineEditTarget.setStyleSheet("padding: 3px ; margin-left: 2px; margin-right: 2px;")
        self.lineEditTarget.setFrame(False)
        self.lineEditTarget.setCursorPosition(0)
        self.lineEditTarget.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.lineEditTarget.setReadOnly(True)
        self.lineEditTarget.setObjectName("lineEditTarget")
        self.verticalLayout.addWidget(self.lineEditTarget)
        self.pushButtonSelectTarget = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonSelectTarget.sizePolicy().hasHeightForWidth())
        self.pushButtonSelectTarget.setSizePolicy(sizePolicy)
        self.pushButtonSelectTarget.setAutoFillBackground(False)
        self.pushButtonSelectTarget.setStyleSheet("border-color: rgb(0, 0, 0);")
        self.pushButtonSelectTarget.setObjectName("pushButtonSelectTarget")
        self.verticalLayout.addWidget(self.pushButtonSelectTarget)
        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 650, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Rocksmith 2014 CDLC convert pc/mac"))
        self.plainTextEdit.setPlaceholderText(_translate("MainWindow", "DROP FILES HERE"))
        self.checkBoxAutoProcess.setText(_translate("MainWindow", "Auto-process"))
        self.pushButtonDownloadDir.setText(_translate("MainWindow", "Set auto-process folder"))
        self.processButton.setText(_translate("MainWindow", "Process 0 files"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Convert and/or rename CDLC files</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Example:</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Really_Long_Artist_Name-ThisIsJustATribute_p.psarc</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">-&gt; ReallyLong-ThisIsJust_m.psarc</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Original files remain as they are, new files are created to target folder. If target file exists, processing is skipped.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">If auto-process is selected, the app will check specified folder and execute processing without further user interaction. Auto-processing is also applied  when files are manually dropped to app.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"https://github.com/glebb/rocksmithconvert\"><span style=\" text-decoration: underline; color:#0068da;\">Github page</span></a></p></body></html>"))
        self.checkBoxConvert.setText(_translate("MainWindow", "Convert"))
        self.checkBoxRename.setText(_translate("MainWindow", "Rename"))
        self.comboBoxPlatform.setItemText(0, _translate("MainWindow", "MAC"))
        self.comboBoxPlatform.setItemText(1, _translate("MainWindow", "PC"))
        self.lineEditTarget.setPlaceholderText(_translate("MainWindow", "target folder"))
        self.pushButtonSelectTarget.setText(_translate("MainWindow", "Select target folder"))
from droparea import DropArea
import resources_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
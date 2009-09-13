# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DeviceTemplate.ui'
#
# Created: Sun Sep 13 10:24:12 2009
#      by: PyQt4 UI code generator 4.5.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(779, 197)
        self.gridLayout = QtGui.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtGui.QLabel(Form)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.view = QtGui.QGraphicsView(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.view.sizePolicy().hasHeightForWidth())
        self.view.setSizePolicy(sizePolicy)
        self.view.setObjectName("view")
        self.gridLayout.addWidget(self.view, 0, 2, 6, 1)
        self.calibrationList = QtGui.QTableWidget(Form)
        self.calibrationList.setObjectName("calibrationList")
        self.calibrationList.setColumnCount(5)
        self.calibrationList.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.calibrationList.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.calibrationList.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.calibrationList.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.calibrationList.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.calibrationList.setHorizontalHeaderItem(4, item)
        self.gridLayout.addWidget(self.calibrationList, 1, 0, 1, 2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.cameraCombo = QtGui.QComboBox(Form)
        self.cameraCombo.setObjectName("cameraCombo")
        self.horizontalLayout.addWidget(self.cameraCombo)
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.laserCombo = QtGui.QComboBox(Form)
        self.laserCombo.setObjectName("laserCombo")
        self.horizontalLayout.addWidget(self.laserCombo)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 2)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.calibrateBtn = QtGui.QPushButton(Form)
        self.calibrateBtn.setObjectName("calibrateBtn")
        self.horizontalLayout_2.addWidget(self.calibrateBtn)
        self.testBtn = QtGui.QPushButton(Form)
        self.testBtn.setObjectName("testBtn")
        self.horizontalLayout_2.addWidget(self.testBtn)
        self.deleteBtn = QtGui.QPushButton(Form)
        self.deleteBtn.setObjectName("deleteBtn")
        self.horizontalLayout_2.addWidget(self.deleteBtn)
        self.gridLayout.addLayout(self.horizontalLayout_2, 3, 0, 2, 2)
        self.resultLabel = QtGui.QLabel(Form)
        self.resultLabel.setObjectName("resultLabel")
        self.gridLayout.addWidget(self.resultLabel, 4, 1, 1, 1)
        self.accuracyLabel = QtGui.QLabel(Form)
        self.accuracyLabel.setObjectName("accuracyLabel")
        self.gridLayout.addWidget(self.accuracyLabel, 5, 0, 1, 2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Form", "Calibrations:", None, QtGui.QApplication.UnicodeUTF8))
        self.calibrationList.horizontalHeaderItem(0).setText(QtGui.QApplication.translate("Form", "Camera", None, QtGui.QApplication.UnicodeUTF8))
        self.calibrationList.horizontalHeaderItem(1).setText(QtGui.QApplication.translate("Form", "Objective", None, QtGui.QApplication.UnicodeUTF8))
        self.calibrationList.horizontalHeaderItem(2).setText(QtGui.QApplication.translate("Form", "Laser", None, QtGui.QApplication.UnicodeUTF8))
        self.calibrationList.horizontalHeaderItem(3).setText(QtGui.QApplication.translate("Form", "Spot", None, QtGui.QApplication.UnicodeUTF8))
        self.calibrationList.horizontalHeaderItem(4).setText(QtGui.QApplication.translate("Form", "Date", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Form", "Camera:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Form", "Laser:", None, QtGui.QApplication.UnicodeUTF8))
        self.calibrateBtn.setText(QtGui.QApplication.translate("Form", "Calibrate", None, QtGui.QApplication.UnicodeUTF8))
        self.testBtn.setText(QtGui.QApplication.translate("Form", "Test", None, QtGui.QApplication.UnicodeUTF8))
        self.deleteBtn.setText(QtGui.QApplication.translate("Form", "Delete", None, QtGui.QApplication.UnicodeUTF8))
        self.accuracyLabel.setText(QtGui.QApplication.translate("Form", "Accuracy:", None, QtGui.QApplication.UnicodeUTF8))

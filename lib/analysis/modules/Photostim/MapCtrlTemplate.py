# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MapCtrlTemplate.ui'
#
# Created: Wed Mar  2 19:23:19 2011
#      by: PyQt4 UI code generator 4.7.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(397, 371)
        self.gridLayout = QtGui.QGridLayout(Form)
        self.gridLayout.setMargin(0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox = QtGui.QGroupBox(Form)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox)
        self.gridLayout_2.setMargin(0)
        self.gridLayout_2.setVerticalSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.scanTree = TreeWidget(self.groupBox)
        self.scanTree.setHeaderHidden(False)
        self.scanTree.setObjectName("scanTree")
        self.gridLayout_2.addWidget(self.scanTree, 0, 0, 1, 3)
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)
        self.clearDBScanBtn = FeedbackButton(self.groupBox)
        self.clearDBScanBtn.setObjectName("clearDBScanBtn")
        self.gridLayout_2.addWidget(self.clearDBScanBtn, 1, 1, 1, 1)
        self.storeDBScanBtn = FeedbackButton(self.groupBox)
        self.storeDBScanBtn.setObjectName("storeDBScanBtn")
        self.gridLayout_2.addWidget(self.storeDBScanBtn, 1, 2, 1, 1)
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 2, 0, 1, 1)
        self.clearDBSpotBtn = FeedbackButton(self.groupBox)
        self.clearDBSpotBtn.setObjectName("clearDBSpotBtn")
        self.gridLayout_2.addWidget(self.clearDBSpotBtn, 2, 1, 1, 1)
        self.storeDBSpotBtn = FeedbackButton(self.groupBox)
        self.storeDBSpotBtn.setObjectName("storeDBSpotBtn")
        self.gridLayout_2.addWidget(self.storeDBSpotBtn, 2, 2, 1, 1)
        self.gridLayout.addWidget(self.groupBox, 2, 0, 1, 3)
        self.groupBox_2 = QtGui.QGroupBox(Form)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_3 = QtGui.QGridLayout(self.groupBox_2)
        self.gridLayout_3.setMargin(0)
        self.gridLayout_3.setVerticalSpacing(0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.mapTable = QtGui.QTreeWidget(self.groupBox_2)
        self.mapTable.setObjectName("mapTable")
        self.gridLayout_3.addWidget(self.mapTable, 0, 0, 1, 3)
        self.newMapBtn = FeedbackButton(self.groupBox_2)
        self.newMapBtn.setObjectName("newMapBtn")
        self.gridLayout_3.addWidget(self.newMapBtn, 1, 0, 1, 1)
        self.loadMapBtn = FeedbackButton(self.groupBox_2)
        self.loadMapBtn.setObjectName("loadMapBtn")
        self.gridLayout_3.addWidget(self.loadMapBtn, 1, 1, 1, 1)
        self.delMapBtn = FeedbackButton(self.groupBox_2)
        self.delMapBtn.setObjectName("delMapBtn")
        self.gridLayout_3.addWidget(self.delMapBtn, 1, 2, 1, 1)
        self.addScanBtn = FeedbackButton(self.groupBox_2)
        self.addScanBtn.setObjectName("addScanBtn")
        self.gridLayout_3.addWidget(self.addScanBtn, 2, 0, 1, 1)
        self.removeScanBtn = FeedbackButton(self.groupBox_2)
        self.removeScanBtn.setObjectName("removeScanBtn")
        self.gridLayout_3.addWidget(self.removeScanBtn, 2, 1, 1, 1)
        self.gridLayout.addWidget(self.groupBox_2, 3, 0, 1, 3)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("Form", "Scans Loaded", None, QtGui.QApplication.UnicodeUTF8))
        self.scanTree.headerItem().setText(0, QtGui.QApplication.translate("Form", "Scan", None, QtGui.QApplication.UnicodeUTF8))
        self.scanTree.headerItem().setText(1, QtGui.QApplication.translate("Form", "Stored", None, QtGui.QApplication.UnicodeUTF8))
        self.scanTree.headerItem().setText(2, QtGui.QApplication.translate("Form", "Display", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Form", "Selected Scan:", None, QtGui.QApplication.UnicodeUTF8))
        self.clearDBScanBtn.setText(QtGui.QApplication.translate("Form", "Clear DB Entry", None, QtGui.QApplication.UnicodeUTF8))
        self.storeDBScanBtn.setText(QtGui.QApplication.translate("Form", "Store to DB", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Form", "Selected Spot:", None, QtGui.QApplication.UnicodeUTF8))
        self.clearDBSpotBtn.setText(QtGui.QApplication.translate("Form", "Clear DB Entry", None, QtGui.QApplication.UnicodeUTF8))
        self.storeDBSpotBtn.setText(QtGui.QApplication.translate("Form", "Store to DB", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("Form", "Maps", None, QtGui.QApplication.UnicodeUTF8))
        self.mapTable.headerItem().setText(0, QtGui.QApplication.translate("Form", "Map/Scan", None, QtGui.QApplication.UnicodeUTF8))
        self.newMapBtn.setText(QtGui.QApplication.translate("Form", "New Map", None, QtGui.QApplication.UnicodeUTF8))
        self.loadMapBtn.setText(QtGui.QApplication.translate("Form", "Load Selected", None, QtGui.QApplication.UnicodeUTF8))
        self.delMapBtn.setText(QtGui.QApplication.translate("Form", "Delete", None, QtGui.QApplication.UnicodeUTF8))
        self.addScanBtn.setText(QtGui.QApplication.translate("Form", "Add Scan", None, QtGui.QApplication.UnicodeUTF8))
        self.removeScanBtn.setText(QtGui.QApplication.translate("Form", "Remove Scan", None, QtGui.QApplication.UnicodeUTF8))

from FeedbackButton import FeedbackButton
from TreeWidget import TreeWidget
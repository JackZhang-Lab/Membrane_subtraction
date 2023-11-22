# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'radon_gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(553, 342)
        self.splitter = QtWidgets.QSplitter(Form)
        self.splitter.setGeometry(QtCore.QRect(40, 0, 475, 331))
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.splitter)
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.horizontalLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.mrcPathLineEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.mrcPathLineEdit.setObjectName("mrcPathLineEdit")
        self.gridLayout.addWidget(self.mrcPathLineEdit, 0, 1, 1, 1)
        self.browseButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.browseButton.setObjectName("browseButton")
        self.gridLayout.addWidget(self.browseButton, 0, 2, 1, 1)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.splitter)
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.sectionSpinBox = QtWidgets.QSpinBox(self.horizontalLayoutWidget_2)
        self.sectionSpinBox.setObjectName("sectionSpinBox")
        self.horizontalLayout_2.addWidget(self.sectionSpinBox)
        self.previewButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.previewButton.setObjectName("previewButton")
        self.horizontalLayout_2.addWidget(self.previewButton)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.splitter)
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.cropRateLineEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget_3)
        self.cropRateLineEdit.setObjectName("cropRateLineEdit")
        self.horizontalLayout_3.addWidget(self.cropRateLineEdit)
        self.label_4 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.thrLineEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget_3)
        self.thrLineEdit.setObjectName("thrLineEdit")
        self.horizontalLayout_3.addWidget(self.thrLineEdit)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.splitter)
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_7 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout.addWidget(self.label_7)
        self.theta_start_lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.theta_start_lineEdit.setObjectName("theta_start_lineEdit")
        self.horizontalLayout.addWidget(self.theta_start_lineEdit)
        self.label_8 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout.addWidget(self.label_8)
        self.theta_end_lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.theta_end_lineEdit.setObjectName("theta_end_lineEdit")
        self.horizontalLayout.addWidget(self.theta_end_lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.analyzeButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.analyzeButton.setObjectName("analyzeButton")
        self.verticalLayout.addWidget(self.analyzeButton)
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_4.addWidget(self.label_6)
        self.jsonPathLineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.jsonPathLineEdit.setObjectName("jsonPathLineEdit")
        self.horizontalLayout_4.addWidget(self.jsonPathLineEdit)
        self.jsonBrowseButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.jsonBrowseButton.setObjectName("jsonBrowseButton")
        self.horizontalLayout_4.addWidget(self.jsonBrowseButton)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.saveButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.saveButton.setObjectName("saveButton")
        self.verticalLayout.addWidget(self.saveButton)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Radon Analyser - Radonfit - MemXTerminator"))
        self.label.setText(_translate("Form", "2D Average mrc"))
        self.browseButton.setText(_translate("Form", "Browse..."))
        self.label_2.setText(_translate("Form", "Section"))
        self.previewButton.setText(_translate("Form", "Preview this section"))
        self.label_3.setText(_translate("Form", "Crop Rate"))
        self.cropRateLineEdit.setText(_translate("Form", "0.6"))
        self.label_4.setText(_translate("Form", "Threshold"))
        self.thrLineEdit.setText(_translate("Form", "0.7"))
        self.label_7.setText(_translate("Form", "Theta start (deg)"))
        self.theta_start_lineEdit.setText(_translate("Form", "0"))
        self.label_8.setText(_translate("Form", "Theta end (deg)"))
        self.theta_end_lineEdit.setText(_translate("Form", "180"))
        self.analyzeButton.setText(_translate("Form", "START Radon Analysis !"))
        self.label_5.setText(_translate("Form", "If you find params above are suitable, select PATH and press SAVE:"))
        self.label_6.setText(_translate("Form", "JSON file save path"))
        self.jsonBrowseButton.setText(_translate("Form", "Browse..."))
        self.saveButton.setText(_translate("Form", "SAVE these parameters !"))
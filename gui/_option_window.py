# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '_option_window.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(445, 356)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Apply|QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok|QtWidgets.QDialogButtonBox.RestoreDefaults)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 3, 0, 1, 1)
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setObjectName("tabWidget")
        self.tabWidgetPage0 = QtWidgets.QWidget()
        self.tabWidgetPage0.setObjectName("tabWidgetPage0")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tabWidgetPage0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.groupBox_2 = QtWidgets.QGroupBox(self.tabWidgetPage0)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.destFolderEdit = QtWidgets.QLineEdit(self.groupBox_2)
        self.destFolderEdit.setObjectName("destFolderEdit")
        self.horizontalLayout.addWidget(self.destFolderEdit)
        self.findFolderBtn = QtWidgets.QPushButton(self.groupBox_2)
        self.findFolderBtn.setObjectName("findFolderBtn")
        self.horizontalLayout.addWidget(self.findFolderBtn)
        self.gridLayout_3.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.dir_per_page = QtWidgets.QCheckBox(self.groupBox_2)
        self.dir_per_page.setObjectName("dir_per_page")
        self.gridLayout_3.addWidget(self.dir_per_page, 1, 0, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_3, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox_2, 0, 0, 1, 1)
        self.groupBox_3 = QtWidgets.QGroupBox(self.tabWidgetPage0)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.gridLayout_7 = QtWidgets.QGridLayout()
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.label_7 = QtWidgets.QLabel(self.groupBox_3)
        self.label_7.setObjectName("label_7")
        self.gridLayout_7.addWidget(self.label_7, 3, 0, 1, 1)
        self.down_block = QtWidgets.QSpinBox(self.groupBox_3)
        self.down_block.setMinimum(1)
        self.down_block.setMaximum(1000000)
        self.down_block.setProperty("value", 1024)
        self.down_block.setObjectName("down_block")
        self.gridLayout_7.addWidget(self.down_block, 1, 3, 1, 1)
        self.timeout = QtWidgets.QSpinBox(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.timeout.sizePolicy().hasHeightForWidth())
        self.timeout.setSizePolicy(sizePolicy)
        self.timeout.setMinimumSize(QtCore.QSize(100, 0))
        self.timeout.setMinimum(0)
        self.timeout.setMaximum(100)
        self.timeout.setProperty("value", 10)
        self.timeout.setObjectName("timeout")
        self.gridLayout_7.addWidget(self.timeout, 0, 3, 1, 1)
        self.label = QtWidgets.QLabel(self.groupBox_3)
        self.label.setObjectName("label")
        self.gridLayout_7.addWidget(self.label, 0, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.groupBox_3)
        self.label_6.setObjectName("label_6")
        self.gridLayout_7.addWidget(self.label_6, 2, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_7.addItem(spacerItem, 2, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_7.addItem(spacerItem1, 1, 2, 1, 1)
        self.gui_interval = QtWidgets.QDoubleSpinBox(self.groupBox_3)
        self.gui_interval.setSuffix("")
        self.gui_interval.setDecimals(1)
        self.gui_interval.setMinimum(0.1)
        self.gui_interval.setProperty("value", 0.1)
        self.gui_interval.setObjectName("gui_interval")
        self.gridLayout_7.addWidget(self.gui_interval, 2, 3, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.groupBox_3)
        self.label_5.setObjectName("label_5")
        self.gridLayout_7.addWidget(self.label_5, 1, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox_3)
        self.label_2.setObjectName("label_2")
        self.gridLayout_7.addWidget(self.label_2, 1, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_7.addItem(spacerItem2, 0, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox_3)
        self.label_3.setObjectName("label_3")
        self.gridLayout_7.addWidget(self.label_3, 2, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.groupBox_3)
        self.label_4.setObjectName("label_4")
        self.gridLayout_7.addWidget(self.label_4, 0, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.groupBox_3)
        self.label_8.setObjectName("label_8")
        self.gridLayout_7.addWidget(self.label_8, 3, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_7.addItem(spacerItem3, 3, 2, 1, 1)
        self.threadnum = QtWidgets.QSpinBox(self.groupBox_3)
        self.threadnum.setEnabled(False)
        self.threadnum.setMinimum(1)
        self.threadnum.setMaximum(10)
        self.threadnum.setProperty("value", 2)
        self.threadnum.setObjectName("threadnum")
        self.gridLayout_7.addWidget(self.threadnum, 3, 3, 1, 1)
        self.gridLayout_8.addLayout(self.gridLayout_7, 0, 0, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_8.addItem(spacerItem4, 0, 1, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox_3, 1, 0, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem5, 2, 0, 1, 1)
        self.tabWidget.addTab(self.tabWidgetPage0, "")
        self.tabWidgetPage1 = QtWidgets.QWidget()
        self.tabWidgetPage1.setObjectName("tabWidgetPage1")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.tabWidgetPage1)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.groupBox = QtWidgets.QGroupBox(self.tabWidgetPage1)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.filter_add = QtWidgets.QToolButton(self.groupBox)
        self.filter_add.setObjectName("filter_add")
        self.verticalLayout.addWidget(self.filter_add)
        self.filter_substract = QtWidgets.QToolButton(self.groupBox)
        self.filter_substract.setObjectName("filter_substract")
        self.verticalLayout.addWidget(self.filter_substract)
        self.filter_reset = QtWidgets.QToolButton(self.groupBox)
        self.filter_reset.setObjectName("filter_reset")
        self.verticalLayout.addWidget(self.filter_reset)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem6)
        self.gridLayout_5.addLayout(self.verticalLayout, 0, 1, 1, 1)
        self.filter_list = QtWidgets.QListWidget(self.groupBox)
        self.filter_list.setObjectName("filter_list")
        self.gridLayout_5.addWidget(self.filter_list, 0, 0, 1, 1)
        self.gridLayout_6.addWidget(self.groupBox, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tabWidgetPage1, "")
        self.gridLayout.addWidget(self.tabWidget, 1, 0, 1, 1)

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "설정"))
        self.groupBox_2.setTitle(_translate("Dialog", "다운로드 폴더"))
        self.findFolderBtn.setText(_translate("Dialog", "폴더 찾기"))
        self.dir_per_page.setText(_translate("Dialog", "사이트 별로 폴더 생성"))
        self.groupBox_3.setTitle(_translate("Dialog", "상세 설정"))
        self.label_7.setText(_translate("Dialog", "동시 다운로드"))
        self.label.setText(_translate("Dialog", "타임아웃"))
        self.label_6.setText(_translate("Dialog", "(기본값: 0.1)"))
        self.label_5.setText(_translate("Dialog", "(기본값: 1024)"))
        self.label_2.setText(_translate("Dialog", "다운로드 블록 크기"))
        self.label_3.setText(_translate("Dialog", "GUI 업데이트 주기"))
        self.label_4.setText(_translate("Dialog", "(기본값: 10)"))
        self.label_8.setText(_translate("Dialog", "(기본값: 2)"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabWidgetPage0), _translate("Dialog", "다운로드 설정 "))
        self.groupBox.setTitle(_translate("Dialog", "제목 필터"))
        self.filter_add.setToolTip(_translate("Dialog", "키워드 추가"))
        self.filter_add.setText(_translate("Dialog", "+"))
        self.filter_substract.setToolTip(_translate("Dialog", "키워드 삭제"))
        self.filter_substract.setText(_translate("Dialog", "-"))
        self.filter_reset.setToolTip(_translate("Dialog", "키워드 전부 삭제"))
        self.filter_reset.setText(_translate("Dialog", "x"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabWidgetPage1), _translate("Dialog", "키워드 필터"))


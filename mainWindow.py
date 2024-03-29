
from PyQt5 import QtCore, QtGui, QtWidgets


self.centralwidget = QtWidgets.QWidget(MainWindow)
self.centralwidget.setObjectName("centralwidget")
self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
self.gridLayout_3.setObjectName("gridLayout_3")
self.frame_4 = QtWidgets.QFrame(self.centralwidget)
sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
sizePolicy.setHorizontalStretch(5)
sizePolicy.setVerticalStretch(0)
sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
self.frame_4.setSizePolicy(sizePolicy)
self.frame_4.setFrameShape(QtWidgets.QFrame.Box)
self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
self.frame_4.setObjectName("frame_4")
self.gridLayout_6 = QtWidgets.QGridLayout(self.frame_4)
self.gridLayout_6.setObjectName("gridLayout_6")
self.frame = QtWidgets.QFrame(self.frame_4)

_translate = QtCore.QCoreApplication.translate
MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
self.pushButton_4.setText(_translate("MainWindow", "初始化"))
self.comboBox.setItemText(0, _translate("MainWindow", "相片"))
self.comboBox.setItemText(1, _translate("MainWindow", "视频"))
self.comboBox.setItemText(2, _translate("MainWindow", "摄像头"))
self.pushButton_3.setText(_translate("MainWindow", "模型初始化thread"))
self.pushButton.setText(_translate("MainWindow", "开始检测"))
self.pushButton_2.setText(_translate("MainWindow", "退出"))

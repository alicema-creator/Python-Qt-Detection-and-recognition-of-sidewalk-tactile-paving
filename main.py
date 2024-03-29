import cv2
import sys
import os
import random
import numpy as np
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
class myWin(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(myWin, self).__init__()
        self.setupUi(self)


        self.pushButton_3.clicked.connect(self.threadRun)
        self.pushButton_2.clicked.connect(self.closeEvent)
        self.pushButton_4.clicked.connect(self.initThread)

    def initThread(self):
        print("initThread")
        threadStop()
        self.pushButton_3.setText("模型初始化thread")
        self.pushButton.setText("开始检测")

    def threadRun(self):
        TEXT=self.comboBox.currentText()
        print("TEXT",TEXT)

        global videoName
        if (TEXT=="相片"):
            print("TEXT2", TEXT)
            videoName, imgType = QFileDialog.getOpenFileName(self, "打开文件", "./images", "files(*.*)")

            # thread1.start()
            if self.pushButton_3.text() == "模型初始化thread":
                threadSetup()
                # thread1.start()
                self.pushButton_3.setText("暂停模型thread")

            elif self.pushButton_3.text() == "暂停模型thread":
                # stop_thread(thread1)
                # stop_thread(threadT)
                threadSuspend()
                print("tttt6")
                self.pushButton_3.setText("模型恢复thread")
            elif self.pushButton_3.text() == "模型恢复thread":
                # stop_thread(thread1)
                # stop_thread(threadT)
                threadResume()
                print("tttt6")
                self.pushButton_3.setText("暂停模型thread")

        if (TEXT=="视频"):
            print("TEXT2", TEXT)
            videoName, imgType = QFileDialog.getOpenFileName(self, "打开文件", "./imagesVideo", "files(*.*)")

            # thread1.start()
            if self.pushButton_3.text() == "模型初始化thread":
                threadSetup()
                # thread1.start()
                self.pushButton_3.setText("暂停模型thread")

            elif self.pushButton_3.text() == "暂停模型thread":
                # stop_thread(thread1)
                # stop_thread(threadT)
                threadSuspend()
                print("tttt6")
                self.pushButton_3.setText("模型恢复thread")
            elif self.pushButton_3.text() == "模型恢复thread":
                # stop_thread(thread1)
                # stop_thread(threadT)
                threadResume()
                print("tttt6")
                self.pushButton_3.setText("暂停模型thread")

        elif (TEXT=="摄像头"):
            print("TEXT3", TEXT)
            videoName="0"

            # thread1.start()
            if self.pushButton_3.text()=="模型初始化thread":
                threadSetup()
                # thread1.start()
                self.pushButton_3.setText("暂停模型thread")

            elif self.pushButton_3.text()=="暂停模型thread":
                #stop_thread(thread1)
                #stop_thread(threadT)
                threadSuspend()
                print("tttt6")
                self.pushButton_3.setText("模型恢复thread")
            elif self.pushButton_3.text()=="模型恢复thread":
                #stop_thread(thread1)
                #stop_thread(threadT)
                threadResume()
                print("tttt6")
                self.pushButton_3.setText("暂停模型thread")

    #closeEvent2暂时不用
    def closeEvent2(self, event):
        self.box = QMessageBox(QMessageBox.Warning, "系统提示信息", "是否暂停摄像头？")
        qyes = self.box.addButton(self.tr("是"), QMessageBox.YesRole)
        qno = self.box.addButton(self.tr("否"), QMessageBox.NoRole)
        self.box.exec_()
        if self.box.clickedButton() == qyes:
            self.label.clear()
            while 1:
                if cv2.waitKey(1) == ord('q'):
                    break
            self.cap.release()
            cv2.destroyAllWindows()
        else:
            event.ignore()

    def closethreed(self):
        print("test")

    # # 退出系统窗口 X 绑定函数事件
    def closeEvent(self, event):
        # print("test")
        self.box = QMessageBox(QMessageBox.Warning, "系统提示信息", "是否退出系统？")
        qyes = self.box.addButton(self.tr("是"), QMessageBox.YesRole)
        qno = self.box.addButton(self.tr("否"), QMessageBox.NoRole)
        self.box.exec_()
        if self.box.clickedButton() == qyes:
            try:
                threadStop()
                self.timer2.stop()
            except:
                print("abnormal")
            event.accept()
            QtWidgets.QWidget.closeEvent(self, event)
            sys.exit().accept()
        else:
            event.ignore()


    def switch_video(self):
        # self.timer2.start()
        if self.pushButton.text()=="开始检测":
            self.timer2.start()
            print("tttt6")
            self.pushButton.setText("暂停检测")
        elif self.pushButton.text()=="暂停检测":
            self.timer2.pause()
            print("tttt6")
            self.pushButton.setText("恢复检测")
        elif self.pushButton.text()=="恢复检测":
            self.timer2.resume()
            print("tttt6")
            self.pushButton.setText("暂停检测")




    def videoRecog2(self):

        #print("im02: ",im02)
        #try是预防两个按钮同时点击变量取不到值
        try:
            frame = cv2.cvtColor(im02, cv2.COLOR_BGR2RGB)
            height, width, bytesPerComponent = frame.shape
            bytesPerLine = bytesPerComponent * width

            self.q_image = QtGui.QImage(frame.data, width, height, bytesPerLine, QtGui.QImage.Format_RGB888) \
                .scaled(self.label.height() * 0.8, self.label.height() * 0.6)
            self.label.setPixmap(QPixmap.fromImage(self.q_image))
            self.update()

        except:
            print("breakdown")


if __name__=="__main__":
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    app=QtWidgets.QApplication(sys.argv)
    Widget=myWin()
    Widget.showMaximized();
    Widget.show()
    sys.exit(app.exec_())


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interfaz.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets,QtChart

#from QtCharts import QChartView


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(918, 653)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color: rgb(138, 174, 225)")
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 60, 231, 81))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 180, 60, 16))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 220, 60, 16))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(30, 260, 101, 16))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(60, 310, 113, 32))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(83, 105, 154);")
        self.pushButton.setObjectName("pushButton")
        self.graphicsView = QtChart.QChartView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(300, 70, 256, 192))
        self.graphicsView.setObjectName("graphicsView")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(130, 180, 61, 16))
        self.label_5.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(130, 220, 61, 16))
        self.label_6.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(130, 260, 60, 16))
        self.label_7.setStyleSheet("background-color: rgb(254, 254, 254);")
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.graphicsView_2 = QtChart.QChartView(self.centralwidget)
        self.graphicsView_2.setGeometry(QtCore.QRect(590, 70, 256, 192))
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.graphicsView_3 = QtChart.QChartView(self.centralwidget)
        self.graphicsView_3.setGeometry(QtCore.QRect(300, 330, 256, 192))
        self.graphicsView_3.setObjectName("graphicsView_3")
        self.graphicsView_4 = QtChart.QChartView(self.centralwidget)
        self.graphicsView_4.setGeometry(QtCore.QRect(590, 330, 256, 192))
        self.graphicsView_4.setObjectName("graphicsView_4")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(210, 180, 60, 16))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(210, 220, 60, 16))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(210, 260, 60, 16))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(10, 10, 791, 16))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(370, 280, 121, 16))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(670, 280, 121, 16))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(370, 540, 141, 16))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(590, 540, 261, 16))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 918, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Sensor BME280"))
        self.label_2.setText(_translate("MainWindow", "Humedad:"))
        self.label_3.setText(_translate("MainWindow", "Presión:"))
        self.label_4.setText(_translate("MainWindow", "Temperatura:"))
        self.pushButton.setText(_translate("MainWindow", "Refresh Data"))
        self.label_8.setText(_translate("MainWindow", "g/m^3"))
        self.label_9.setText(_translate("MainWindow", "MPa"))
        self.label_10.setText(_translate("MainWindow", "ºC"))
        self.label_11.setText(_translate("MainWindow", "Equipo: María Fernanda Mendoza Romero, José Francisco Martínez Morales, Francisco Gonzáles Morales "))
        self.label_12.setText(_translate("MainWindow", "Gráfica. Humedad"))
        self.label_13.setText(_translate("MainWindow", "Gráfica. Presión"))
        self.label_14.setText(_translate("MainWindow", "Gráfica. Temperatura"))
        self.label_15.setText(_translate("MainWindow", "Gráfica Humedad, Presión y  Temperatura"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

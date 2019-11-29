from interfaz_ui import*
from PyQt5 import QtCore, QtGui, QtWidgets,QtChart

import pyqtgraph as pg
#import RPi.GPIO as GPIO
#from time import sleep
#import board
#import busio
#import adafruit_bme280
import psycopg2
#from psycopg2 import Error
#try:
    #i2c = busio.I2C(board.SCL, board.SDA)
    #BME280 = adafruit_bme280.Adafruit_BME280_I2C(i2c)
#except:
    #print("No se encuentra ningún sensor")
    
#GPIO.setmode(GPIO.BCM)
#GPIO.setup(6,GPIO.OUT)

Humedad=0
Presion=0
Temperatura=0
valorinicial=0

humedad=[]
presion=[]
temperatura=[]
tiempo=[]

pen=pg.mkPen(255,0,0)
pen1=pg.mkPen(0,255,0)

class MainWindow(QtWidgets.QMainWindow,Ui_MainWindow):
    global Temperatura, Humedad, Presion
    def __init__(self,args,*kwargs):
        QtWidgets.QMainWindow._init_(self,args,*kwargs)
        self.setupUi(self)
        self.datos()
        self.graphicsView.setBackground('w')
        self.graphicsView_2.setBackground('w')
        self.graphicsView_3.setBackground('w')
        self.graphicsView_4.setBackground('w')
        self.graphicsView_5.setBackground('w')
    def actualizo(self):
        print ("Actualizando")
        self.label.setText("Actualizando Datos del Sensor")
        self.pushButton.setText("lo actualizaste")
    def valores(self):
        global Temperatura, Humedad, Presion
        self.label_5.setText("value", Humedad)
        self.label_6.setText("value", Presion)
        self.label_7.setText("value", Temperatura)
    
    def actualizar(self):
        global Humedad,Presion,Temperatura,humedad,presion,temperatura
        
        sensor()
        self.graphicsView.QtChart.QChartView(tiempo,humedad)
        self.graphicsView_2.QtChart.QChartView(tiempo,presion, pen=pen)
        self.graphicsView_3.QtChart.QChartView(tiempo,temperatura,pen=pen1)
        self.graphicsView_4.QtChart.QChartView(tiempo,humedad)
        self.graphicsView_4.QtChart.QChartView(tiempo,presion, pen=pen)
        self.graphicsView_4.QtChart.QChartView(tiempo,temperatura,pen=pen1)
        
def sensor():
        global Humedad,Presion,Temperatura,humedad,presion,temperatura,tiempo,valorinicial
        try:
        
            Humedad=bme280.humidity
            Presion=bme280.pressure
            Temperatura=bme280.temperature
            
           
            humedad.append(Humedad)
            presion.append(Presion)
            temperatura.append(Temperatura)
             
            tiempo.append(valorinicial)
            valorinicial+=1


def Database():
    global Humedad,Presion,Temperatura
    try:
        connection=psycopg2.connect(user="pi", password="raspberry",host="127.0.0.1",port="5432",database="pi")
        cursor=connection.cursor()
        try:
            createTableQuery='''Create TABLE IF NOT EXISTS SENSORBME280
                (ID SERIAL  PRIMARY KEY,
                HUMEDAD    REAL    NOT NULL,
                PRESION        REAL    NOT NULL,
                TEMPERATURA       REAL    NOT NULL);'''
            cursor.execute(createTableQuery)
            connection.commit()
            print('Table created successfully in PostgresSQL')
        except:
            print('Table already created')
        try:
            
            addTableQuerry="INSERT INTO SENSORBME280 (humedad,presion,temperatura) VALUES (%0.2f,%0.2f,%0.2f,%0.2f);" %(Humedad,Presion,Temperatura)
            print(addTableQuerry)
            cursor.execute(addTableQuerry)
            connection.commit()
        finally:                
            if (connection):
                cursor.close()
                connection.close()

if __name__=="__main__":
    
        app=QtWidgets.QApplication([])
        window = MainWindow()
        window.show()
        app.exec()

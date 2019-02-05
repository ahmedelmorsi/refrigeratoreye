#1 May 2016 Graduation Project 2016
#Features Matrix Extractor
#Nora Basha , Ahmed EL-morsy , Ahmed Al-Badrawy
import sys , time
import cv2
import os
from json import dumps
import numpy as np
from PyQt4 import QtCore, QtGui, QtWebKit, Qt
from PyQt4.QtWebKit import *
from PyQt4.QtCore import QThread
from program_layout import Ui_Form
from sensors import Sensor
from PIL import Image
import datetime
from datetime import date
import sqlite3
from Recognition_Storing import *
import json, ast
import urllib2
from Weight import *
import requests
'''
from iothub_client_transifer import *
import yaml
'''
Key=0
weight=0
class Video():
    def __init__(self,capture):
        self.capture = capture
        self.currentFrame=np.array([])
    def captureNextFrame(self):
        """                           
        capture frame and reverse RBG BGR and return opencv image                                      
        """
        ret, readFrame=self.capture.read()
        if(ret==True):
            self.currentFrame=cv2.cvtColor(readFrame,cv2.COLOR_BGR2RGB)
    def convertFrame(self):
        """     converts frame to format suitable for QtGui            """
        try:
            height,width=self.currentFrame.shape[:2]
            global img
            img=QtGui.QImage(self.currentFrame,width,height,QtGui.QImage.Format_RGB888)
            img=QtGui.QPixmap.fromImage(img)
            self.previousFrame = self.currentFrame
            return img
        except:
            return None
class MyForm(QtGui.QMainWindow):
    def __init__(self, parent =None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        Type = 'Apple'
        global cap
        cap=cv2.VideoCapture(0)
        self.video = Video(cap)
        self._timer = QtCore.QTimer(self)
        self._timer.timeout.connect(self.play)
        self._timer.start(27)
        self.update()
        self.ui.web.setUrl(QtCore.QUrl('http://funcook.com/'))
        self.signalworker = SignalWorker()
        self.signalworker.start()
        #get the signals and connect it with gui update funnctions
        self.connect(self.signalworker,QtCore.SIGNAL("TempSignal"),self.set_temp)
        self.connect(self.signalworker, QtCore.SIGNAL("DistSignal"), self.set_dist)
        QtCore.QObject.connect(self.ui.capture_bt,QtCore.SIGNAL("clicked()"),self.capture)
        QtCore.QObject.connect(self.ui.store_bt,QtCore.SIGNAL("clicked()"),self.store)
        QtCore.QObject.connect(self.ui.update_food,QtCore.SIGNAL("clicked()"),self.set_food)
        QtCore.QObject.connect(self.ui.update_list,QtCore.SIGNAL("clicked()"),self.set_list)
        QtCore.QObject.connect(self.ui.noice,QtCore.SIGNAL("clicked()"),self.no_ice)
        QtCore.QObject.connect(self.ui.toowarm,QtCore.SIGNAL("clicked()"),self.too_warm)
        QtCore.QObject.connect(self.ui.notrun,QtCore.SIGNAL("clicked()"),self.not_run)
        QtCore.QObject.connect(self.ui.toocold,QtCore.SIGNAL("clicked()"),self.too_cold)
    def no_ice(self):
        self.ui.tableWidget.setItem(0, 0, QtGui.QTableWidgetItem("Check no_icethat the power plug is properly connected"))
        self.ui.tableWidget.setItem(0, 1, QtGui.QTableWidgetItem("Make sure that the back of the refrigerator is not near heat source"))
        self.ui.tableWidget.setItem(0, 2, QtGui.QTableWidgetItem("check the refrigerator control box "))
    def too_warm(self):
        self.ui.tableWidget.setItem(0, 0, QtGui.QTableWidgetItem("Check that the power plug is properly connected"))
        self.ui.tableWidget.setItem(0, 1, QtGui.QTableWidgetItem("Make sure that the back of the refrigerator is not near heat source"))
        self.ui.tableWidget.setItem(0, 2, QtGui.QTableWidgetItem("check the refrigerator control box "))
    def not_run(self):
        self.ui.tableWidget.setItem(0, 0, QtGui.QTableWidgetItem("Check not_runthat the power plug is properly connected"))
        self.ui.tableWidget.setItem(0, 1, QtGui.QTableWidgetItem("Make sure that the back of the refrigerator is not near heat source"))
        self.ui.tableWidget.setItem(0, 2, QtGui.QTableWidgetItem("check the refrigerator control box "))
    def too_cold(self):
        self.ui.tableWidget.setItem(0, 0, QtGui.QTableWidgetItem("Check too_coldthat the power plug is properly connected"))
        self.ui.tableWidget.setItem(0, 1, QtGui.QTableWidgetItem("Make sure that the back of the refrigerator is not near heat source"))
        self.ui.tableWidget.setItem(0, 2, QtGui.QTableWidgetItem("check the refrigerator control box "))
    def set_temp(self, temp):
        self.ui.temp_bar.setProperty("value", temp)
        if temp > 200:
            self.ui.tableWidget.setItem(0, 0, QtGui.QTableWidgetItem("Check that the power plug is properly connected"))
            self.ui.tableWidget.setItem(0, 1, QtGui.QTableWidgetItem("Make sure that the back of the refrigerator is not near heat source"))
            self.ui.tableWidget.setItem(0, 2, QtGui.QTableWidgetItem("check the refrigerator control box "))
            '''
        else :
            self.ui.tableWidget.setItem(0, 0, QtGui.QTableWidgetItem(""))
            self.ui.tableWidget.setItem(0, 1, QtGui.QTableWidgetItem(""))
            self.ui.tableWidget.setItem(0, 2, QtGui.QTableWidgetItem(""))
            '''
        self.ui.temp_val.setText(str(temp))
    def set_dist(self, dist):
        self.ui.dist_bar.setProperty("value", dist)
        if dist<0:
            self.ui.tableWidget.setItem(0, 3, QtGui.QTableWidgetItem("Make sure that the back of the refrigerator is not close to the wall"))
            '''
        else :
            self.ui.tableWidget.setItem(0, 3, QtGui.QTableWidgetItem(""))
            '''
        self.ui.dist_val.setText(str(dist))
    def set_food(self):
        r = requests.get('https://refrigeratoreye.azurewebsites.net/tables/foodmanager?zumo-api-version=2.0.0')
        a = r.json()
        b = len(a)
        self.ui.tablefood.setRowCount(b)
        for i in range(0,b):
            c = a[i]
            d = c['Type']
            e = d.encode("utf-8")
            self.ui.tablefood.setItem(i, 0, QtGui.QTableWidgetItem(e))
        for i in range(0,b):
            c = a[i]
            d = c['Quantity']
            e = d.encode("utf-8")
            self.ui.tablefood.setItem(i, 1, QtGui.QTableWidgetItem(e))
        for i in range(0,b):
            c = a[i]
            d = c['Calories']
            e = d.encode("utf-8")
            self.ui.tablefood.setItem(i, 2, QtGui.QTableWidgetItem(e))
        for i in range(0,b):
            c = a[i]
            d = c['Fat']
            e = d.encode("utf-8")
            self.ui.tablefood.setItem(i, 3, QtGui.QTableWidgetItem(e))
        for i in range(0,b):
            c = a[i]
            d = c['Sugar']
            e = d.encode("utf-8")
            self.ui.tablefood.setItem(i, 4, QtGui.QTableWidgetItem(e))
        for i in range(0,b):
            c = a[i]
            d = c['Start_Date']
            e = d.encode("utf-8")
            self.ui.tablefood.setItem(i, 5, QtGui.QTableWidgetItem(e))
        for i in range(0,b):
            c = a[i]
            d = c['End_Date']
            e = d.encode("utf-8")
            self.ui.tablefood.setItem(i, 6, QtGui.QTableWidgetItem(e))
    def set_list(self):
        r = requests.get('https://refrigeratoreye.azurewebsites.net/tables/shoppinglist?zumo-api-version=2.0.0')
        a = r.json()
        b = len(a)
        self.ui.tablelist.setRowCount(b)
        for i in range(0,b):
            c = a[i]
            d = c['Name']
            e = d.encode("utf-8")
            self.ui.tablelist.setItem(i, 0, QtGui.QTableWidgetItem(e))
        for i in range(0,b):
            c = a[i]
            d = c['Quantity']
            e = d.encode("utf-8")
            self.ui.tablelist.setItem(i, 1, QtGui.QTableWidgetItem(e))
        for i in range(0,b):
            c = a[i]
            d = c['Price']
            e = d.encode("utf-8")
            self.ui.tablelist.setItem(i, 2, QtGui.QTableWidgetItem(e))
        self.ui.instock.setItem(0, 0, QtGui.QTableWidgetItem("Awlad Ragab"))
        self.ui.instock.setItem(0, 1, QtGui.QTableWidgetItem("Wekalet elmansoura"))
    def play(self):
        try:
            self.video.captureNextFrame()
            self.ui.videoFrame.setPixmap(
            self.video.convertFrame())
            self.ui.videoFrame.setScaledContents(True)
        except TypeError:
            print "No frame"
    def capture(self):
        self.ui.capture_bt.setText("captureing")
        s,frame=cap.read()
        cv2.imwrite("10.jpg",frame)
        data=gettype()
        body = str.encode(json.dumps(data))
        url = 'https://ussouthcentral.services.azureml.net/workspaces/8c4897812c7345b98c46250d871c923a/services/a8d0d47a1b3e42068ddaf72a71f6a63b/execute?api-version=2.0&details=true'
        api_key = '3bwVzVxmX+tDPbxpCGLXRq0Tw8bbzNRGPkKTKyYHeBaUAqwWXwtuhhr4yp73VWCbvQDeDwnGkx6QdA6xCmNueQ==' # Replace this with the API key for the web service
        headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}
        req = urllib2.Request(url, body, headers)
        response = urllib2.urlopen(req)
        # If you are using Python 3+, replace urllib2 with urllib.request in the above code:
        # req = urllib.request.Request(url, body, headers) 
        # response = urllib.request.urlopen(req)
        result = response.read()
        a = json.loads(result)
        b = a["Results"]["output1"]["value"]["Values"]
        c = b[0][0]
        global Key
        Key = c.encode("utf-8")
        if Key== 'Apple':
           Enddate = date.today()+ datetime.timedelta(days=30)
           sweight=200
        if Key=='Onion':
           Enddate= date.today()+ datetime.timedelta(days=60)
           sweight=80
        if Key=='Tomato':
           Enddate= date.today()+ datetime.timedelta(days=14)
           sweight=150
        try:
            global weight
            weight=getweight()   #get the weight 
        except:
            weight=500
        Quantity=weight/sweight
        self.ui.type_text.setText(Key)  #set Type on GUI
        self.ui.exdate.setDate(Enddate) #set Expiriny Data
        self.ui.Quantity_val.setValue(Quantity)
        self.ui.wight_text.setText(str(weight)) #set the weight on GUI
        self.ui.capture_bt.setText("Capture")
        '''
    except urllib2.HTTPError, error:
        print("The request failed with status code: " + str(error.code))
        #Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
        print(error.info())
        print(json.loads(error.read()))
        '''
    def store(self):
        self.ui.store_bt.setText("storeing")
        deviceid = '"Device1"'
        print Key
        if Key== 'Apple':
           Calories='"52 Calories"'
           Protein='"0.26 g"'
           Fat='"0.17 g"'
           Carbs='"13.81 g"'
           Sugars='"10.39 g"'
           Sodium='"1 mg"'
           Vitamin_C='"8 %"'
        if Key=='Onion':
           Calories='"42 Calories"'
           Protein='"0.92 g"'
           Fat='"0.08 g"'
           Carbs='"10.11 g"'
           Sugars='"4.28 g"'
           Sodium='"3 mg"'
           Vitamin_C='"11 %"'
        if Key=='Tomato':
           Calories='"18 Calories"'
           Protein='"0.88 g"'
           Fat='"0.2 g"'
           Carbs='"3.92 g"'
           Sugars='"2.63 g"'
           Sodium='"5 mg"'
           Vitamin_C='"21 %"'
        Enddate1=self.ui.exdate.date()
        Enddate=Enddate1.toPyDate()
        Quantity=6
        Quantity1=self.ui.Quantity_val.value()
        if self.ui.in_check.isChecked() == True:
            Quantity2 = Quantity1
        if self.ui.out_check.isChecked() == True:
            Quantity2 = -1*Quantity1
        r = requests.get('https://refrigeratoreye.azurewebsites.net/tables/foodmanager?zumo-api-version=2.0.0')
        a = r.json()
        b = len(a)
        for i in range(0,b):
            c = a[i]
            d = c['Type']
            e = d.encode("utf-8")
            if Key==e:
                c = a[i]
                d = c['Quantity']
                e = d.encode("utf-8")
                Quantity= int(e)+Quantity2     
            else :
                Quantity=Quantity2
        print Quantity
        def json_serial(obj):
                """JSON serializer for objects not serializable by default json code"""
                if isinstance(obj, date):
                     serial = obj.isoformat()
                     return serial
                raise TypeError ("Type not serializable")
        Type= dumps(Key, default=json_serial)
        Start_Date= dumps(date.today(), default=json_serial)
        End_Date= dumps(Enddate, default=json_serial)
        MSG_Text = '{ "deviceid": %s , "Type": %s , "Quantity": %s , "Calories" : %s , "Protein": %s , "Fat":%s , "Carbs": %s , "Sugar": %s , "Sodium": %s , "Vitamin_C": %s , "Start_Date": %s , "End_Date": %s }'
        MSG_Text_Formatted = MSG_Text % ( deviceid , Type , Quantity , Calories  , Protein , Fat , Carbs , Sugars , Sodium , Vitamin_C , Start_Date , End_Date)
        print MSG_Text_Formatted
       # import requests
        '''
        for i in range(0,b):
            c = a[i]
            d = c['Type']
            e = d.encode("utf-8")
            if Key==e:
                ID=c['id']
                
                body = json.dumps({
                "id": "901f517f-1100-4808-857c-12e900619d0c" ,
                "Type": "ahmed"
                })
                r = requests.patch('https://refrigeratoreye.azurewebsites.net/tables/foodmanager?zumo-api-version=2.0.0', data=body)
                print r.status_code
            else :
          '''
        r = requests.post('https://refrigeratoreye.azurewebsites.net/tables/foodmanager?zumo-api-version=2.0.0' , data = MSG_Text_Formatted)
        print r.status_code
        self.set_list()
        self.set_food()
        self.ui.store_bt.setText("Store")
        '''
        #iothub_client_sample_run(MSG_Text_Formatted)
        '''
#generate signals to threads 
class SignalWorker(QThread):
    def __init__(self, parent = None):
            QThread.__init__(self, parent)
            self.sensor = Sensor()
    #override function that works to generate values for signals
    def run(self):
            while True:
                    temp = self.sensor.gettemp()
                    dist = self.sensor.getdist()
                    self.emit(QtCore.SIGNAL("TempSignal"), temp)
                    self.emit(QtCore.SIGNAL("DistSignal"), dist)
                    time.sleep(1)
def main():
    app = QtGui.QApplication(sys.argv)
    Form = MyForm()
    Form.show()
    app.exec_()
main()

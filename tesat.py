# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'HueUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIntValidator,QDoubleValidator,QFont
from PyQt5.QtSerialPort import QSerialPort, QSerialPortInfo
import serial
stral=""
class Ui_Form(object):
    def setupUi(self, Form):
       ###TU jest dobre nie ruszać
        Form.setObjectName("QutletHue")
        Form.resize(640, 480)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(640, 480))
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(170, 380, 75, 23))
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setObjectName("pushButton")
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(190, 150, 241, 141))
        self.layoutWidget.setAutoFillBackground(False)
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setMaximumSize(QtCore.QSize(75, 25))
        self.label_2.setAutoFillBackground(False)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setMaximumSize(QtCore.QSize(75, 25))
        self.label.setAutoFillBackground(False)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setMaximumSize(QtCore.QSize(75, 25))
        self.label_3.setAutoFillBackground(False)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setMaximumSize(QtCore.QSize(75, 25))
        self.lineEdit.setAutoFillBackground(False)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_2.addWidget(self.lineEdit)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_2.setSizePolicy(sizePolicy)
        self.lineEdit_2.setMaximumSize(QtCore.QSize(75, 25))
        self.lineEdit_2.setAutoFillBackground(False)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_2.addWidget(self.lineEdit_2)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_3.setMaximumSize(QtCore.QSize(75, 25))
        self.lineEdit_3.setAutoFillBackground(False)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.horizontalLayout_2.addWidget(self.lineEdit_3)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setMaximumSize(QtCore.QSize(75, 25))
        self.label_4.setAutoFillBackground(False)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        self.label_5.setMaximumSize(QtCore.QSize(75, 25))
        self.label_5.setAutoFillBackground(False)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_4.addWidget(self.label_5)
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        self.label_6.setMaximumSize(QtCore.QSize(75, 25))
        self.label_6.setAutoFillBackground(False)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_4.addWidget(self.label_6)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_4.sizePolicy().hasHeightForWidth())
        self.lineEdit_4.setSizePolicy(sizePolicy)
        self.lineEdit_4.setMaximumSize(QtCore.QSize(75, 25))
        self.lineEdit_4.setAutoFillBackground(False)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.horizontalLayout_3.addWidget(self.lineEdit_4)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_5.sizePolicy().hasHeightForWidth())
        self.lineEdit_5.setSizePolicy(sizePolicy)
        self.lineEdit_5.setMaximumSize(QtCore.QSize(75, 25))
        self.lineEdit_5.setAutoFillBackground(False)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.horizontalLayout_3.addWidget(self.lineEdit_5)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_6.sizePolicy().hasHeightForWidth())
        self.lineEdit_6.setSizePolicy(sizePolicy)
        self.lineEdit_6.setMaximumSize(QtCore.QSize(75, 25))
        self.lineEdit_6.setAutoFillBackground(False)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.horizontalLayout_3.addWidget(self.lineEdit_6)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.layoutWidget1 = QtWidgets.QWidget(Form)
        self.layoutWidget1.setGeometry(QtCore.QRect(440, 140, 41, 121))
        self.layoutWidget1.setAutoFillBackground(False)
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_7 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_7.setAutoFillBackground(False)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_2.addWidget(self.label_7)
        self.label_8 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_8.setAutoFillBackground(False)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_2.addWidget(self.label_8)
        ###Porty Boże Serialowe
        self.portNames = QtWidgets.QComboBox(Form)
        self.portNames.addItems([ port.portName() for port in QSerialPortInfo().availablePorts() ])
        self.portNames.setMinimumHeight(30)
        ### Label do portu
        self.portSelect=QtWidgets.QLabel(Form)
        self.portNames.setGeometry(380,100,75,25)
        self.portSelect.setGeometry(190,100,180,25)
        ###Baudrates
        self.baudRates = QtWidgets.QComboBox(Form)
        self.baudRates.addItems([
            '110', '300', '600', '1200', '2400', '4800', '9600', '14400', '19200', '28800', 
            '31250', '38400', '51200', '56000', '57600', '76800', '115200', '128000', '230400', '256000', '921600'
        ])
        self.baudRates.setCurrentText('115200')
        self.baudRates.setMinimumHeight(30)
        self.baudRates.setGeometry(456,100,75,25)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        ###Ograniczenia przy wporwadzaniu danych oraz połaczenie przycisku z metodą.
        self.pushButton.clicked.connect(self.clickMethod)
        self.lineEdit.setValidator(QIntValidator(0,255))
        self.lineEdit.setMaxLength(3)
        self.lineEdit_2.setValidator(QIntValidator(0,255))
        self.lineEdit_2.setMaxLength(3)
        self.lineEdit_3.setValidator(QIntValidator(0,255))
        self.lineEdit_3.setMaxLength(3)
        self.lineEdit_4.setValidator(QIntValidator(0,255))
        self.lineEdit_4.setMaxLength(3)
        self.lineEdit_5.setValidator(QIntValidator(0,255))
        self.lineEdit_5.setMaxLength(3)
        self.lineEdit_6.setValidator(QIntValidator(0,255))
        self.lineEdit_6.setMaxLength(3)
    def clickMethod(self):
        
        stral=self.lineEdit.text()+","+self.lineEdit_2.text()+","+self.lineEdit_3.text()+","+self.lineEdit_4.text()+","+self.lineEdit_5.text()+","+self.lineEdit_6.text()
        print(stral)
        
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "QutletHue"))
        self.pushButton.setText(_translate("Form", "Wyślij"))
        self.label_2.setText(_translate("Form", "R:"))
        self.label.setText(_translate("Form", "G:"))
        self.label_3.setText(_translate("Form", "B:"))
        self.label_4.setText(_translate("Form", "R:"))
        self.label_5.setText(_translate("Form", "G:"))
        self.label_6.setText(_translate("Form", "B:"))
        self.label_7.setText(_translate("Form", "Prawa"))
        self.label_8.setText(_translate("Form", "Lewa"))
        self.portSelect.setText(_translate("Form","Wybierz port do komunikacji:"))
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ###CSS Boży
    style = """
   QWidget{
       background: #213769;
   }
   QLabel{
       color: #baab00;
       font: "Arial";
       font-size:14px;
       font-weight:opaque;
   }
   QLineEdit{
       padding:1px;
       color:#baab00;
       font: "Arial";
       font-size:14px;
       font-weight:opaque;
       border: 2px solid #baab08;
       border-radius: 8px;
   }
     QPushButton:hover
   {
    padding:1px;
       color:#000000;
       font: "Arial";
       font-size:14px;
       font-weight:opaque;
       border: 2px solid #000000;
       border-radius: 8px;
          
   }
   QPushButton
   {
    padding:1px;
       color:#baab00;
       font: "Arial";
       font-size:14px;
       font-weight:opaque;
       border: 2px solid #baab08;
       border-radius: 8px;
          
   }
   
   QComboBox
   {
       left: 106px;
      padding:1px;
       color:#baab00;
       font: "Arial";
       font-size:14px;
       font-weight:opaque;
       border: 2px solid #baab08;
       border-radius: 16px;
      
   }
  
    """
    app.setStyleSheet(style)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    
    sys.exit(app.exec_())

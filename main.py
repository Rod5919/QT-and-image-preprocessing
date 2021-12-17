# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from api.imlib231 import Image
import glob

class Ui_MainWindow(object):
    def __init__(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
        self.imagepath = "images/base.png"
        self.valid = False
        #region css
        f = open("css/style.css", "r")
        self.style = f.read()
        f.close()
        f = open("css/buttonStyle.css", "r")
        self.button_style = f.read()
        f.close()
        #endregion css
        self.main_window = MainWindow
        self.setupUi()
    
    def setupUi(self):
        self.centralwidget = QtWidgets.QWidget(self.main_window)
        self.centralwidget.setObjectName("centralwidget")
        
        #region buttons
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(390, 190, 89, 25))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setStyleSheet(self.button_style)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(510, 120, 89, 25))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setStyleSheet(self.button_style)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(390, 120, 89, 25))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.setStyleSheet(self.button_style)
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(510, 190, 89, 25))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.setStyleSheet(self.button_style)
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(390, 260, 89, 25))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.setStyleSheet(self.button_style)
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(510, 260, 89, 25))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_6.setStyleSheet(self.button_style)
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(570, 10, 50, 30))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_7.setStyleSheet("background: #AA0000;\n"
        "border: 0.5px solid rgba(255, 255, 255, 0.48);\n"
        "border-radius: 10px;\n"
        "\n"
        "font-family: Roboto;\n"
        "font-style: normal;\n"
        "font-weight: normal;\n"
        "font-size: 18px;\n"
        "line-height: 28px;\n"
        "\n"
        "color: #FFFFFF;")
        self.pushButton_7.clicked.connect(lambda: sys.exit(0))
        
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(470, 375, 50, 50))
        self.pushButton_8.setStyleSheet("background-color: rgb(255, 255, 255);\n"
        "border-image: url(:/check/assets/check2.png);\n"
        "border-radius:30px\n"
        "")
        self.pushButton_8.setText("")
        self.pushButton_8.setObjectName("crt_pushButton_2")
        self.pushButton_8.setIcon(QIcon('assets/check2.png'))
        self.pushButton_8.setIconSize(QtCore.QSize(45, 45))
        self.pushButton_8.setStyleSheet("border-radius:30px\noverflow:hidden;")
        self.pushButton_8.clicked.connect(self.validator)
        #endregion buttons
        
        #region labels
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(450, 80, 81, 17))
        self.label.setObjectName("label")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(460, 315, 67, 17))
        self.label_2.setObjectName("label_2")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(0, 0, 640, 50))
        self.label_3.setObjectName("label_3")
        self.label_3.setStyleSheet(self.style)        
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(0, 435, 640, 25))
        self.label_4.setStyleSheet("background-color: black;\n"
        "color: white;\n"
        "padding: 5px 0;")
        self.label_4.setObjectName("label_4")
        #endregion labels
        
        self.img_label = QtWidgets.QLabel(self.centralwidget)
        self.img_label.setGeometry(QtCore.QRect(20, 120, 350, 175))
        
        self.lineEdit = QtWidgets.QLineEdit(self.main_window)
        self.lineEdit.setGeometry(QtCore.QRect(410, 340, 170, 25))
        
        self.main_window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self.main_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 22))
        self.menubar.setObjectName("menubar")
        self.main_window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self.main_window)
        self.statusbar.setObjectName("statusbar")
        self.main_window.setStatusBar(self.statusbar)

        # Organizando los widgets en el eje Z...
        self.label.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        self.pushButton_3.raise_()
        self.pushButton_4.raise_()
        self.pushButton_5.raise_()
        self.pushButton_6.raise_()
        self.pushButton_7.raise_()
        self.pushButton_8.raise_()

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self.main_window)

    def retranslateUi(self):
        self.main_window.setWindowTitle("MainWindow")
        self.pushButton.setText("Original")
        self.pushButton_2.setText("Median")
        self.pushButton_3.setText("Canny edge")
        self.pushButton_4.setText("Blur")
        self.pushButton_5.setText("Gaussian")
        self.pushButton_6.setText("Grayscale")
        self.pushButton_7.setText("X")
        
        # Deshabilita los botones cuando la ruta es incorrecta
        self.pushButton.setEnabled(self.valid)
        self.pushButton_2.setEnabled(self.valid)
        self.pushButton_3.setEnabled(self.valid)
        self.pushButton_4.setEnabled(self.valid)
        self.pushButton_5.setEnabled(self.valid)
        self.pushButton_6.setEnabled(self.valid)
         
        # Cambia la imagen a mostrar
        pixmap = QPixmap(self.imagepath).scaledToWidth(350)
        self.img_label.setPixmap(pixmap)
        
        # Asigna los textos de las etiquetas
        self.label.setText("Filtros")
        self.label_2.setText("Ruta")
        self.label_3.setText("Proyecto Final IMT-231")
        self.label_4.setText("Gabriela Ana Zubieta")
        
        # Genera interacción con los botones
        try:
            self.pushButton.clicked.connect(lambda: self.change_image(self.im.median,"."))
            self.pushButton_2.clicked.connect(lambda: self.change_image(self.im.median,"_median."))
            self.pushButton_3.clicked.connect(lambda: self.change_image(self.im.canny_edge,"_canny."))
            self.pushButton_4.clicked.connect(lambda: self.change_image(self.im.blur,"_blur."))
            self.pushButton_5.clicked.connect(lambda: self.change_image(self.im.gaussian,"_gaussian."))
            self.pushButton_6.clicked.connect(lambda: self.change_image(self.im.grayscale,"_gray."))
        except:
            pass

    def validator(self):
        path = self.lineEdit.text()
        dir_path = '/'.join(path.split('/')[:-1])+'/'
        
        if path in glob.glob(dir_path+'*'): #Verifica si laa imagen existe
            self.valid = True
            self.imagepath = path
            self.im = Image(path)
            self.retranslateUi()
        else: # Mensaje de error y deshabilita botones
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("No existe la imagen.\nRuta incorrecta")
            msg.setWindowTitle("ERROR")
            msg.exec_()
            self.valid = False
            self.retranslateUi()
            
    def change_image(self, function, suffix):
        # Verifica si ya se realizó la función
        if not(self.im.dir_path+self.im.filename.split(".")[0]+suffix+self.im.filename.split(".")[-1] in glob.glob(self.im.dir_path+'*')):
            function()
        self.imagepath = self.im.dir_path+self.im.filename.split(".")[0]+suffix+self.im.filename.split(".")[-1]
        self.retranslateUi()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

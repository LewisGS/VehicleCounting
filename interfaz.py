
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPalette, QPixmap, QResizeEvent, QMouseEvent, QIcon
from PyQt5.QtCore import QTranslator, QLocale, QLibraryInfo, Qt, QPoint, QSize
from PyQt5.QtWidgets import (QApplication, QDialog, QVBoxLayout, QWidget, QPushButton,QFrame, QLabel,  QMessageBox, QLineEdit)
import cv2
import numpy


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(582, 484)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.btnCancelar = QtWidgets.QPushButton(self.centralwidget)
        self.btnCancelar.setGeometry(QtCore.QRect(50, 380, 131, 51))
        self.btnCancelar.setObjectName("btnCancelar")
        
        self.btnIniciar = QtWidgets.QPushButton(self.centralwidget)
        self.btnIniciar.setGeometry(QtCore.QRect(350, 380, 131, 51))
        self.btnIniciar.setObjectName("btnIniciar")
        self.lblCuadrado = QtWidgets.QLabel(self.centralwidget)
        self.lblCuadrado.setGeometry(QtCore.QRect(10, 70, 91, 16))
        self.lblCuadrado.setObjectName("lblCuadrado")
        self.lblLimite = QtWidgets.QLabel(self.centralwidget)
        self.lblLimite.setGeometry(QtCore.QRect(10, 140, 121, 16))
        self.lblLimite.setObjectName("lblLimite")
        self.lblMedia = QtWidgets.QLabel(self.centralwidget)
        self.lblMedia.setGeometry(QtCore.QRect(10, 210, 111, 16))
        self.lblMedia.setObjectName("lblMedia")

        self.leCuadrado = QtWidgets.QLineEdit(self.centralwidget)
        self.leCuadrado.setGeometry(QtCore.QRect(150, 70, 113, 20))
        self.leCuadrado.setPlaceholderText("400 - 1000")
        self.leCuadrado.setObjectName("leCuadrado")

        self.leLimite = QtWidgets.QLineEdit(self.centralwidget)
        self.leLimite.setGeometry(QtCore.QRect(150, 140, 113, 20))
        self.leLimite.setPlaceholderText("50 - 100")
        self.leLimite.setObjectName("leLimite")

        self.leMedia = QtWidgets.QLineEdit(self.centralwidget)
        self.leMedia.setGeometry(QtCore.QRect(150, 210, 113, 20))
        self.leMedia.setPlaceholderText("0.02 - 0.09")
        self.leMedia.setObjectName("leMedia")

        self.leRuta = QtWidgets.QLineEdit(self.centralwidget)
        self.leRuta.setGeometry(QtCore.QRect(150, 280, 351, 20))
        self.leRuta.setPlaceholderText("Ruta del video a leer...")
        self.leRuta.setObjectName("leRuta")
        
        self.btnCargar = QtWidgets.QPushButton(self.centralwidget)
        self.btnCargar.setGeometry(QtCore.QRect(30, 320, 471, 41))
        self.btnCargar.setObjectName("btnCargar")

        self.lblTitulo = QtWidgets.QLabel(self.centralwidget)
        self.lblTitulo.setGeometry(QtCore.QRect(110, 0, 391, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.lblTitulo.setFont(font)
        self.lblTitulo.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lblTitulo.setObjectName("lblTitulo")

        self.btnBusqueda = QtWidgets.QPushButton(self.centralwidget)
        self.btnBusqueda.setGeometry(QtCore.QRect(10, 280, 101, 21))
        self.btnBusqueda.setObjectName("btnBusqueda")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 582, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
#****************************TRABAJANDO****************************#
        self.btnBusqueda.clicked.connect(self.findVideo)
        self.btnCargar.clicked.connect(self.save_text)
        self.btnIniciar.clicked.connect(self.launchScript)
        self.btnCancelar.clicked.connect(self.AboutMessage)       


# ********************************************************************
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate(
            "MainWindow", "Configurador de aplicación"))
        self.btnCancelar.setText(_translate("MainWindow", "Detener y salir"))
        self.btnIniciar.setText(_translate("MainWindow", "Iniciar conteo"))
        self.lblCuadrado.setText(_translate("MainWindow", "Tamaño cuadrado"))
        self.lblLimite.setText(_translate(
            "MainWindow", "Sensivilidad de detección"))
        self.lblMedia.setText(_translate("MainWindow", "Detección de cambios"))
        self.btnCargar.setText(_translate(
            "MainWindow", "Cargar todos los datos"))
        self.lblTitulo.setText(_translate("MainWindow", "            PANEL DE CONFIGURACIÓN\n"
                                          "CONTROL DE VOLUMENES EN CARRETERAS"))
        self.btnBusqueda.setText(_translate("MainWindow", "Buscar vídeo"))

#****************************TRABAJANDO****************************#
    # Creamos una funcion para buscar, elegir el video y mostrar su ruta.
    def findVideo(self):
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(
            None, "Selecciona un video...", "", "Archivo permitido(*.avi, *.mp4)")
        self._filename = fileName
        self.leRuta.setText(fileName)

    # Funcion que crea un archivo de texto con la ruta
    def save_text(self):        
        param = self.leCuadrado.text()
        param2 = self.leLimite.text()
        param3 = self.leMedia.text()
        with open('C:/PROYECTO FINAL/configuracion.txt', 'w') as f:
            my_text = self._filename
            f.write(my_text + '\n' + param + '\n' + param2 + '\n' + param3)

      # Funcion desde donde activamos el boton de inicio
    def launchScript(self):
        import proyectoFINAL 
        proyectoFINAL.mainFunction()
    
    def AboutMessage(self):
        alert = QMessageBox()
        alert.setWindowIcon(QIcon('C:/PROYECTO FINAL/coche.png'))
        alert.setWindowTitle('Saliendo...')
        alert.setText('¡HASTA PRONTO!')        
        alert.exec_()       
        sys.exit()


# ********************************************************************
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')
    # Traducimos al idioma del SO
    qt_traductor = QTranslator()
    qt_traductor.load("qtbase_"+QLocale.system().name(),
                      QLibraryInfo.location(QLibraryInfo.TranslationsPath))
    app.installTranslator(qt_traductor)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    # Icono de aplicación
    MainWindow.setWindowIcon(QIcon('C:/PROYECTO FINAL/coche.png'))
    
    MainWindow.show()
    sys.exit(app.exec_())

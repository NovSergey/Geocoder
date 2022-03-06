from PyQt5 import uic
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox

import Geocoder
import StaticMaps
import PPO


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('gui/MainWindow.ui', self)
        self.findBTN.clicked.connect(self.findToponym)
        self.resultLW.itemClicked.connect(self.resultLWclick)
        self.btn2.clicked.connect(self.findOrganiz)
    def resultLWclick(self, item):
        global check
        geoO = self.result[self.resultLW.currentRow()]
        if not StaticMaps.downloadImageSucsess(geoO, check):
            QMessageBox.information(self, "Info", "Ошибка при загрузке фото")
        pixmap = QPixmap("images/map.png")
        self.imageLBL.setPixmap(pixmap)

    def findToponym(self):
        global check
        check = True
        toponym = self.queryLE.text().strip()
        if toponym == "":
            return
        self.result = Geocoder.find(toponym)
        sp = [Geocoder.convert(geoO) for geoO in self.result]
        self.resultLW.clear()
        self.resultLW.addItems(sp)
    def findOrganiz(self):
        global check
        check = False
        organiz = self.queryLE.text().strip()
        if organiz == "":
            return
        self.result = PPO.find(organiz)
        sp = [PPO.convert(geoO) for geoO in self.result]
        self.resultLW.clear()
        self.resultLW.addItems(sp)
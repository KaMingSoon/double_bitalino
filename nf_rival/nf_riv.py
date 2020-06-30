from PyQt5 import QtWidgets, QtGui
from nf_riv_ui import Ui_MainWindow  # importing our UI window
import os, sys
 
 
class main_window(QtWidgets.QMainWindow):
    def __init__(self, imgList):
        super(main_window, self).__init__()
        self.ui = Ui_MainWindow()
        self.imagesInList = imgList
        self.imgCount = 0
        self.ui.setupUi(self)
        # connect button click event to slot btnClicked
        self.ui.pushButton.clicked.connect(self.nextImage)
        self.nextImage()

 
    def nextImage(self):
    """ switch to next image or previous image
    """
    if self.imagesInList:
        if self.imgCount == len(self.imagesInList):
            self.imgCount = 0

        self.showImageByPath(
                self.imagesInList[self.imgCount])

        if self.animFlag:
            self.imgCount += 1
        else:
            self.imgCount -= 1


    def showImageByPath(self, path):
        if path:
            image = QtGui.QImage(path)
            pp = QtGui.QPixmap.fromImage(image)
            self.ui.label.setPixmap(QtGui.QPixmap('user1\stimuli\Sudoku1.png'))

    

 
app = QtWidgets.QApplication([])
user1_stimuli = []
user2_stimuli = []
application = main_window()
application.show()
 
sys.exit(app.exec())
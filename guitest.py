from PyQt4 import QtGui
import sys
import untitled1
import tkinter as tk
import tkFileDialog
from microsoftcognitive import MicrosoftVision
from requests import Request
root = tk.Tk()
root.withdraw()
mv = MicrosoftVision('',MicrosoftVision.VisualService.ANALYZE)

class GUIApp(QtGui.QMainWindow,untitled1.Ui_MainWindow):
    def __init__(self):
        super(GUIApp,self).__init__(None)

        self.setupUi(self)
        self.pushButton.setText('Analyse Image')
        self.pushButton.clicked.connect(self.button_clicked)
    def button_clicked(self):
        file_path = tkFileDialog.askopenfilename()
        img = QtGui.QPixmap(file_path)
        scene = QtGui.QGraphicsScene()
        img = img.scaled(self.graphicsView.size())
        scene.addPixmap(img)
        self.graphicsView.setScene(scene)
        result = mv.recognizeImageFromFile(file_path)
        self.label.setText(str(result['categories'][0]['name']))
        print result



def main():
    app = QtGui.QApplication(sys.argv)
    form = GUIApp()
    form.show()
    app.exec_()


if __name__ == '__main__':
    main()

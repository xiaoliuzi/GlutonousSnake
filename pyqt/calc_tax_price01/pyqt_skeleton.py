import sys
from PyQt5 import QtCore, QtGui, uic

qtCreatorfile = "" # Enter file here.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtGui.QMainWindow, Ui_MainWindow):
	def __init__(self):
	QtGui.QMainWindow.__init__(self)
	Ui_MainWindow.__init__(self)
	self.setupUI(self)

if __name__ == "__main__"
	app = QtGui.QApplication(sys.argv)
	window = MyApp()
	window.show()
	sys.exit(app.exec_())


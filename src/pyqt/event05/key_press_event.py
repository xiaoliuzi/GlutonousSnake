import sys
from PyQt4 import QtGui, QtCore

class Example(QtGui.QWidget):

    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):

        self.setGeometry(300,300,250,150)
        self.setWindowTitle('Event handler')
        self.show()
    # A key has been pressed!
    def keyPressEvent(self, e):
        # Did the user press the Escapse key?
        if e.key() == QtCore.Qt.Key_Escape:# QtCore.Qt.Key_Escape is a value that equates to what the operating system passes to python from the key board when the escape key is pressed.
            # Yes: Close the window
            self.close()

        # No: Do nothing.

def main():

    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

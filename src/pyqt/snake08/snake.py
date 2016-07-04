import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import *
from PyQt4.QtCore import *


class Snake(QWidget):

    def __init__(self):
        super(Snake, self).__init__()
        self.initUI()

    def initUI(self):
        self.text = "hello world"
        self.setGeometry(100, 100, 400, 300)
        self.setWindowTitle("Gluttonous Snake")
        self.show()

    def paintEvent(self, event):
        pborder = QPainter()
        pborder.begin(self)
    
        
        pborder.setPen(QColor(Qt.blue))
        pborder.drawRect(10, 150, 150, 80)
        
        #---draw initial snake
        pborn_snake = QPainter()
        pborn_snake.begin(self)

        pborn_snake.setPen(QColor(Qt.red))
        for j in range(0, 100):
            for i in range(20, 80, 10):
                pborn_snake.drawPoint(i+10, 170)

        #---draw food
        pfood = QPainter()
        pfood.begin(self)

        pfood.drawPoint(50, 180)

        pborder.end()
        pborn_snake.end()
        pfood.end()

def main():
    
    app = QApplication(sys.argv)

    s = Snake()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

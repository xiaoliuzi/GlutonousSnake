import sys, random
from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import *
from PyQt4.QtCore import *


class Snake(QtGui.QWidget):

    def __init__(self):
        super(Snake, self).__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle("Gluttonous Snake")
        self.show()

    def paintEvent(self, event):
        qp = QtGui.QPainter()
        qp.begin(self)
        #self.drawPoints(qp)
        for i in range (10, 200, 50):
            self.drawRectangles(qp, i)
            timer = QtCore.QTimer()
            timer.start(2000)
            self.update()
        qp.end()

        #self.paintBorderEvent(QtCore.Qt.Key_B)
        #self.paintSnakeEvent(QtCore.Qt.Key_B)
        #self.paintFood(QtCore.Qt.Key_B)
    
    def drawRectangles(self, qp, i):
        color = QtGui.QColor(0, 0, 0)
        color.setNamedColor("#d4d4d4")
        qp.setPen(color)

        qp.setBrush(QtGui.QColor(200-i, 0, 0))
        qp.drawRect(10, 15, 90, 60)

        qp.setBrush(QtGui.QColor(255-i, 80, 0, 160))
        qp.drawRect(130, 15, 90, 60)

        qp.setBrush(QtGui.QColor(25+i, 0, 90, 200))
        qp.drawRect(250, 15, 90, 60)



    def drawPoints(self, qp):
        qp.setPen(QtCore.Qt.red)
        size = self.size()
        
        for i in range(1000):
            x = random.randint(1, size.width()-1)
            y = random.randint(1, size.height()-1)
            #qp.drawPoint(x, y)


    def paintBorderEvent(self, event):
        pborder = QPainter()
        pborder.begin(self)
    
        pborder.setPen(QColor(Qt.blue))
        pborder.drawRect(10, 150, 150, 80)
        pborder.end()

    #---draw initial snake
    def paintSnakeEvent(self, event):
        pborn_snake = QPainter()
        pborn_snake.begin(self)

        pborn_snake.setPen(QColor(Qt.red))
        """
        for j in range(0, 100):
            for i in range(20, 40, 10):
                pborn_snake.drawPoint(i+10, 170)
        """
        
        pborn_snake.end()

    #---draw food
    def paintFood(self, event):
        pfood = QPainter()
        pfood.begin(self)

        pfood.drawPoint(50, 180)

        pfood.end()

    def SnakeMove(self):
        #paintSnake(self, e)
        print 'hello '
#        self.xlz_move()
"""
    def xlz_move(self):
        pborn_snake.begin()
        pborn_snake.setpen(QColor(Qt.black))
        pborn_snake.drawPoint(100, 170)
        pborn_snake.drawPoint(110, 170)
        pborn_snake.end()
"""

def main():
    
    app = QApplication(sys.argv)
    s = Snake()

#    timer = QtCore.QTimer()
#    timer.timeout.connect(s.paintEvent )
#    timer.start(2000)

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

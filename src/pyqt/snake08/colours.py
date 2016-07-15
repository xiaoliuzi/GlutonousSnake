#!/usr/bin/python
#-*- coding:utf-8 -*-
"""
ZetCode PyQt4 tutorial
This example draws three rectangles in three
different colours.

author: Jan Bodnar
website: zetcode.com
last edited: September 2011
"""

import sys
from PyQt4 import QtGui, QtCore

class Example(QtGui.QWidget):
    x = 10
    y = 15
    d = 0
    nodelist = [10, 15, 0]#x,y,d
    
    slist = [nodelist]
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()
    def initUI(self):
        self.setGeometry(300, 300, 1200, 600)
        self.setWindowTitle('Colours')
        self.show()

    def paintEvent(self, e):
        qp = QtGui.QPainter()
        qp.begin(self)
        self.drawRectangles(qp, Example.slist)
        self.drawFood(qp)
        qp.end()

    def drawRectangles(self, qp, slist):
        color = QtGui.QColor(0, 0, 0)
        color.setNamedColor('#d4d4d4')
        qp.setPen(color)

        qp.setBrush(QtGui.QColor(0, 0, 0))
        
        for i in range(10, 150, 70):
            qp.drawRect(i, 15, 60, 60)

    def drawFood(self, qp):
        color = QtGui.QColor(255,0,0)
        color.setNamedColor('#d4d4d4')
        qp.setPen(color)
        
        qp.setBrush(QtGui.QColor(200,0,0))
        qp.drawRect(200, 130, 60, 60)


def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()


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

import sys, random
from PyQt4 import QtGui, QtCore

class Snake(QtGui.QWidget):
    x = 10
    y = 10
    d = 0
    nodelist = [10, 10, 0]#x,y,d
    slist = [nodelist]

    def __init__(self):
        super(Snake, self).__init__()
        self.initUI()
    def initUI(self):
        self.setGeometry(300, 300, 1200, 600)
        self.setWindowTitle('Colours')
        self.show()

    def paintEvent(self, e):
        qp = QtGui.QPainter()
        qp.begin(self)
        self.drawRectangles(qp, Snake.slist)
        self.drawFood(qp)
        qp.end()

    def drawRectangles(self, qp, slist):
        color = QtGui.QColor(0, 0, 0)
        color.setNamedColor('#d4d4d4')
        qp.setPen(color)

        #qp.setBrush(QtGui.QColor(0, 0, 0))
        
        for i in range(0, len(slist)):
            qp.drawRect(slist[i][i], 10, 60, 60)

    def eraseRectangels(self, qp, nodelist):
        color = QtGui.QColor(0, 0, 0)
        color.setNamedColor('#d4d4d4')
        qp.setPen(color)
        qp.setBrush(QtGui.QColor(0,0,0))
        qp.drawRect(nodelist[0], nodelist[1], 60, 60)

    def drawFood(self, qp):
        color = QtGui.QColor(255,0,0)
        color.setNamedColor('#d4d4d4')
        qp.setPen(color)
        
        qp.setBrush(QtGui.QColor(200,0,0))
        qp.drawRect(200, 130, 60, 60)

    def move(self, slist, direction):
        if direction == 0:
        #right direction->
            for i in range(0, len(slist)):
                sqlist[i][0] += 1
            # last one disappear
            sqlist[i][-1] 
        elif direction == 3:
        #left direction<-
            for i in range(0, len(slist)):
                sqlist[i][i]+1

def main():
    app = QtGui.QApplication(sys.argv)
    ex = Snake()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()


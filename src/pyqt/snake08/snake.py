#!/usr/bin/python
#-*- coding:utf-8 -*-
"""
PyQt4 tutorial

Description: This file is the gluttonous snake games.

Author: xiaoliuzi

date: 20160719

email: genie.6qp@gmail.com

"""

import sys, random
from PyQt4 import QtGui, QtCore

class Food(QtGui.QWidget):
    xrandom_list = [10, 80, 150, 220, 290, 360, 430, 500, 570, 640, 710 ]
    yrandom_list = [10, 80, 150, 220, 290, 360]
class Snake(QtGui.QWidget):
    
    head_list = [80, 10]
    body_list = [10, 10]
    slist = [head_list, body_list]

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

        self.drawRectangleBorder(qp)
        self.drawSnake(qp, Snake.slist)
        self.drawFood(qp)

        qp.end()

    def drawRectangleBorder(self, qp):

        color = QtGui.QColor(65, 105, 225)
        qp.setPen(color)
        qp.drawRect(10, 10, 760, 410)

    def drawSnake(self, qp, slist):
        qp.setBrush(QtGui.QColor(0,0,0))
        for i in range(0, len(slist)):
            qp.drawRect(slist[i][0], slist[i][1], 60, 60)

    def drawFood(self, qp):
        color = QtGui.QColor(255,0,0)
        qp.setPen(color)
        polymerrization = True
        while polymerrization:
            x = random.choice(range(10, 710, 70))
            y = random.choice(range(10, 360, 70))
            fcoordinate_list = [x,y]
            if fcoordinate_list in Snake.slist:
                polymerrization = True
            else:
                polymerrization = False

        qp.setBrush(QtGui.QColor(200,0,0))
        qp.drawRect(x, y, 60, 60)

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



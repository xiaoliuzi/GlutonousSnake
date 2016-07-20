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
from PyQt4.QtCore import QTimer

#from functools import partial # to pass the arguments for signal and slots

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
        self.setWindowTitle('Glustonnous Snake')
        self.show()

    def paintEvent(self, e):
        #qp = QtGui.QPainter()
        bqp = QtGui.QPainter()
        #fqp = QtGui.QPainter()
        #sqp = QtGui.QPainter()

        bqp.begin(self)
        #bqp.begin(self)
        #fqp.begin(self)
        #sqp.begin(self)

        #self.drawFood(fqp)
        #self.drawSnake(self, sqp, slist):
        self.drawRectangleBorder(bqp)
        #self.drawRectangleBorder(bqp)

        bqp.end()
        #bqp.end()
        #fqp.end()
        #sqp.end()

    def drawRectangleBorder(self, bqp):
        color = QtGui.QColor(0, 0, 255)
        bqp.setPen(color)
        bqp.drawRect(10, 10, 760, 410)

    def drawSnake(self, qp, slist):
        qp.setBrush(QtGui.QColor(0,0,0))
        for i in range(0, len(slist)):
            qp.drawRect(slist[i][0], slist[i][1], 60, 60)

    def drawFood(self, fqp):
        #qp = QtGui.QPainter()
        #self.qp.begin(self)

        print 'draw food'
        #color = QtGui.QColor(255,0,0)
        #qp.setPen(color)

        polymerrization = True
        while polymerrization:
            x = random.choice(range(10, 710, 70))
            y = random.choice(range(10, 360, 70))
            fcoordinate_list = [x,y]
            if fcoordinate_list in Snake.slist:
                polymerrization = True
            else:
                polymerrization = False

        fqp.setBrush(QtGui.QColor(200,0,0))
        fqp.drawRect(x, y, 60, 60)

        #self.update()
        #self.qp.end()


def main():
    app = QtGui.QApplication(sys.argv)
    ex = Snake()


    sys.exit(app.exec_())

if __name__ == '__main__':
    main()




'''
        #for testing timer demo
        food_timer = QtCore.QTimer(self)
        food_timer.timeout.connect(self.update)#to update the paiter
        #QtCore.QObject.connect(food_timer, QtCore.SIGNAL("timeout()"), partial(self.drawFood, self.fqp))
        food_timer.start(1000)
'''
'''
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

'''

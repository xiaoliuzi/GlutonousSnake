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
from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import QTimer

#from functools import partial # to pass the arguments for signal and slots

class Food(QtGui.QWidget):
    xrandom_list = [10, 80, 150, 220, 290, 360, 430, 500, 570, 640, 710 ]
    yrandom_list = [10, 80, 150, 220, 290, 360]

class Snake(QtGui.QWidget):
    
    direction = 0
    head_list = [80, 10]
    body_list = [10, 10]
    slist = [head_list, body_list]
    fcoordinate_list = [220,220]
    qp = QtGui.QPainter()
    fqp = QtGui.QPainter()


    def __init__(self):
        super(Snake, self).__init__()

        #for testing timer demo
        food_timer = QtCore.QTimer(self)
        food_timer.timeout.connect(self.update)#to update the paiter
        #QtCore.QObject.connect(food_timer, QtCore.SIGNAL("timeout()"), partial(self.drawFood, self.fqp))
        food_timer.start(800)

        #self.fqp.begin(self)
        #self.drawInitFood(self.fqp)
        #self.fqp.end()

        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 1200, 600)
        self.setWindowTitle('Glutonous Snake')
        

        self.show()

    def paintEvent(self, e):
        #qp = QtGui.QPainter()

        self.qp.begin(self)
        self.drawRectangleBorder(self.qp)

        self.drawFood(self.qp)
        #self.drawInitFood(self.fqp)
        #self.drawInitFood(self.qp)
#        self.drawInitFood(self.qp)
        self.drawSnake(self.qp, self.slist)

        self.move(self.slist, self.direction)
        self.collide(self.qp, self.slist)

        self.qp.end()

    def keyPressEvent(self, e):
        if e.key() == QtCore.Qt.Key_Escape:
            self.close()
        if e.key() == QtCore.Qt.Key_Right:
            self.direction = 0
        if e.key() == QtCore.Qt.Key_Up:
            self.direction = 1
        if e.key() == QtCore.Qt.Key_Down:
            self.direction = 2
        if e.key() == QtCore.Qt.Key_Left:
            self.direction = 3

        #print 'direction is ' , self.direction


    def move(self, slist, direction):
        if (slist[0][0] <= 710 and slist[0][0] >= 10) and (slist[0][1] >= 10 and slist[0][1] <= 360):
            #right direction right
            if direction == 0:
                # last one disappear
                del slist[-1]
                head_list = [slist[0][0]+70, slist[0][1]]
                slist.insert(0, head_list)
            elif direction == 1:
            #left direction up
                del slist[-1]
                head_list = [slist[0][0], slist[0][1]-70]
                slist.insert(0, head_list)
            elif direction == 2:
            #left direction down
                del slist[-1]
                head_list = [slist[0][0], slist[0][1]+70]
                slist.insert(0, head_list)
            elif direction == 3:
            #left direction left
                del slist[-1]
                head_list = [slist[0][0]-70, slist[0][1]]
                slist.insert(0, head_list)

            #print "key pressed number: " , direction
        #else:
            #print " beyond border"

    def collide(self, qp, slist):
        # collide with food
        #print 'collision'
        if (slist[0][0] == self.fcoordinate_list[0]) and (slist[0][1] == self.fcoordinate_list[1]):
            #snake increases
            slist.insert(0, self.fcoordinate_list)

            #draw next food
            self.generateFoodPos()
            self.drawFood(qp)


    def drawRectangleBorder(self, qp):
        color = QtGui.QColor(0, 0, 255)
        #color = QtGui.QColor(255, 255, 0)
        qp.setPen(color)
        #qp.setBrush(color)
        qp.drawRect(10, 10, 760, 410)

    def drawSnake(self, qp, slist):
        qp.setBrush(QtGui.QColor(0,0,0))
        for i in range(0, len(slist)):
            qp.drawRect(slist[i][0], slist[i][1], 60, 60)

    def drawInitFood(self, qp):
        qp.setBrush(QtGui.QColor(200, 0, 0))
        qp.drawRect(220, 220, 60, 60)

    def drawFood(self, qp):
        #print 'draw food'
        qp.setBrush(QtGui.QColor(200,0,0))
        qp.drawRect(self.fcoordinate_list[0], self.fcoordinate_list[1], 60, 60)
        #qp.drawRect(220, 220, 60, 60)

    def generateFoodPos(self):
        #generate random position of food.
        polymerrization = True
        while polymerrization:
            x = random.choice(range(10, 710, 70))
            y = random.choice(range(10, 360, 70))
            self.fcoordinate_list = [x,y]
            if self.fcoordinate_list in Snake.slist:
                polymerrization = True
            else:
                polymerrization = False


def main():
    app = QtGui.QApplication(sys.argv)
    ex = Snake()


    sys.exit(app.exec_())

if __name__ == '__main__':
    main()





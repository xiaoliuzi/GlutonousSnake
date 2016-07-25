#!/usr/bin/python
#-*- coding:utf-8 -*-
"""
PyQt4 tutorial

Description: This file is the gluttonous snake games.

Author: xiaoliuzi

date: 20160719

email: genie.6qp@gmail.co:30


"""

import sys, random

from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import Qt, QTimer

class Snake(QWidget):
    
    direction = 0 # initial snake move direction
    snake_food_size = 60 # initial snake or food size
    head_list = [80, 10] # initial snake head
    body_list = [10, 10] # initial snake body
    slist = [head_list, body_list]#initial snake coordinate
    fcoordinate_list = [220,220]#initial food coordinate
    qp = QPainter() # general painter

    def __init__(self):
        super(Snake, self).__init__()

        #for testing timer demo
        food_timer = QTimer(self)
        food_timer.timeout.connect(self.myupdate)#to update the paiter
        food_timer.start(800)

        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 1200, 600)
        self.setWindowTitle('Glutonous Snake')

        self.show()

    def paintEvent(self, e):
        print ('paintevent')
        #painter can be used in paintEvent() only.
        self.qp.begin(self)
        self.drawRectangleBorder(self.qp)

        self.drawFood(self.qp)
        self.drawSnake(self.qp, self.slist)

        #self.move(self.slist, self.direction)
        #self.collide(self.qp, self.slist)

        self.qp.end()


    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()
        if e.key() == Qt.Key_Right:
            self.direction = 0
        if e.key() == Qt.Key_Up:
            self.direction = 1
        if e.key() == Qt.Key_Down:
            self.direction = 2
        if e.key() == Qt.Key_Left:
            self.direction = 3

        #print 'direction is ' , self.direction
    def myupdate(self):
        print ('myupdate')
    
        self.move(self.slist, self.direction)
        self.repaint()
        self.collide(self.qp, self.slist)


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
        color = QColor(0, 0, 255)
        qp.setPen(color)
        qp.drawRect(10, 10, 760, 410)

    def drawSnake(self, qp, slist):
        qp.setBrush(QColor(0,0,0))
        for i in range(0, len(slist)):
            qp.drawRect(slist[i][0], slist[i][1], self.snake_food_size, self.snake_food_size)

    def drawInitFood(self, qp):
        qp.setBrush(QColor(200, 0, 0))
        qp.drawRect(220, 220, self.snake_food_size, self.snake_food_size)

    def drawFood(self, qp):
        #print 'draw food'
        qp.setBrush(QColor(200,0,0))
        qp.drawRect(self.fcoordinate_list[0], self.fcoordinate_list[1], self.snake_food_size, self.snake_food_size)

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


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Snake()

    sys.exit(app.exec_())


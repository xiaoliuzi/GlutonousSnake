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
from PyQt5.QtCore import Qt, QTimer, QRect

class Snake(QWidget):
    collision_tag = False
    templist = [0,0]
    count = 0
    x_init = 10
    y_init = 10
    direction = 0 # initial snake move direction
    old_direction = direction # to solve the opposite direction
    snake_food_size = 30 # initial snake or food size
    gap_of_snake_body = 10
    w = 10
    h = 5


    rect_border_width = ((snake_food_size+gap_of_snake_body)*w+snake_food_size)
    rect_border_height = ((snake_food_size+gap_of_snake_body)*h+snake_food_size)
    max_posx = (rect_border_width - snake_food_size+gap_of_snake_body)
    max_posy = (rect_border_height - snake_food_size+gap_of_snake_body)
    head_list = [(x_init+snake_food_size+gap_of_snake_body), y_init] # initial snake head
    body_list = [(x_init+snake_food_size+gap_of_snake_body), y_init] # initial snake body
    slist = [head_list, body_list]#initial snake coordinate
    fcoordinate_list = [((snake_food_size+gap_of_snake_body)+x_init),((snake_food_size+gap_of_snake_body)+y_init)]#initial food coordinate
    qp = QPainter() # general painter
    food_timer = QTimer()
    pause = False
    speed = 800 # it is ms time actually.

    def __init__(self):
        super(Snake, self).__init__()

        #for testing timer demo
        #food_timer = QTimer(self)
        self.food_timer.timeout.connect(self.myupdate)#to update the paiter
        self.food_timer.start(self.speed)

        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 1200, 600)
        self.setWindowTitle('Glutonous Snake')

        self.show()

    def paintEvent(self, e):
        #print ('paintevent')
        #painter can be used in paintEvent() only.
        self.qp.begin(self)
        self.drawRectangleBorder(self.qp)

        self.drawSnake(self.qp, self.slist)
        self.drawFood(self.qp)

        if self.direction == 4:#direction is 4 to show the snake is dead
            self.drawDeadSnake(self.qp, self.slist)

        self.qp.end()


    def keyPressEvent(self, e):
        if (self.direction ^ self.old_direction != 3):
            self.old_direction = self.direction
        if e.key() == Qt.Key_Right:
                self.direction = 0
        if e.key() == Qt.Key_Up:
                self.direction = 1
        if e.key() == Qt.Key_Down:
                self.direction = 2
        if e.key() == Qt.Key_Left:
                self.direction = 3
        if e.key() == Qt.Key_Space :
                self.pause = not self.pause 
        if e.key() == Qt.Key_Escape:
                self.close()

        #else:
            #print ('other key pressed')
        od = 'od is:'+repr( self.old_direction) 
        d = 'd is:'+repr( self.direction) 
        print(od)
        print(d)

    def myupdate(self):
        qrect = QRect(self.x_init, self.y_init, self.rect_border_width, self.rect_border_height)

        self.collide(self.qp, self.slist)
        #self.update(qrect)
        self.repaint()
        if self.collision_tag == False and self.pause == False:
            self.move(self.slist, self.direction)
        self.collision_tag = False
        #self.update(qrect)


        self.repaint()
        #self.update(qrect)


    def move(self, slist, direction):
        if (slist[0][0] <= self.max_posx and slist[0][0] >= self.x_init) and (slist[0][1] >= self.y_init and slist[0][1] <= self.max_posy):
            if (direction ^ self.old_direction != 3):
                #right direction right
                if (direction == 0) :
                    # last one disappear
                    del slist[-1]
                    head_list = [slist[0][0]+(self.snake_food_size+self.gap_of_snake_body), slist[0][1]]
                    slist.insert(0, head_list)
                elif (direction == 1):
                    #left direction up
                    del slist[-1]
                    head_list = [slist[0][0], slist[0][1]-(self.snake_food_size+self.gap_of_snake_body)]
                    slist.insert(0, head_list)
                elif (direction == 2):
                #left direction down
                    del slist[-1]
                    head_list = [slist[0][0], slist[0][1]+(self.snake_food_size+self.gap_of_snake_body)]
                    slist.insert(0, head_list)
                elif (direction == 3):
                #left direction left
                    del slist[-1]
                    head_list = [slist[0][0]-(self.snake_food_size+self.gap_of_snake_body), slist[0][1]]
                    slist.insert(0, head_list)

            else:
                print('d ^ od is 3')
                if (self.old_direction == 0) :
                    # last one disappear
                    del slist[-1]
                    head_list = [slist[0][0]+(self.snake_food_size+self.gap_of_snake_body), slist[0][1]]
                    slist.insert(0, head_list)
                elif (self.old_direction == 1):
                    #left direction up
                    del slist[-1]
                    head_list = [slist[0][0], slist[0][1]-(self.snake_food_size+self.gap_of_snake_body)]
                    slist.insert(0, head_list)
                elif (self.old_direction == 2):
                #left direction down
                    del slist[-1]
                    head_list = [slist[0][0], slist[0][1]+(self.snake_food_size+self.gap_of_snake_body)]
                    slist.insert(0, head_list)
                elif (self.old_direction == 3):
                #left direction left
                    del slist[-1]
                    head_list = [slist[0][0]-(self.snake_food_size+self.gap_of_snake_body), slist[0][1]]
                    slist.insert(0, head_list)

    def collide(self, qp, slist):
        #s = 'self.direction is:'+repr( self.direction) 
        #print(s)
        #t = 'snake coordinate:' + repr(self.slist[0][0]) + ','+ repr(self.slist[0][1])
        #print(t)
        #u = 'self.fcoordinate:' + repr(self.fcoordinate_list[0]) + ','+ repr(self.fcoordinate_list[1])
        #print(u)

        #collise with border
        if ((slist[0][1]+(self.snake_food_size+self.gap_of_snake_body) > self.max_posy) and (self.direction == 2))  or ((slist[0][1]-(self.snake_food_size+self.gap_of_snake_body) < 10) and (self.direction == 1)) or ((slist[0][0]+(self.snake_food_size+self.gap_of_snake_body) > self.max_posx) and  (self.direction == 0)) or  ((slist[0][0]-(self.snake_food_size+self.gap_of_snake_body) < 10) and (self.direction == 3)):
            print('out of border')
            self.dead(qp, slist)

        #collise with snake itself
        if (([slist[0][0],slist[0][1]+(self.snake_food_size+self.gap_of_snake_body)] in slist) and (self.direction == 2) and ([slist[0][0], slist[0][1]+(self.snake_food_size+self.gap_of_snake_body)] != [slist[1][0],slist[1][1]])) \
        or (([slist[0][0],slist[0][1]-(self.snake_food_size+self.gap_of_snake_body)] in slist) and (self.direction == 1) and ([slist[0][0], slist[0][1]-(self.snake_food_size+self.gap_of_snake_body)] != [slist[1][0],slist[1][1]])) \
        or (([slist[0][0]+(self.snake_food_size+self.gap_of_snake_body),slist[0][1]] in slist) and (self.direction == 0) and ([slist[0][0]+(self.snake_food_size+self.gap_of_snake_body), slist[0][1]] != [slist[1][0],slist[1][1]])) \
        or (([slist[0][0]-(self.snake_food_size+self.gap_of_snake_body),slist[0][1]] in slist) and (self.direction == 3) and ([slist[0][0]-(self.snake_food_size+self.gap_of_snake_body), slist[0][1]] != [slist[1][0],slist[1][1]])): 
        #and (self.direction ^ self.old_direction != 3):
            self.dead(qp, slist)

        # collide with food
        if ((slist[0][0] == self.fcoordinate_list[0]) and (slist[0][1]+(self.snake_food_size+self.gap_of_snake_body) == self.fcoordinate_list[1]) and (self.direction == 2)):
            #snake increases
            slist.insert(0, self.fcoordinate_list)
            print ('food collision happen down')
            #draw next food
            self.generateFoodPos()
            self.collision_tag = True

        if ((slist[0][0] == self.fcoordinate_list[0]) and (slist[0][1]-(self.snake_food_size+self.gap_of_snake_body) == self.fcoordinate_list[1]) and (self.direction == 1)):
            #snake increases
            slist.insert(0, self.fcoordinate_list)
            print ('food collision happen up')
            #draw next food
            self.generateFoodPos()
            self.collision_tag = True

        if ((slist[0][0]+(self.snake_food_size+self.gap_of_snake_body) == self.fcoordinate_list[0]) and (slist[0][1] == self.fcoordinate_list[1]) and (self.direction == 0)):
            #snake increases
            slist.insert(0, self.fcoordinate_list)
            print ('food collision happen up')
            #draw next food
            self.generateFoodPos()
            self.collision_tag = True

        if ((slist[0][0]-(self.snake_food_size+self.gap_of_snake_body) == self.fcoordinate_list[0]) and (slist[0][1] == self.fcoordinate_list[1]) and (self.direction == 3)):
            #snake increases
            slist.insert(0, self.fcoordinate_list)
            print ('food collision happen up')
            #draw next food
            self.generateFoodPos()
            self.collision_tag = True

    def dead(self,qp, slist):
        print ('snake dead!!!!!!!!!!!!!!!!!!')
        self.direction = 4
        self.food_timer.stop()# to avoid snake can move after death.

    def drawDeadSnake(self, qp, slist):
        qp.setBrush(QColor(0,255,0))
        for i in range(0, len(slist)):
            qp.drawRect(slist[i][0], slist[i][1], self.snake_food_size, self.snake_food_size)
        

    def drawRectangleBorder(self, qp):
        color = QColor(0, 0, 255)
        qp.setPen(color)
        qp.drawRect(self.x_init, self.y_init, self.rect_border_width, self.rect_border_height)

    def drawSnake(self, qp, slist):
        qp.setBrush(QColor(0,0,0))
        for i in range(0, len(slist)):
            qp.drawRect(slist[i][0], slist[i][1], self.snake_food_size, self.snake_food_size)

    def drawFood(self, qp):
        #print 'draw food'
        qp.setBrush(QColor(200,0,0))
        qp.drawRect(self.fcoordinate_list[0], self.fcoordinate_list[1], self.snake_food_size, self.snake_food_size)

    def generateFoodPos(self):
        #generate random position of food.
        polymerrization = True
        while polymerrization:
            x = random.choice(range(self.x_init, self.max_posx, (self.snake_food_size+self.gap_of_snake_body)))
            y = random.choice(range(self.y_init, self.max_posy, (self.snake_food_size+self.gap_of_snake_body)))
            self.fcoordinate_list = [x,y]
            if self.fcoordinate_list in Snake.slist:
                polymerrization = True
            else:
                polymerrization = False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Snake()

    sys.exit(app.exec_())

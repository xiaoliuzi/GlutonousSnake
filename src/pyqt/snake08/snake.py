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
    x_init = 10
    y_init = 10
    direction = [0] # initial snake move direction
    press_key_tag = 0
    snake_food_size = 30 # initial snake or food size
    gap_of_snake_body = 5
    w = 30
    h = 15 
    death_tag = 1
    snake_len = (snake_food_size+gap_of_snake_body)

    rect_border_width = ((snake_len)*w+snake_food_size)
    rect_border_height = ((snake_len)*h+snake_food_size)
    max_posx = (rect_border_width +gap_of_snake_body)
    max_posy = (rect_border_height +gap_of_snake_body)
    head_list = [(x_init+snake_len), y_init] # initial snake head
    body_list = [x_init, y_init] # initial snake body
    snake = [head_list, body_list]#initial snake coordinate
    fcoordinate_list = [(snake_len+x_init),(snake_len+y_init)]#initial food coordinate

    qp = QPainter() # general painter
    food_timer = QTimer()
    pause = False
    speed = 800 # it is ms time actually.

    def __init__(self):
        super(Snake, self).__init__()

        #for testing timer demo
        self.food_timer.timeout.connect(self.myupdate)#to update the paiter
        self.food_timer.start(self.speed)

        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 1200, 600)
        self.setWindowTitle('Glutonous Snake')

        self.show()

    def paintEvent(self, e):
        #painter can be used in paintEvent() only.
        self.qp.begin(self)

        self.drawRectangleBorder(self.qp)
        self.drawSnake(self.qp, self.snake)
        self.drawFood(self.qp)

        if self.death_tag == 4:#direction is 4 to show the snake is dead
            self.drawDeadSnake(self.qp, self.snake)

        self.qp.end()


    def keyPressEvent(self, e):
        d = 'd is:'+repr( self.direction) 
        self.press_key_tag = 1
        if e.key() == Qt.Key_Right and self.direction[0] != 3 and self.direction[0] != 0:
                self.direction[0] = 0
                print(d)
                self.myupdate()
        if e.key() == Qt.Key_Up and self.direction[0] != 2 and self.direction[0] != 1:
                self.direction[0] = 1
                print(d)
                self.myupdate()
        if e.key() == Qt.Key_Down and self.direction[0] != 1 and self.direction[0] != 2:
                self.direction[0] = 2
                print(d)
                self.myupdate()
        if e.key() == Qt.Key_Left and self.direction[0] != 0 and self.direction[0] != 3:
                self.direction[0] = 3
                print(d)
                self.myupdate()
        if e.key() == Qt.Key_Space :
                self.pause = not self.pause 
                self.myupdate()
        if e.key() == Qt.Key_Escape:
                self.close()
                self.myupdate()

    def myupdate(self):
        qrect = QRect(self.x_init, self.y_init, self.rect_border_width, self.rect_border_height)

        self.collide(self.qp, self.snake)
        self.update(qrect)
        #self.repaint()
        if self.collision_tag == False and self.pause == False and self.death_tag != 4 and self.press_key_tag == 1:
            self.move(self.snake, self.direction[0])
            self.press_key_tag = 0
            print('presskey and move')
        elif self.collision_tag == False and self.pause == False and self.death_tag != 4 and self.press_key_tag == 0:
            self.move(self.snake, self.direction[0])
            print('no press and move')
            #self.press_key_tag = 1

        self.collision_tag = False
        self.update(qrect)


    def move(self, snake, direction):
        if (snake[0][0] <= self.max_posx and snake[0][0] >= self.x_init) and (snake[0][1] >= self.y_init and snake[0][1] <= self.max_posy):
            #direction right
            if (direction == 0) :
            #last one disappear
                del snake[-1]
                head_list = [snake[0][0]+self.snake_len, snake[0][1]]
                snake.insert(0, head_list)
            elif (direction == 1):
            #direction up
                del snake[-1]
                head_list = [snake[0][0], snake[0][1]-self.snake_len]
                snake.insert(0, head_list)
            elif (direction == 2):
            #direction down
                del snake[-1]
                head_list = [snake[0][0], snake[0][1]+self.snake_len]
                snake.insert(0, head_list)
            elif (direction == 3):
            #direction left
                del snake[-1]
                head_list = [snake[0][0]-self.snake_len, snake[0][1]]
                snake.insert(0, head_list)

    def collide(self, qp, snake):
        #collise with border
        if ((snake[0][1]+self.snake_len > self.max_posy) and (self.direction[0] == 2))  \
            or ((snake[0][1]-self.snake_len < self.y_init) and (self.direction[0] == 1)) \
            or ((snake[0][0]+self.snake_len > self.max_posx) and  (self.direction[0] == 0)) \
            or  ((snake[0][0]-self.snake_len < self.x_init) and (self.direction[0] == 3)):
            print('out of border')
            self.dead(qp, snake)
            self.update()

        #collise with snake itself
        if (([snake[0][0],snake[0][1]+self.snake_len] in snake) and (self.direction[0] == 2) and ([snake[0][0], snake[0][1]+self.snake_len] != [snake[1][0],snake[1][1]])) \
        or (([snake[0][0],snake[0][1]-self.snake_len] in snake) and (self.direction[0] == 1) and ([snake[0][0], snake[0][1]-self.snake_len] != [snake[1][0],snake[1][1]])) \
        or (([snake[0][0]+self.snake_len,snake[0][1]] in snake) and (self.direction[0] == 0) and ([snake[0][0]+self.snake_len, snake[0][1]] != [snake[1][0],snake[1][1]])) \
        or (([snake[0][0]-self.snake_len,snake[0][1]] in snake) and (self.direction[0] == 3) and ([snake[0][0]-self.snake_len, snake[0][1]] != [snake[1][0],snake[1][1]])): 
            self.dead(qp, snake)

        # collide with food
        if ((snake[0][0] == self.fcoordinate_list[0]) and (snake[0][1]+self.snake_len == self.fcoordinate_list[1]) and (self.direction[0] == 2))    \
        or ((snake[0][0] == self.fcoordinate_list[0]) and (snake[0][1]-self.snake_len == self.fcoordinate_list[1]) and (self.direction[0] == 1))    \
        or ((snake[0][0]+self.snake_len == self.fcoordinate_list[0]) and (snake[0][1] == self.fcoordinate_list[1]) and (self.direction[0] == 0))    \
        or ((snake[0][0]-self.snake_len == self.fcoordinate_list[0]) and (snake[0][1] == self.fcoordinate_list[1]) and (self.direction[0] == 3)):
            #snake increases
            snake.insert(0, self.fcoordinate_list)
            print ('food collision happen down')
            #draw next food
            self.generateFoodPos()
            self.collision_tag = True

    def dead(self,qp, snake):
        print ('snake dead!!!!!!!!!!!!!!!!!!')
        self.death_tag = 4
        self.food_timer.stop()# to avoid snake can move after death.

    def drawDeadSnake(self, qp, snake):
        qp.setBrush(QColor(0,255,0))
        for i in range(0, len(snake)):
            qp.drawRect(snake[i][0], snake[i][1], self.snake_food_size, self.snake_food_size)
        

    def drawRectangleBorder(self, qp):
        color = QColor(0, 0, 255)
        qp.setPen(color)
        qp.drawRect(self.x_init, self.y_init, self.rect_border_width, self.rect_border_height)

    def drawSnake(self, qp, snake):
        qp.setBrush(QColor(0,0,0))
        for i in range(0, len(snake)):
            qp.drawRect(snake[i][0], snake[i][1], self.snake_food_size, self.snake_food_size)

    def drawFood(self, qp):
        #print 'draw food'
        qp.setBrush(QColor(200,0,0))
        qp.drawRect(self.fcoordinate_list[0], self.fcoordinate_list[1], self.snake_food_size, self.snake_food_size)

    def generateFoodPos(self):
        #generate random position of food.
        polymerrization = True
        while polymerrization:
            x = random.choice(range(self.x_init, self.max_posx, self.snake_len))
            y = random.choice(range(self.y_init, self.max_posy, self.snake_len))
            self.fcoordinate_list = [x,y]
            if self.fcoordinate_list in Snake.snake:
                polymerrization = True
            else:
                polymerrization = False

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Snake()

    sys.exit(app.exec_())

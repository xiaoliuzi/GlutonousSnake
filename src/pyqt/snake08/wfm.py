# copy write from sw
#import PyQt5 and python library
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import Qt, QTimer, QPoint, QSize, QRect
import sys, time, random




# Contants

#Refresh screen every timeout second
timeout = 500

#initial panel size
panel = QSize(30, 20)
block = QSize(20, 20)

#
directions = {
        Qt.Key_Left:    QPoint(-1,  0),
        Qt.Key_Right:   QPoint( 1,  0),
        Qt.Key_Up:      QPoint( 0, -1),
        Qt.Key_Down:    QPoint( 0,  1)
}

oppsite = {
    Qt.Key_Left:    Qt.Key_Right,
    Qt.Key_Right:   Qt.Key_Left,
    Qt.Key_Up:      Qt.Key_Down,
    Qt.Key_Down:    Qt.Key_Up
}

# Return current time in seconds as a int number.
def now():
    return int(round(time.time()*1000))



# Return a tuple of block size
def bsize()
    return block.width()-1, block.height()-1

# return the scale of the window
def scale_sz(sz)
    return sz.width() * block.width(), sz.height()* block.height()

# return the size of snake size
def scaled_pt(p):
    return p.x() * block.width(), p.y() * block.height()


# Snake controller Game
class Game(ojbect):
    def __init__(self):
        super(Snake, self).__init__()

        # init the data attribute
        self.timer  = QTimer()
        self.score  = 0
        self.dead   = False
        self.curdir = Qt.Key_Right
        self.last_update = now()

        # init the snake position

        self.snake = [[0, block.width()/2], [1, block.height()/2]]

    # start the timer
    def start_timer(self):
        self.timer.start()
    # stop the timer
    def stop_timer(self):
        self.timer.stop()
    # start the game
    def start(self, view=None):
        view = view or GameView()
        # let the view.game data point to the Game() object
        view.game = self
        self.view = view

        # generate new seed random
        self.new_seed()
        self.view.update()
        self.start_timer()

    # move one step
    def one_step(self, snake=None):
        snake = snake or self.snake
        # create a new head to check whether polymerrization or not
        d = directions[self.curdir]
        
        neck, head = snake[-2:]
        new_head = head + d
        

        
        # if new head polymerize with neck

        # if new head is dead

        # if new head is seed?

        # else new head is ordinarilly move


    # create new seed


    # test is dead or not



# GameView

    # init

    # update


    # paintevnet

    # key press event

    #clear screen and draw border

    # draw snake

    # draw seed


# main function

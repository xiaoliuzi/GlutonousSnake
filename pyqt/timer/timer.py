import sys
from PyQt4 import QtGui, QtCore

size = 0

app = QtGui.QApplication(sys.argv)

graphicsView = QtGui.QGraphicsView()
graphicsView.setWindowTitle("Timer test")

graphicsView.setGeometry(QtCore.QRect(600,300,250,250))
graphicsView.scene = QtGui.QGraphicsScene()
graphicsView.setScene(graphicsView.scene)

def draw():
    global size
    size += 1

    size2Nd = size * 1.125

    if (size >= 240):
        size = 1
    if (size2Nd >= 240):
        size2Nd = 1
    graphicsView.scene.clear()
    
    graphicsView.item = QtGui.QGraphicsEllipseItem(125 - size/2, 125 - size/2, size, size)
    graphicsView.scene.addItem(graphicsView.item)
    
    graphicsView.item = QtGui.QGraphicsEllipseItem(125 - size2Nd/2, 125 - size2Nd/2, size2Nd, size2Nd)
    graphicsView.scene.addItem(graphicsView.item)

graphicsView.show()

timer = QtCore.QTimer()
timer.timeout.connect(draw)
timer.start(6)
sys.exit(app.exec_())

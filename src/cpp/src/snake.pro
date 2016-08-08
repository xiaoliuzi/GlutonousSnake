#-------------------------------------------------
#
# Project created by QtCreator 2016-08-04T21:08:55
#
#-------------------------------------------------

QT       += core gui widgets

greaterThan(QT_MAJOR_VERSION, 4): QT += widgets

TARGET = snake
TEMPLATE = app


SOURCES += main.cpp\
        mainwindow.cpp \
    gameview.cpp \
    game.cpp \
    constant.cpp \
    test.cpp

HEADERS  += mainwindow.h \
    constant.h \
    gameview.h \
    game.h \
    test.h

FORMS    += mainwindow.ui

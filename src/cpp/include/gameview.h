#ifndef GAMEVIEW_H
#define GAMEVIEW_H

#include <QWidget>
#include <QPainter>

#include <QString>
#include <QColor>
#include <QtGui>
#include "constant.h"
#include "game.h"

class GameView : public QWidget
{
    Q_OBJECT
public:
    explicit GameView(QWidget *parent = 0);
    void update();
    void paintEvent();
    void keyReleaseEvent(QKeyEvent *event=NULL);
    void clear();
    void drawSnake(QVector<QPoint>  &snake, QColor c=QColor("gray"));
    void drawSeed(QPoint  &seed, QColor c=QColor("gray"));
    void set_game(Game *g=NULL);

private:
    QPainter qpainter;
    Game *game;
};

#endif // GAMEVIEW_H

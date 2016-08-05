#ifndef GAMEVIEW_H
#define GAMEVIEW_H

#include <QWidget>
#include <QPainter>
#include <game.h>
#include <QString>
#include <QColor>
#include <QtGui>

class Game;

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

signals:

public slots:
private:
    QPainter qpainter;
    Game *game;
};

#endif // GAMEVIEW_H

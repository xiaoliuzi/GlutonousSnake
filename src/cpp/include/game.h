#ifndef GAME_H
#define GAME_H

#include <QObject>

#include <QVector>
#include <QTimer>
#include "constant.h"
#include <ctime>


class GameView;

class Game : public QObject
{
    Q_OBJECT
public:
    explicit Game(QObject *parent = 0);
    ~Game();

    void start(GameView &view);
    void start_timer();
    void stop_timer();
    bool dead_();
    int score_();
    QVector<QPoint>& snake_();
    QPoint& seed_();

    bool is_dead(QPoint new_head);
    QPoint& new_seed();
    void control(int code);
#if 0
    bool operator==(const QPoint& p1, const QPoint& p2) {
      return p1.x() == p2.x() && p1.y() == p2.y();
    }
#endif

    bool is_in(QPoint p, QVector<QPoint> s){

        for (auto &it : s){
            if(p.x() == it.x()
                    && p.y() == it.y())
                return true;
        }

        return false;

    }
   //考虑使用函数模板,实现简单的find
#if 0
    bool is_in(int *p, QMap<int,QPoint> s){

        for (QMap<int, QPoint> &it : s){
            if(p->x() == it.second.x()
                    && p->y() == it.second.y())
                return true;
        }

        return false;

    }
#endif

signals:

public slots:
    void one_step();
private:
    int last_update;
    int score;
    QTimer *timer = new QTimer(this);
    QVector<QPoint> snake;
    bool dead;
    int curdir;
    GameView *view;
    QPoint seed;
};

#endif // GAME_H

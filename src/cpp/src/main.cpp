#include "mainwindow.h"
#include <QApplication>
#include <QWidget>
//#include <constant.h>
//#include <gameview.h>
//#include <game.h>


int main(int argc, char *argv[])
{
    QApplication a(argc, argv);

#if 0
    GameView view;
    Game start_game;
    view.setWindowTitle("Snake");
    //view.setFixedSize(scaled_sz(panel)[0], scaled_sz(panel)[1]);
    view.setFixedSize(601,401);
    view.show();

    start_game.start(view);
#endif
    QWidget w;
    QPolygon polygon;
    polygon << QPoint(10,20) << QPoint(20, 30);

    w.show();

    return a.exec();
}

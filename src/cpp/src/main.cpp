#include "mainwindow.h"
#include <QApplication>
#include <QWidget>
#include "constant.h"
#include "gameview.h"
#include "game.h"


int main(int argc, char *argv[])
{
    QApplication a(argc, argv);

    GameView *view = new GameView();
    Game *start_game = new Game();
    view->setWindowTitle("Snake");
    view->setFixedSize(scaled_sz(panel)[0], scaled_sz(panel)[1]);
    view->setFixedSize(panel.width()*block.width()+1,
                      panel.height()*block.height()+1);
    view->show();

    start_game->start(*view);

    return a.exec();
}

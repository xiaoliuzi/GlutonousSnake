#include "game.h"
#include "gameview.h"



Game::Game(QObject *parent) : QObject(parent)
{
    last_update = now();
    score = 0;
    connect(timer, SIGNAL(timeout()), this, SLOT(one_step()));
    snake.push_back(QPoint(0, panel.height()/2));
    snake.push_back(QPoint(1, panel.height()/2));
    dead = false;
    curdir = Qt::Key_Right;
    view = NULL;
}


Game::~Game(){

}
bool Game::dead_(){
    return dead;
}
int Game::score_(){
    return score;
}
QVector<QPoint>& Game::snake_(){
    return snake;
}
QPoint& Game::seed_(){
    return seed;
}

void Game::start_timer(){
    timer->start(timeout);
}
void Game::stop_timer(){
    timer->stop();
}

void Game::start(GameView &v){

    v.set_game(this);
    view = &v;

    new_seed();
    view->update();
    start_timer();
}

void Game::one_step(){
    QPoint d, new_head;
    QVector<QPoint>::iterator neck, head;
    d = directions[curdir];
    head = snake.end()-1;
    neck = snake.end()-2;
    new_head = *head + d;
    if (new_head == *neck) {
        std::reverse(snake.begin(),snake.end());

        head = snake.end()-1;
        neck = snake.end()-2;
        new_head = *head + d;
        if (new_head == *neck){
            curdir = opposite[curdir];
            d = directions[curdir];
            new_head = *head + d;
        }
    }
    if (is_dead(new_head)){
        qDebug() << "snake is dead" << endl;
        dead = true;
        view->update();
        stop_timer();
        return;
    }
    if(new_head.x() == seed.x() &&
            new_head.y() == seed.y()){
        new_seed();
        score += 1;
    }
    else{
        snake.erase(snake.begin());
    }
    snake.append(new_head);
    view->update();
    last_update = now();
}

bool Game::is_dead(QPoint new_head){
    QVector<QPoint>::iterator it = qFind(snake.begin(), snake.end(), new_head);
    return ((it != snake.end())
            && (new_head != *snake.begin())
            || new_head.x() < 0 || new_head.x() >= panel.width()
            || new_head.y() < 0 || new_head.y() >= panel.height());
}

QPoint& Game::new_seed(){
    QVector<QPoint>::iterator it;

    srand(time(0));
    while (true){
        seed = QPoint(rand()%panel.width(),rand()%panel.height());
        it= qFind(snake.begin(), snake.end(), seed);
        if (it != snake.end()) continue;
        else return seed;
    }
}

void Game::control(int code){
    if (!code) return;
    if (code == Qt::Key_Escape){
        view->close();
    }

    if (code == Qt::Key_R){
        Game new_game;
        qDebug() << "before start" << endl;

        //new_game.start();

        qDebug() << "start success" << endl;
    }

    if (dead_()) return;
    if (code == Qt::Key_Space){
        if (timer->isActive())
            stop_timer();
        else
            start_timer();
    }
	QMap<int, QPoint>::iterator it = directions.find(code);
    if (it != directions.end()){
        int olddir = curdir;
        curdir = code;
        if (olddir != curdir || ((now()-last_update) > timeout/4)){
            one_step();
            start_timer();//reset timer.
        }
    }
}


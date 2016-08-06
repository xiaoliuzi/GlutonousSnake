#include "game.h"
#include <gameview.h>



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
    QVector<QPoint>::reverse_iterator neck, head;
    d = directions[curdir];
    head = snake.rbegin();
    neck = snake.rbegin()-1;
    new_head = *head + d;
    if (new_head == *neck) {
        std::reverse(snake.begin(),snake.end());
        head = snake.rbegin();
        neck = snake.rbegin()-1;
        new_head = *head + d;
        if (new_head == *neck){
            curdir = opposite[curdir];
            d = directions[curdir];
            new_head = *head + d;
        }
    }
    if (is_dead(new_head)){
        dead = true;
        view->update();
        stop_timer();
    }
    //if (new_head == seed){
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
    return (is_in(new_head,snake)
            && (new_head != *snake.begin())
            || new_head.x() < 0 || new_head.y() >= panel.width()
            || new_head.y() < 0 || new_head.y() >= panel.width());
}

QPoint& Game::new_seed(){
    srand(time(0));
    while (true){
        seed = QPoint(rand()%panel.width(),rand()%panel.height());
        //if (snake.end() != std::find(snake.begin(), snake.end(), seed)) continue;
        if (is_in(seed,snake)) continue;
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
        new_game.start(*(this->view));
    }
    if (dead_()) return;
    if (code == Qt::Key_Space){
        if (timer->isActive())
            stop_timer();
        else
            start_timer();
    }
    //if (directions.end()!= std::find(directions.begin(), directions.end(), code)){
    //if (is_in(code, directions)){
    {
        int olddir = curdir;
        curdir = code;
        if (olddir != curdir || ((now()-last_update) > timeout/4)){
            one_step();
            start_timer();//reset timer.
        }
    }
}


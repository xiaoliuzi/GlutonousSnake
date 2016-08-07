#include "gameview.h"
#include "game.h"



GameView::GameView(QWidget *parent) : QWidget(parent)
{
    QWidget::QWidget();
    game = NULL;
}
void GameView::set_game(Game *g){
    game = g;
}

void GameView::update(){
    QWidget::update();
    if (game->dead_()){
        this->setWindowTitle("Snake Game Over");
    }
    else{
        this->setWindowTitle("Snake score =" + QString::number(game->score_(),10));
    }
}

void GameView::clear(){
    QColor color;
    color = QColor("black");
    qpainter.setPen(color);
    qpainter.drawRect(0, 0, scaled_sz(panel)[0], scaled_sz(panel)[1]);
    color = QColor("white");
    qpainter.setBrush(color);
    qpainter.drawRect(0, 0, scaled_sz(panel)[0], scaled_sz(panel)[1]);

}

void GameView::paintEvent(QPaintEvent *event){
    qpainter.begin(this);
    QColor color;
    clear();
    if (game->dead_())
        color = QColor("gray");
    drawSnake(game->snake_(), color);
    drawSeed(game->seed_(), color);
    qpainter.end();
}

void GameView::keyReleaseEvent(QKeyEvent *e){
    int code = e->key();
    //qDebug() << "key code is: " << code << endl;
    game->control(code);

}

void GameView::drawSnake( QVector<QPoint> &snake, QColor color){
    if (color != QColor("gray"))
        color = QColor("black");
    qpainter.setPen(Qt::NoPen);
    qpainter.setBrush(color);
    for (auto &it:snake){
        qpainter.drawRect(scaled_pt(it)[0], scaled_pt(it)[1],
                            bsize()[0], bsize()[1]);
    }
}

void GameView::drawSeed( QPoint &seed, QColor color){
    if (color != QColor("gray"))
        color = QColor("red");
    qpainter.setPen(Qt::NoPen);
    qpainter.setBrush(color);
    qpainter.drawRect(scaled_pt(seed)[0], scaled_pt(seed)[1],
                        bsize()[0], bsize()[1]);
}

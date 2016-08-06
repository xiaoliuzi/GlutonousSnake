#include "constant.h"

int timeout(500);
QSize panel(30, 20);
QSize block(20, 20);


// Qt.Key_A is enum
QMap<int, QPoint> directions = {
    {Qt::Key_Left,	QPoint(-1,   0)},
    {Qt::Key_Right,	QPoint( 1,   0)},
    {Qt::Key_Up,	QPoint( 0,  -1)},
    {Qt::Key_Left,	QPoint( 0,   1)}
};

QMap<int, int> opposite = {
    {Qt::Key_Left, 	Qt::Key_Right},
    {Qt::Key_Right, Qt::Key_Left},
    {Qt::Key_Up, 	Qt::Key_Down},
    {Qt::Key_Down, 	Qt::Key_Up}
};

int now(){
    return time(0);
}

QVector<int> bsize(){
    QVector<int> v;
    v.push_back(block.width()-1);
    v.push_back(block.height()-1);
    return v;
}

QVector<int> scaled_sz(QSize &sz){
    QVector<int> v;
    v.push_back(sz.width() * block.width());
    v.push_back(sz.height() * block.height());
    return v;
}

QVector<int> scaled_pt(QPoint &p){
    QVector<int> v;
    v.push_back(p.x() * block.width());
    v.push_back(p.y() * block.height());
    return v;
}

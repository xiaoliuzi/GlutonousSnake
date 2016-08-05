#ifndef CONSTANT_H
#define CONSTANT_H
#include <QMap>
#include <QPoint>
#include <QSize>
#include <ctime>
#include <QVector>

extern int timeout(500);
extern QSize panel(30, 20);
extern QSize block(20, 20);


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

int now();

QVector<int> bsize();

QVector<int> scaled_sz(int sz);

QVector<int> scaled_pt(QPoint p);

#endif // CONSTANT_H

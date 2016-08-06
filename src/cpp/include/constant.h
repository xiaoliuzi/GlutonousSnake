#ifndef CONSTANT_H
#define CONSTANT_H
#include <QMap>
#include <QPoint>
#include <QSize>
#include <ctime>
#include <QVector>

extern int timeout;
extern QSize panel;
extern QSize block;


// Qt.Key_A is enum
extern QMap<int, QPoint> directions;

extern QMap<int, int> opposite;

extern int now();

extern QVector<int> bsize();

extern QVector<int> scaled_sz(QSize &sz);

extern QVector<int> scaled_pt(QPoint &p);

#endif // CONSTANT_H

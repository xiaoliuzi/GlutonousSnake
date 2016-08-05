#include <constant.h>


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

QVector<int> scaled_pt(QPoint p){
    QVector<int> v;
    v.push_back(p.x() * block.width());
    v.push_back(p.y() * block.height());
    return v;
}

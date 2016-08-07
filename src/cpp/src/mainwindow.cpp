#include "mainwindow.h"
#include "ui_mainwindow.h"
#include <QKeyEvent>

MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{

    //setFocusPolicy(Qt::StrongFocus);///
    ui->setupUi(this);
}

MainWindow::~MainWindow()
{
    delete ui;
}


//void MainWindow::keyReleaseEvent(QKeyEvent *event){
   // event->ignore();
//}

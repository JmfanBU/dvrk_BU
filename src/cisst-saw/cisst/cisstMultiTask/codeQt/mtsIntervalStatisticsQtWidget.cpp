/* -*- Mode: C++; tab-width: 4; indent-tabs-mode: nil; c-basic-offset: 4 -*-    */
/* ex: set filetype=cpp softtabstop=4 shiftwidth=4 tabstop=4 cindent expandtab: */

/*
  Author(s):  Anton Deguet
  Created on: 2013-07-13

  (C) Copyright 2013-2017 Johns Hopkins University (JHU), All Rights Reserved.

--- begin cisst license - do not edit ---

This software is provided "as is" under an open source license, with
no warranty.  The complete license can be found in license.txt and
http://www.cisst.org/cisst/license.txt.

--- end cisst license ---
*/

#include <cisstMultiTask/mtsInterfaceRequired.h>
#include <cisstMultiTask/mtsIntervalStatisticsQtWidget.h>

#include <QHeaderView>
#include <QScrollBar>

mtsIntervalStatisticsQtWidget::mtsIntervalStatisticsQtWidget(void):
    QTableWidget()
{
    this->setRowCount(4);
    this->setColumnCount(3);
    this->verticalHeader()->hide();
    this->horizontalHeader()->hide();
    this->verticalScrollBar()->hide();
    this->horizontalScrollBar()->hide();
#if CISST_HAS_QT4
    this->horizontalHeader()->setResizeMode(QHeaderView::Stretch);
    this->verticalHeader()->setResizeMode(QHeaderView::ResizeToContents);
#else
    this->setHorizontalScrollBarPolicy(Qt::ScrollBarAlwaysOff);
    this->setVerticalScrollBarPolicy(Qt::ScrollBarAlwaysOff);
    this->horizontalHeader()->setSectionResizeMode(QHeaderView::Stretch);
    this->verticalHeader()->setSectionResizeMode(QHeaderView::ResizeToContents);
#endif
    QLabel * label;
    int rowIndex = 0;
    
    label = new QLabel("Average");
    this->setCellWidget(rowIndex, 0, label);
    QTWIAverage = new QTableWidgetItem();
    QTWIAverage->setTextAlignment(Qt::AlignRight | Qt::AlignVCenter);  
    QTWIAverage->setFlags(QTWIAverage->flags() ^ Qt::ItemIsEditable);
    this->setItem(rowIndex, 1, QTWIAverage);
    QTWIAverageHz = new QTableWidgetItem();
    QTWIAverageHz->setTextAlignment(Qt::AlignRight | Qt::AlignVCenter);
    QTWIAverageHz->setFlags(QTWIAverageHz->flags() ^ Qt::ItemIsEditable);
    this->setItem(rowIndex, 2, QTWIAverageHz);

    rowIndex++;
    label = new QLabel("Std dev");
    this->setCellWidget(rowIndex, 0, label);
    QTWIStdDev = new QTableWidgetItem();
    QTWIStdDev->setTextAlignment(Qt::AlignRight | Qt::AlignVCenter);
    QTWIStdDev->setFlags(QTWIStdDev->flags() ^ Qt::ItemIsEditable);
    this->setItem(rowIndex, 1, QTWIStdDev);

    rowIndex++;
    label = new QLabel("Range");
    this->setCellWidget(rowIndex, 0, label);
    QTWIMin = new QTableWidgetItem();
    QTWIMin->setTextAlignment(Qt::AlignRight | Qt::AlignVCenter);
    QTWIMin->setFlags(QTWIMin->flags() ^ Qt::ItemIsEditable);
    this->setItem(rowIndex, 1, QTWIMin);
    QTWIMax = new QTableWidgetItem();
    QTWIMax->setTextAlignment(Qt::AlignRight | Qt::AlignVCenter);
    QTWIMax->setFlags(QTWIMax->flags() ^ Qt::ItemIsEditable);
    this->setItem(rowIndex, 2, QTWIMax);

    rowIndex++;
    label = new QLabel("Load");
    this->setCellWidget(rowIndex, 0, label);
    QTWILoadMin = new QTableWidgetItem();
    QTWILoadMin->setTextAlignment(Qt::AlignRight | Qt::AlignVCenter);
    QTWILoadMin->setFlags(QTWILoadMin->flags() ^ Qt::ItemIsEditable);
    this->setItem(rowIndex, 1, QTWILoadMin);
    QTWILoadMax = new QTableWidgetItem();
    QTWILoadMax->setTextAlignment(Qt::AlignRight | Qt::AlignVCenter);
    QTWILoadMax->setFlags(QTWILoadMax->flags() ^ Qt::ItemIsEditable);
    this->setItem(rowIndex, 2, QTWILoadMax);

    // compute height
    int height = 0; // this->verticalHeader()->sizeHint().height() * this->rowCount();
    for (rowIndex = 0; rowIndex < this->model()->rowCount(); rowIndex++) {
        height += this->rowHeight(rowIndex);
    }
    this->setFixedHeight(height);
}

void mtsIntervalStatisticsQtWidget::SetValue(const mtsIntervalStatistics & newValue)
{
    const double avg = newValue.GetAvg();
    QTWIAverage->setText(QString("%1 ms").arg(avg * 1000.0, -6, 'f', 3));
    QTWIAverageHz->setText(QString("%1 KHz").arg(0.001 / avg, -6, 'f', 3));
    QTWIStdDev->setText(QString("%1 ms").arg(newValue.GetStdDev() * 1000.0, -6, 'f', 3));
    QTWIMin->setText(QString("%1 ms").arg(newValue.GetMin() * 1000.0, -6, 'f', 3));
    QTWIMax->setText(QString("%1 ms").arg(newValue.GetMax() * 1000.0, -6, 'f', 3));
    const double minLoad = newValue.MinComputeTime() / avg * 100.0;
    const double maxLoad = newValue.MaxComputeTime() / avg * 100.0;
    QTWILoadMin->setText(QString("%1\%").arg(minLoad, -4, 'f', 0));
    QTWILoadMax->setText(QString("%1\%").arg(maxLoad, -4, 'f', 0));
}



CMN_IMPLEMENT_SERVICES_DERIVED_ONEARG(mtsIntervalStatisticsQtWidgetComponent, mtsComponent, std::string);

mtsIntervalStatisticsQtWidgetComponent::mtsIntervalStatisticsQtWidgetComponent(const std::string & componentName, double periodInSeconds):
    mtsComponent(componentName),
    TimerPeriodInMilliseconds(periodInSeconds * 1000)
{
    // Setup CISST Interface
    mtsInterfaceRequired * interfaceRequired = AddInterfaceRequired("Component");
    if (interfaceRequired) {
        interfaceRequired->AddFunction("GetPeriodStatistics", GetPeriodStatistics);
    }
}

void mtsIntervalStatisticsQtWidgetComponent::Startup(void)
{
    startTimer(TimerPeriodInMilliseconds); // ms
}

void mtsIntervalStatisticsQtWidgetComponent::timerEvent(QTimerEvent * CMN_UNUSED(event))
{
    // make sure we should update the display
    if (this->isHidden()) {
        return;
    }

    GetPeriodStatistics(IntervalStatistics);
    mtsIntervalStatisticsQtWidget::SetValue(IntervalStatistics);
}


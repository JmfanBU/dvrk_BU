/****************************************************************************
** Meta object code from reading C++ file 'vctPlot2DOpenGLQtWidget.h'
**
** Created by: The Qt Meta Object Compiler version 67 (Qt 5.5.1)
**
** WARNING! All changes made in this file will be lost!
*****************************************************************************/

#include "../../../../src/cisst-saw/cisst/cisstVector/vctPlot2DOpenGLQtWidget.h"
#include <QtCore/qbytearray.h>
#include <QtCore/qmetatype.h>
#if !defined(Q_MOC_OUTPUT_REVISION)
#error "The header file 'vctPlot2DOpenGLQtWidget.h' doesn't include <QObject>."
#elif Q_MOC_OUTPUT_REVISION != 67
#error "This file was generated using the moc from 5.5.1. It"
#error "cannot be used with the include files from this version of Qt."
#error "(The moc has changed too much.)"
#endif

QT_BEGIN_MOC_NAMESPACE
struct qt_meta_stringdata_vctPlot2DOpenGLQtWidget_t {
    QByteArrayData data[9];
    char stringdata0[153];
};
#define QT_MOC_LITERAL(idx, ofs, len) \
    Q_STATIC_BYTE_ARRAY_DATA_HEADER_INITIALIZER_WITH_OFFSET(len, \
    qptrdiff(offsetof(qt_meta_stringdata_vctPlot2DOpenGLQtWidget_t, stringdata0) + ofs \
        - idx * sizeof(QByteArrayData)) \
    )
static const qt_meta_stringdata_vctPlot2DOpenGLQtWidget_t qt_meta_stringdata_vctPlot2DOpenGLQtWidget = {
    {
QT_MOC_LITERAL(0, 0, 23), // "vctPlot2DOpenGLQtWidget"
QT_MOC_LITERAL(1, 24, 10), // "FreezeSlot"
QT_MOC_LITERAL(2, 35, 0), // ""
QT_MOC_LITERAL(3, 36, 8), // "FitXSlot"
QT_MOC_LITERAL(4, 45, 8), // "FitYSlot"
QT_MOC_LITERAL(5, 54, 21), // "SetContinuousFitXSlot"
QT_MOC_LITERAL(6, 76, 21), // "SetContinuousFitYSlot"
QT_MOC_LITERAL(7, 98, 24), // "SetContinuousExpandYSlot"
QT_MOC_LITERAL(8, 123, 29) // "SetContinuousExpandYResetSlot"

    },
    "vctPlot2DOpenGLQtWidget\0FreezeSlot\0\0"
    "FitXSlot\0FitYSlot\0SetContinuousFitXSlot\0"
    "SetContinuousFitYSlot\0SetContinuousExpandYSlot\0"
    "SetContinuousExpandYResetSlot"
};
#undef QT_MOC_LITERAL

static const uint qt_meta_data_vctPlot2DOpenGLQtWidget[] = {

 // content:
       7,       // revision
       0,       // classname
       0,    0, // classinfo
       7,   14, // methods
       0,    0, // properties
       0,    0, // enums/sets
       0,    0, // constructors
       0,       // flags
       0,       // signalCount

 // slots: name, argc, parameters, tag, flags
       1,    1,   49,    2, 0x0a /* Public */,
       3,    0,   52,    2, 0x0a /* Public */,
       4,    0,   53,    2, 0x0a /* Public */,
       5,    1,   54,    2, 0x0a /* Public */,
       6,    1,   57,    2, 0x0a /* Public */,
       7,    1,   60,    2, 0x0a /* Public */,
       8,    0,   63,    2, 0x0a /* Public */,

 // slots: parameters
    QMetaType::Void, QMetaType::Bool,    2,
    QMetaType::Void,
    QMetaType::Void,
    QMetaType::Void, QMetaType::Bool,    2,
    QMetaType::Void, QMetaType::Bool,    2,
    QMetaType::Void, QMetaType::Bool,    2,
    QMetaType::Void,

       0        // eod
};

void vctPlot2DOpenGLQtWidget::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    if (_c == QMetaObject::InvokeMetaMethod) {
        vctPlot2DOpenGLQtWidget *_t = static_cast<vctPlot2DOpenGLQtWidget *>(_o);
        Q_UNUSED(_t)
        switch (_id) {
        case 0: _t->FreezeSlot((*reinterpret_cast< bool(*)>(_a[1]))); break;
        case 1: _t->FitXSlot(); break;
        case 2: _t->FitYSlot(); break;
        case 3: _t->SetContinuousFitXSlot((*reinterpret_cast< bool(*)>(_a[1]))); break;
        case 4: _t->SetContinuousFitYSlot((*reinterpret_cast< bool(*)>(_a[1]))); break;
        case 5: _t->SetContinuousExpandYSlot((*reinterpret_cast< bool(*)>(_a[1]))); break;
        case 6: _t->SetContinuousExpandYResetSlot(); break;
        default: ;
        }
    }
}

const QMetaObject vctPlot2DOpenGLQtWidget::staticMetaObject = {
    { &OpenGLBaseWidget::staticMetaObject, qt_meta_stringdata_vctPlot2DOpenGLQtWidget.data,
      qt_meta_data_vctPlot2DOpenGLQtWidget,  qt_static_metacall, Q_NULLPTR, Q_NULLPTR}
};


const QMetaObject *vctPlot2DOpenGLQtWidget::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *vctPlot2DOpenGLQtWidget::qt_metacast(const char *_clname)
{
    if (!_clname) return Q_NULLPTR;
    if (!strcmp(_clname, qt_meta_stringdata_vctPlot2DOpenGLQtWidget.stringdata0))
        return static_cast<void*>(const_cast< vctPlot2DOpenGLQtWidget*>(this));
    if (!strcmp(_clname, "vctPlot2DOpenGL"))
        return static_cast< vctPlot2DOpenGL*>(const_cast< vctPlot2DOpenGLQtWidget*>(this));
    return OpenGLBaseWidget::qt_metacast(_clname);
}

int vctPlot2DOpenGLQtWidget::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = OpenGLBaseWidget::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 7)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 7;
    } else if (_c == QMetaObject::RegisterMethodArgumentMetaType) {
        if (_id < 7)
            *reinterpret_cast<int*>(_a[0]) = -1;
        _id -= 7;
    }
    return _id;
}
QT_END_MOC_NAMESPACE

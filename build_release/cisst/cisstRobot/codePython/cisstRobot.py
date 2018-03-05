# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.8
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_cisstRobotPython', [dirname(__file__)])
        except ImportError:
            import _cisstRobotPython
            return _cisstRobotPython
        if fp is not None:
            try:
                _mod = imp.load_module('_cisstRobotPython', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _cisstRobotPython = swig_import_helper()
    del swig_import_helper
else:
    import _cisstRobotPython
del version_info
try:
    _swig_property = property
except NameError:
    pass  # Python < 2.2 doesn't have 'property'.


def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if (name == "thisown"):
        return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if (not static):
        object.__setattr__(self, name, value)
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr_nondynamic(self, class_type, name, static=1):
    if (name == "thisown"):
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    if (not static):
        return object.__getattr__(self, name)
    else:
        raise AttributeError(name)

def _swig_getattr(self, class_type, name):
    return _swig_getattr_nondynamic(self, class_type, name, 0)


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object:
        pass
    _newclass = 0



def _swig_setattr_nondynamic_method(set):
    def set_attr(self, name, value):
        if (name == "thisown"):
            return self.this.own(value)
        if hasattr(self, name) or (name == "this"):
            set(self, name, value)
        else:
            raise AttributeError("You cannot add attributes to %s" % self)
    return set_attr


class SwigPyIterator(object):
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _cisstRobotPython.delete_SwigPyIterator
    __del__ = lambda self: None

    def value(self):
        return _cisstRobotPython.SwigPyIterator_value(self)

    def incr(self, n=1):
        return _cisstRobotPython.SwigPyIterator_incr(self, n)

    def decr(self, n=1):
        return _cisstRobotPython.SwigPyIterator_decr(self, n)

    def distance(self, x):
        return _cisstRobotPython.SwigPyIterator_distance(self, x)

    def equal(self, x):
        return _cisstRobotPython.SwigPyIterator_equal(self, x)

    def copy(self):
        return _cisstRobotPython.SwigPyIterator_copy(self)

    def next(self):
        return _cisstRobotPython.SwigPyIterator_next(self)

    def __next__(self):
        return _cisstRobotPython.SwigPyIterator___next__(self)

    def previous(self):
        return _cisstRobotPython.SwigPyIterator_previous(self)

    def advance(self, n):
        return _cisstRobotPython.SwigPyIterator_advance(self, n)

    def __eq__(self, x):
        return _cisstRobotPython.SwigPyIterator___eq__(self, x)

    def __ne__(self, x):
        return _cisstRobotPython.SwigPyIterator___ne__(self, x)

    def __iadd__(self, n):
        return _cisstRobotPython.SwigPyIterator___iadd__(self, n)

    def __isub__(self, n):
        return _cisstRobotPython.SwigPyIterator___isub__(self, n)

    def __add__(self, n):
        return _cisstRobotPython.SwigPyIterator___add__(self, n)

    def __sub__(self, *args):
        return _cisstRobotPython.SwigPyIterator___sub__(self, *args)
    def __iter__(self):
        return self
SwigPyIterator_swigregister = _cisstRobotPython.SwigPyIterator_swigregister
SwigPyIterator_swigregister(SwigPyIterator)

import cisstCommonPython
import cisstVectorPython
class robManipulator(object):
    """Proxy of C++ robManipulator class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    ESUCCESS = _cisstRobotPython.robManipulator_ESUCCESS
    EFAILURE = _cisstRobotPython.robManipulator_EFAILURE
    Rtw0 = _swig_property(_cisstRobotPython.robManipulator_Rtw0_get, _cisstRobotPython.robManipulator_Rtw0_set)
    Jn = _swig_property(_cisstRobotPython.robManipulator_Jn_get, _cisstRobotPython.robManipulator_Jn_set)
    Js = _swig_property(_cisstRobotPython.robManipulator_Js_get, _cisstRobotPython.robManipulator_Js_set)
    links = _swig_property(_cisstRobotPython.robManipulator_links_get, _cisstRobotPython.robManipulator_links_set)

    def LoadRobot(self, *args):
        """
        LoadRobot(robManipulator self, std::string const & linkfile) -> robManipulator::Errno
        LoadRobot(robManipulator self, Json::Value const & config) -> robManipulator::Errno
        LoadRobot(robManipulator self, std::vector< robKinematics *,std::allocator< robKinematics * > > KinParms) -> robManipulator::Errno
        """
        return _cisstRobotPython.robManipulator_LoadRobot(self, *args)


    def JacobianBody(self, *args):
        """
        JacobianBody(robManipulator self, vctDynamicVector< double > const & q)
        JacobianBody(robManipulator self, vctDynamicVector< double > const & q, vctDynamicMatrix< double > & J) -> bool
        """
        return _cisstRobotPython.robManipulator_JacobianBody(self, *args)


    def JacobianSpatial(self, *args):
        """
        JacobianSpatial(robManipulator self, vctDynamicVector< double > const & q)
        JacobianSpatial(robManipulator self, vctDynamicVector< double > const & q, vctDynamicMatrix< double > & J) -> bool
        """
        return _cisstRobotPython.robManipulator_JacobianSpatial(self, *args)


    def RNE(self, q, qd, qdd, f, g=9.81):
        """
        RNE(robManipulator self, vctDynamicVector< double > const & q, vctDynamicVector< double > const & qd, vctDynamicVector< double > const & qdd, vctFixedSizeVector< double,6 > const & f, double g=9.81) -> vctDynamicVector< double >
        RNE(robManipulator self, vctDynamicVector< double > const & q, vctDynamicVector< double > const & qd, vctDynamicVector< double > const & qdd, vctFixedSizeVector< double,6 > const & f) -> vctDynamicVector< double >
        """
        return _cisstRobotPython.robManipulator_RNE(self, q, qd, qdd, f, g)


    def CCG(self, q, qd):
        """CCG(robManipulator self, vctDynamicVector< double > const & q, vctDynamicVector< double > const & qd) -> vctDynamicVector< double >"""
        return _cisstRobotPython.robManipulator_CCG(self, q, qd)


    def BiasAcceleration(self, q, qd):
        """BiasAcceleration(robManipulator self, vctDynamicVector< double > const & q, vctDynamicVector< double > const & qd) -> vctFixedSizeVector< double,6 >"""
        return _cisstRobotPython.robManipulator_BiasAcceleration(self, q, qd)


    def JSinertia(self, *args):
        """
        JSinertia(robManipulator self, double ** A, vctDynamicVector< double > const & q)
        JSinertia(robManipulator self, vctDynamicVector< double > const & q) -> vctDynamicMatrix< double >
        """
        return _cisstRobotPython.robManipulator_JSinertia(self, *args)


    def OSinertia(self, Ac, q):
        """OSinertia(robManipulator self, double [6][6] Ac, vctDynamicVector< double > const & q)"""
        return _cisstRobotPython.robManipulator_OSinertia(self, Ac, q)


    def SE3Difference(self, Rt1, Rt2):
        """SE3Difference(robManipulator self, vctFrame4x4< double > const & Rt1, vctFrame4x4< double > const & Rt2) -> vctFixedSizeMatrix< double,4,4 >"""
        return _cisstRobotPython.robManipulator_SE3Difference(self, Rt1, Rt2)


    def AddIdentificationColumn(self, J, delRt):
        """AddIdentificationColumn(robManipulator self, vctDynamicMatrix< double > & J, vctFixedSizeMatrix< double,4,4 > & delRt)"""
        return _cisstRobotPython.robManipulator_AddIdentificationColumn(self, J, delRt)

    L0 = _cisstRobotPython.robManipulator_L0
    L1 = _cisstRobotPython.robManipulator_L1
    L2 = _cisstRobotPython.robManipulator_L2
    L3 = _cisstRobotPython.robManipulator_L3
    L4 = _cisstRobotPython.robManipulator_L4
    L5 = _cisstRobotPython.robManipulator_L5
    L6 = _cisstRobotPython.robManipulator_L6
    L7 = _cisstRobotPython.robManipulator_L7
    L8 = _cisstRobotPython.robManipulator_L8
    L9 = _cisstRobotPython.robManipulator_L9
    LN = _cisstRobotPython.robManipulator_LN

    def __init__(self, *args):
        """
        __init__(robManipulator self, vctFrame4x4< double > const & Rtw0) -> robManipulator
        __init__(robManipulator self) -> robManipulator
        __init__(robManipulator self, std::string const & robotfilename, vctFrame4x4< double > const & Rtw0) -> robManipulator
        __init__(robManipulator self, std::string const & robotfilename) -> robManipulator
        __init__(robManipulator self, std::vector< robKinematics *,std::allocator< robKinematics * > > const linkParms, vctFrame4x4< double > const & Rtw0) -> robManipulator
        __init__(robManipulator self, std::vector< robKinematics *,std::allocator< robKinematics * > > const linkParms) -> robManipulator
        """
        this = _cisstRobotPython.new_robManipulator(*args)
        try:
            self.this.append(this)
        except Exception:
            self.this = this
    __swig_destroy__ = _cisstRobotPython.delete_robManipulator
    __del__ = lambda self: None

    def ForwardKinematics(self, q, N=-1):
        """
        ForwardKinematics(robManipulator self, vctDynamicVector< double > const & q, int N=-1) -> vctFrame4x4< double >
        ForwardKinematics(robManipulator self, vctDynamicVector< double > const & q) -> vctFrame4x4< double >
        """
        return _cisstRobotPython.robManipulator_ForwardKinematics(self, q, N)


    def InverseKinematics(self, *args):
        """
        InverseKinematics(robManipulator self, vctDynamicVector< double > & q, vctFrame4x4< double > const & Rts, double tolerance=1e-12, size_t Niteration=1000, double LAMBDA=0.001) -> robManipulator::Errno
        InverseKinematics(robManipulator self, vctDynamicVector< double > & q, vctFrame4x4< double > const & Rts, double tolerance=1e-12, size_t Niteration=1000) -> robManipulator::Errno
        InverseKinematics(robManipulator self, vctDynamicVector< double > & q, vctFrame4x4< double > const & Rts, double tolerance=1e-12) -> robManipulator::Errno
        InverseKinematics(robManipulator self, vctDynamicVector< double > & q, vctFrame4x4< double > const & Rts) -> robManipulator::Errno
        InverseKinematics(robManipulator self, vctDynamicVector< double > & q, vctFrm3 Rts, double tolerance=1e-12, size_t Niteration=1000) -> robManipulator::Errno
        InverseKinematics(robManipulator self, vctDynamicVector< double > & q, vctFrm3 Rts, double tolerance=1e-12) -> robManipulator::Errno
        InverseKinematics(robManipulator self, vctDynamicVector< double > & q, vctFrm3 Rts) -> robManipulator::Errno
        """
        return _cisstRobotPython.robManipulator_InverseKinematics(self, *args)


    def NormalizeAngles(self, q):
        """NormalizeAngles(robManipulator self, vctDynamicVector< double > & q)"""
        return _cisstRobotPython.robManipulator_NormalizeAngles(self, q)


    def InverseDynamics(self, *args):
        """
        InverseDynamics(robManipulator self, vctDynamicVector< double > const & q, vctDynamicVector< double > const & qd, vctDynamicVector< double > const & qdd) -> vctDynamicVector< double >
        InverseDynamics(robManipulator self, vctDynamicVector< double > const & q, vctDynamicVector< double > const & qd, vctFixedSizeVector< double,6 > const & vdwd) -> vctDynamicVector< double >
        """
        return _cisstRobotPython.robManipulator_InverseDynamics(self, *args)


    def JacobianKinematicsIdentification(self, q, epsilon=1e-6):
        """
        JacobianKinematicsIdentification(robManipulator self, vctDynamicVector< double > const & q, double epsilon=1e-6) -> vctDynamicMatrix< double >
        JacobianKinematicsIdentification(robManipulator self, vctDynamicVector< double > const & q) -> vctDynamicMatrix< double >
        """
        return _cisstRobotPython.robManipulator_JacobianKinematicsIdentification(self, q, epsilon)


    def PrintKinematics(self, os):
        """PrintKinematics(robManipulator self, ostream os)"""
        return _cisstRobotPython.robManipulator_PrintKinematics(self, os)


    def Attach(self, tool):
        """Attach(robManipulator self, robManipulator tool)"""
        return _cisstRobotPython.robManipulator_Attach(self, tool)

robManipulator_swigregister = _cisstRobotPython.robManipulator_swigregister
robManipulator_swigregister(robManipulator)

class robLink(object):
    """Proxy of C++ robLink class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    ESUCCESS = _cisstRobotPython.robLink_ESUCCESS
    EFAILURE = _cisstRobotPython.robLink_EFAILURE

    def __init__(self, *args):
        """
        __init__(robLink self) -> robLink
        __init__(robLink self, robLink link) -> robLink
        __init__(robLink self, robKinematics kinematics, robMass const & mass) -> robLink
        """
        this = _cisstRobotPython.new_robLink(*args)
        try:
            self.this.append(this)
        except Exception:
            self.this = this
    __swig_destroy__ = _cisstRobotPython.delete_robLink
    __del__ = lambda self: None

    def Read(self, *args):
        """
        Read(robLink self, istream arg2) -> robLink::Errno
        Read(robLink self, Json::Value const & linkConfig) -> robLink::Errno
        """
        return _cisstRobotPython.robLink_Read(self, *args)


    def Write(self, os):
        """Write(robLink self, ostream os) -> robLink::Errno"""
        return _cisstRobotPython.robLink_Write(self, os)


    def ForwardKinematics(self, q):
        """ForwardKinematics(robLink self, double q) -> vctFrame4x4< double >"""
        return _cisstRobotPython.robLink_ForwardKinematics(self, q)


    def PStar(self):
        """PStar(robLink self) -> vctFixedSizeVector< double,3 >"""
        return _cisstRobotPython.robLink_PStar(self)


    def Orientation(self, q):
        """Orientation(robLink self, double q) -> vctMatrixRotation3< double >"""
        return _cisstRobotPython.robLink_Orientation(self, q)


    def GetKinematics(self):
        """GetKinematics(robLink self) -> robKinematics"""
        return _cisstRobotPython.robLink_GetKinematics(self)


    def GetMass(self):
        """GetMass(robLink self) -> robMass"""
        return _cisstRobotPython.robLink_GetMass(self)


    def GetConvention(self):
        """GetConvention(robLink self) -> robKinematics::Convention"""
        return _cisstRobotPython.robLink_GetConvention(self)


    def GetType(self):
        """GetType(robLink self) -> robJoint::Type"""
        return _cisstRobotPython.robLink_GetType(self)


    def Mass(self):
        """Mass(robLink self) -> double"""
        return _cisstRobotPython.robLink_Mass(self)


    def CenterOfMass(self):
        """CenterOfMass(robLink self) -> vctFixedSizeVector< double,3 >"""
        return _cisstRobotPython.robLink_CenterOfMass(self)


    def MomentOfInertiaAtCOM(self):
        """MomentOfInertiaAtCOM(robLink self) -> vctFixedSizeMatrix< double,3,3 >"""
        return _cisstRobotPython.robLink_MomentOfInertiaAtCOM(self)


    def MomentOfInertia(self):
        """MomentOfInertia(robLink self) -> vctFixedSizeMatrix< double,3,3 >"""
        return _cisstRobotPython.robLink_MomentOfInertia(self)


    def PositionMin(self):
        """PositionMin(robLink self) -> double"""
        return _cisstRobotPython.robLink_PositionMin(self)


    def PositionMax(self):
        """PositionMax(robLink self) -> double"""
        return _cisstRobotPython.robLink_PositionMax(self)


    def ForceTorqueMax(self):
        """ForceTorqueMax(robLink self) -> double"""
        return _cisstRobotPython.robLink_ForceTorqueMax(self)

robLink_swigregister = _cisstRobotPython.robLink_swigregister
robLink_swigregister(robLink)

class robLinkVector(object):
    """Proxy of C++ std::vector<(robLink)> class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def iterator(self):
        """iterator(robLinkVector self) -> SwigPyIterator"""
        return _cisstRobotPython.robLinkVector_iterator(self)

    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        """__nonzero__(robLinkVector self) -> bool"""
        return _cisstRobotPython.robLinkVector___nonzero__(self)


    def __bool__(self):
        """__bool__(robLinkVector self) -> bool"""
        return _cisstRobotPython.robLinkVector___bool__(self)


    def __len__(self):
        """__len__(robLinkVector self) -> std::vector< robLink >::size_type"""
        return _cisstRobotPython.robLinkVector___len__(self)


    def __getslice__(self, i, j):
        """__getslice__(robLinkVector self, std::vector< robLink >::difference_type i, std::vector< robLink >::difference_type j) -> robLinkVector"""
        return _cisstRobotPython.robLinkVector___getslice__(self, i, j)


    def __setslice__(self, *args):
        """
        __setslice__(robLinkVector self, std::vector< robLink >::difference_type i, std::vector< robLink >::difference_type j)
        __setslice__(robLinkVector self, std::vector< robLink >::difference_type i, std::vector< robLink >::difference_type j, robLinkVector v)
        """
        return _cisstRobotPython.robLinkVector___setslice__(self, *args)


    def __delslice__(self, i, j):
        """__delslice__(robLinkVector self, std::vector< robLink >::difference_type i, std::vector< robLink >::difference_type j)"""
        return _cisstRobotPython.robLinkVector___delslice__(self, i, j)


    def __delitem__(self, *args):
        """
        __delitem__(robLinkVector self, std::vector< robLink >::difference_type i)
        __delitem__(robLinkVector self, PySliceObject * slice)
        """
        return _cisstRobotPython.robLinkVector___delitem__(self, *args)


    def __getitem__(self, *args):
        """
        __getitem__(robLinkVector self, PySliceObject * slice) -> robLinkVector
        __getitem__(robLinkVector self, std::vector< robLink >::difference_type i) -> robLink
        """
        return _cisstRobotPython.robLinkVector___getitem__(self, *args)


    def __setitem__(self, *args):
        """
        __setitem__(robLinkVector self, PySliceObject * slice, robLinkVector v)
        __setitem__(robLinkVector self, PySliceObject * slice)
        __setitem__(robLinkVector self, std::vector< robLink >::difference_type i, robLink x)
        """
        return _cisstRobotPython.robLinkVector___setitem__(self, *args)


    def pop(self):
        """pop(robLinkVector self) -> robLink"""
        return _cisstRobotPython.robLinkVector_pop(self)


    def append(self, x):
        """append(robLinkVector self, robLink x)"""
        return _cisstRobotPython.robLinkVector_append(self, x)


    def empty(self):
        """empty(robLinkVector self) -> bool"""
        return _cisstRobotPython.robLinkVector_empty(self)


    def size(self):
        """size(robLinkVector self) -> std::vector< robLink >::size_type"""
        return _cisstRobotPython.robLinkVector_size(self)


    def swap(self, v):
        """swap(robLinkVector self, robLinkVector v)"""
        return _cisstRobotPython.robLinkVector_swap(self, v)


    def begin(self):
        """begin(robLinkVector self) -> std::vector< robLink >::iterator"""
        return _cisstRobotPython.robLinkVector_begin(self)


    def end(self):
        """end(robLinkVector self) -> std::vector< robLink >::iterator"""
        return _cisstRobotPython.robLinkVector_end(self)


    def rbegin(self):
        """rbegin(robLinkVector self) -> std::vector< robLink >::reverse_iterator"""
        return _cisstRobotPython.robLinkVector_rbegin(self)


    def rend(self):
        """rend(robLinkVector self) -> std::vector< robLink >::reverse_iterator"""
        return _cisstRobotPython.robLinkVector_rend(self)


    def clear(self):
        """clear(robLinkVector self)"""
        return _cisstRobotPython.robLinkVector_clear(self)


    def get_allocator(self):
        """get_allocator(robLinkVector self) -> std::vector< robLink >::allocator_type"""
        return _cisstRobotPython.robLinkVector_get_allocator(self)


    def pop_back(self):
        """pop_back(robLinkVector self)"""
        return _cisstRobotPython.robLinkVector_pop_back(self)


    def erase(self, *args):
        """
        erase(robLinkVector self, std::vector< robLink >::iterator pos) -> std::vector< robLink >::iterator
        erase(robLinkVector self, std::vector< robLink >::iterator first, std::vector< robLink >::iterator last) -> std::vector< robLink >::iterator
        """
        return _cisstRobotPython.robLinkVector_erase(self, *args)


    def __init__(self, *args):
        """
        __init__(std::vector<(robLink)> self) -> robLinkVector
        __init__(std::vector<(robLink)> self, robLinkVector arg2) -> robLinkVector
        __init__(std::vector<(robLink)> self, std::vector< robLink >::size_type size) -> robLinkVector
        __init__(std::vector<(robLink)> self, std::vector< robLink >::size_type size, robLink value) -> robLinkVector
        """
        this = _cisstRobotPython.new_robLinkVector(*args)
        try:
            self.this.append(this)
        except Exception:
            self.this = this

    def push_back(self, x):
        """push_back(robLinkVector self, robLink x)"""
        return _cisstRobotPython.robLinkVector_push_back(self, x)


    def front(self):
        """front(robLinkVector self) -> robLink"""
        return _cisstRobotPython.robLinkVector_front(self)


    def back(self):
        """back(robLinkVector self) -> robLink"""
        return _cisstRobotPython.robLinkVector_back(self)


    def assign(self, n, x):
        """assign(robLinkVector self, std::vector< robLink >::size_type n, robLink x)"""
        return _cisstRobotPython.robLinkVector_assign(self, n, x)


    def resize(self, *args):
        """
        resize(robLinkVector self, std::vector< robLink >::size_type new_size)
        resize(robLinkVector self, std::vector< robLink >::size_type new_size, robLink x)
        """
        return _cisstRobotPython.robLinkVector_resize(self, *args)


    def insert(self, *args):
        """
        insert(robLinkVector self, std::vector< robLink >::iterator pos, robLink x) -> std::vector< robLink >::iterator
        insert(robLinkVector self, std::vector< robLink >::iterator pos, std::vector< robLink >::size_type n, robLink x)
        """
        return _cisstRobotPython.robLinkVector_insert(self, *args)


    def reserve(self, n):
        """reserve(robLinkVector self, std::vector< robLink >::size_type n)"""
        return _cisstRobotPython.robLinkVector_reserve(self, n)


    def capacity(self):
        """capacity(robLinkVector self) -> std::vector< robLink >::size_type"""
        return _cisstRobotPython.robLinkVector_capacity(self)

    __swig_destroy__ = _cisstRobotPython.delete_robLinkVector
    __del__ = lambda self: None
robLinkVector_swigregister = _cisstRobotPython.robLinkVector_swigregister
robLinkVector_swigregister(robLinkVector)

class robJoint(object):
    """Proxy of C++ robJoint class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    UNDEFINED = _cisstRobotPython.robJoint_UNDEFINED
    HINGE = _cisstRobotPython.robJoint_HINGE
    SLIDER = _cisstRobotPython.robJoint_SLIDER
    UNIVERSAL = _cisstRobotPython.robJoint_UNIVERSAL
    BALLSOCKET = _cisstRobotPython.robJoint_BALLSOCKET
    ACTIVE = _cisstRobotPython.robJoint_ACTIVE
    PASSIVE = _cisstRobotPython.robJoint_PASSIVE
    ESUCCESS = _cisstRobotPython.robJoint_ESUCCESS
    EFAILURE = _cisstRobotPython.robJoint_EFAILURE

    def __init__(self, *args):
        """
        __init__(robJoint self) -> robJoint
        __init__(robJoint self, robJoint::Type type, robJoint::Mode mode, double offset, double min, double max, double ftmax) -> robJoint
        """
        this = _cisstRobotPython.new_robJoint(*args)
        try:
            self.this.append(this)
        except Exception:
            self.this = this

    def GetType(self):
        """GetType(robJoint self) -> robJoint::Type"""
        return _cisstRobotPython.robJoint_GetType(self)


    def GetMode(self):
        """GetMode(robJoint self) -> robJoint::Mode"""
        return _cisstRobotPython.robJoint_GetMode(self)


    def GetPosition(self):
        """GetPosition(robJoint self) -> double"""
        return _cisstRobotPython.robJoint_GetPosition(self)


    def GetVelocity(self):
        """GetVelocity(robJoint self) -> double"""
        return _cisstRobotPython.robJoint_GetVelocity(self)


    def GetForceTorque(self):
        """GetForceTorque(robJoint self) -> double"""
        return _cisstRobotPython.robJoint_GetForceTorque(self)


    def SetPosition(self, q):
        """SetPosition(robJoint self, double q)"""
        return _cisstRobotPython.robJoint_SetPosition(self, q)


    def SetVelocity(self, qd):
        """SetVelocity(robJoint self, double qd)"""
        return _cisstRobotPython.robJoint_SetVelocity(self, qd)


    def SetForceTorque(self, ft):
        """SetForceTorque(robJoint self, double ft)"""
        return _cisstRobotPython.robJoint_SetForceTorque(self, ft)


    def PositionOffset(self):
        """PositionOffset(robJoint self) -> double"""
        return _cisstRobotPython.robJoint_PositionOffset(self)


    def SetPositionOffset(self, offset):
        """SetPositionOffset(robJoint self, double const offset)"""
        return _cisstRobotPython.robJoint_SetPositionOffset(self, offset)


    def PositionMin(self):
        """PositionMin(robJoint self) -> double"""
        return _cisstRobotPython.robJoint_PositionMin(self)


    def PositionMax(self):
        """PositionMax(robJoint self) -> double"""
        return _cisstRobotPython.robJoint_PositionMax(self)


    def ForceTorqueMax(self):
        """ForceTorqueMax(robJoint self) -> double"""
        return _cisstRobotPython.robJoint_ForceTorqueMax(self)


    def Read(self, *args):
        """
        Read(robJoint self, istream arg2) -> robJoint::Errno
        Read(robJoint self, Json::Value const & config) -> robJoint::Errno
        """
        return _cisstRobotPython.robJoint_Read(self, *args)


    def Write(self, os):
        """Write(robJoint self, ostream os) -> robJoint::Errno"""
        return _cisstRobotPython.robJoint_Write(self, os)

    __swig_destroy__ = _cisstRobotPython.delete_robJoint
    __del__ = lambda self: None
robJoint_swigregister = _cisstRobotPython.robJoint_swigregister
robJoint_swigregister(robJoint)

class robKinematics(robJoint):
    """Proxy of C++ robKinematics class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    UNDEFINED = _cisstRobotPython.robKinematics_UNDEFINED
    STANDARD_DH = _cisstRobotPython.robKinematics_STANDARD_DH
    MODIFIED_DH = _cisstRobotPython.robKinematics_MODIFIED_DH
    HAYATI = _cisstRobotPython.robKinematics_HAYATI
    MODIFIED_HAYATI = _cisstRobotPython.robKinematics_MODIFIED_HAYATI
    __swig_destroy__ = _cisstRobotPython.delete_robKinematics
    __del__ = lambda self: None

    def GetConvention(self):
        """GetConvention(robKinematics self) -> robKinematics::Convention"""
        return _cisstRobotPython.robKinematics_GetConvention(self)


    def Read(self, *args):
        """
        Read(robKinematics self, istream arg2) -> robKinematics::Errno
        Read(robKinematics self, Json::Value const & config) -> robKinematics::Errno
        """
        return _cisstRobotPython.robKinematics_Read(self, *args)


    def ForwardKinematics(self, q):
        """ForwardKinematics(robKinematics self, double q) -> vctFrame4x4< double >"""
        return _cisstRobotPython.robKinematics_ForwardKinematics(self, q)


    def Orientation(self, q):
        """Orientation(robKinematics self, double q) -> vctMatrixRotation3< double >"""
        return _cisstRobotPython.robKinematics_Orientation(self, q)


    def PStar(self):
        """PStar(robKinematics self) -> vctFixedSizeVector< double,3 >"""
        return _cisstRobotPython.robKinematics_PStar(self)


    def Clone(self):
        """Clone(robKinematics self) -> robKinematics"""
        return _cisstRobotPython.robKinematics_Clone(self)


    def Instantiate(type):
        """Instantiate(std::string const & type) -> robKinematics"""
        return _cisstRobotPython.robKinematics_Instantiate(type)

    Instantiate = staticmethod(Instantiate)
robKinematics_swigregister = _cisstRobotPython.robKinematics_swigregister
robKinematics_swigregister(robKinematics)

def robKinematics_Instantiate(type):
    """robKinematics_Instantiate(std::string const & type) -> robKinematics"""
    return _cisstRobotPython.robKinematics_Instantiate(type)

class robDH(robKinematics):
    """Proxy of C++ robDH class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        """
        __init__(robDH self) -> robDH
        __init__(robDH self, double alpha, double a, double theta, double d, robJoint joint) -> robDH
        """
        this = _cisstRobotPython.new_robDH(*args)
        try:
            self.this.append(this)
        except Exception:
            self.this = this
    __swig_destroy__ = _cisstRobotPython.delete_robDH
    __del__ = lambda self: None

    def GetRotationX(self):
        """GetRotationX(robDH self) -> double"""
        return _cisstRobotPython.robDH_GetRotationX(self)


    def GetRotationZ(self):
        """GetRotationZ(robDH self) -> double"""
        return _cisstRobotPython.robDH_GetRotationZ(self)


    def GetTranslationX(self):
        """GetTranslationX(robDH self) -> double"""
        return _cisstRobotPython.robDH_GetTranslationX(self)


    def GetTranslationZ(self):
        """GetTranslationZ(robDH self) -> double"""
        return _cisstRobotPython.robDH_GetTranslationZ(self)


    def SetRotationX(self, x):
        """SetRotationX(robDH self, double x)"""
        return _cisstRobotPython.robDH_SetRotationX(self, x)


    def SetRotationZ(self, x):
        """SetRotationZ(robDH self, double x)"""
        return _cisstRobotPython.robDH_SetRotationZ(self, x)


    def SetTranslationX(self, x):
        """SetTranslationX(robDH self, double x)"""
        return _cisstRobotPython.robDH_SetTranslationX(self, x)


    def SetTranslationZ(self, x):
        """SetTranslationZ(robDH self, double x)"""
        return _cisstRobotPython.robDH_SetTranslationZ(self, x)

robDH_swigregister = _cisstRobotPython.robDH_swigregister
robDH_swigregister(robDH)

class robModifiedDH(robKinematics):
    """Proxy of C++ robModifiedDH class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        """
        __init__(robModifiedDH self) -> robModifiedDH
        __init__(robModifiedDH self, double alpha, double a, double theta, double d, robJoint joint) -> robModifiedDH
        """
        this = _cisstRobotPython.new_robModifiedDH(*args)
        try:
            self.this.append(this)
        except Exception:
            self.this = this
    __swig_destroy__ = _cisstRobotPython.delete_robModifiedDH
    __del__ = lambda self: None

    def GetRotationX(self):
        """GetRotationX(robModifiedDH self) -> double"""
        return _cisstRobotPython.robModifiedDH_GetRotationX(self)


    def GetRotationZ(self):
        """GetRotationZ(robModifiedDH self) -> double"""
        return _cisstRobotPython.robModifiedDH_GetRotationZ(self)


    def GetTranslationX(self):
        """GetTranslationX(robModifiedDH self) -> double"""
        return _cisstRobotPython.robModifiedDH_GetTranslationX(self)


    def GetTranslationZ(self):
        """GetTranslationZ(robModifiedDH self) -> double"""
        return _cisstRobotPython.robModifiedDH_GetTranslationZ(self)


    def SetRotationX(self, x):
        """SetRotationX(robModifiedDH self, double x)"""
        return _cisstRobotPython.robModifiedDH_SetRotationX(self, x)


    def SetRotationZ(self, x):
        """SetRotationZ(robModifiedDH self, double x)"""
        return _cisstRobotPython.robModifiedDH_SetRotationZ(self, x)


    def SetTranslationX(self, x):
        """SetTranslationX(robModifiedDH self, double x)"""
        return _cisstRobotPython.robModifiedDH_SetTranslationX(self, x)


    def SetTranslationZ(self, x):
        """SetTranslationZ(robModifiedDH self, double x)"""
        return _cisstRobotPython.robModifiedDH_SetTranslationZ(self, x)

robModifiedDH_swigregister = _cisstRobotPython.robModifiedDH_swigregister
robModifiedDH_swigregister(robModifiedDH)

class robHayati(robKinematics):
    """Proxy of C++ robHayati class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        """
        __init__(robHayati self) -> robHayati
        __init__(robHayati self, double alpha, double beta, double theta, double d, robJoint joint) -> robHayati
        """
        this = _cisstRobotPython.new_robHayati(*args)
        try:
            self.this.append(this)
        except Exception:
            self.this = this
    __swig_destroy__ = _cisstRobotPython.delete_robHayati
    __del__ = lambda self: None

    def GetRotationX(self):
        """GetRotationX(robHayati self) -> double"""
        return _cisstRobotPython.robHayati_GetRotationX(self)


    def GetRotationY(self):
        """GetRotationY(robHayati self) -> double"""
        return _cisstRobotPython.robHayati_GetRotationY(self)


    def GetRotationZ(self):
        """GetRotationZ(robHayati self) -> double"""
        return _cisstRobotPython.robHayati_GetRotationZ(self)


    def GetTranslationX(self):
        """GetTranslationX(robHayati self) -> double"""
        return _cisstRobotPython.robHayati_GetTranslationX(self)


    def GetTranslationZ(self):
        """GetTranslationZ(robHayati self) -> double"""
        return _cisstRobotPython.robHayati_GetTranslationZ(self)


    def SetRotationX(self, x):
        """SetRotationX(robHayati self, double x)"""
        return _cisstRobotPython.robHayati_SetRotationX(self, x)


    def SetRotationY(self, x):
        """SetRotationY(robHayati self, double x)"""
        return _cisstRobotPython.robHayati_SetRotationY(self, x)


    def SetRotationZ(self, x):
        """SetRotationZ(robHayati self, double x)"""
        return _cisstRobotPython.robHayati_SetRotationZ(self, x)


    def SetTranslationX(self, x):
        """SetTranslationX(robHayati self, double x)"""
        return _cisstRobotPython.robHayati_SetTranslationX(self, x)


    def SetTranslationZ(self, x):
        """SetTranslationZ(robHayati self, double x)"""
        return _cisstRobotPython.robHayati_SetTranslationZ(self, x)

robHayati_swigregister = _cisstRobotPython.robHayati_swigregister
robHayati_swigregister(robHayati)




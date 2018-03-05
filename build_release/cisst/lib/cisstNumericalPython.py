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
            fp, pathname, description = imp.find_module('_cisstNumericalPython', [dirname(__file__)])
        except ImportError:
            import _cisstNumericalPython
            return _cisstNumericalPython
        if fp is not None:
            try:
                _mod = imp.load_module('_cisstNumericalPython', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _cisstNumericalPython = swig_import_helper()
    del swig_import_helper
else:
    import _cisstNumericalPython
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
    __swig_destroy__ = _cisstNumericalPython.delete_SwigPyIterator
    __del__ = lambda self: None

    def value(self):
        return _cisstNumericalPython.SwigPyIterator_value(self)

    def incr(self, n=1):
        return _cisstNumericalPython.SwigPyIterator_incr(self, n)

    def decr(self, n=1):
        return _cisstNumericalPython.SwigPyIterator_decr(self, n)

    def distance(self, x):
        return _cisstNumericalPython.SwigPyIterator_distance(self, x)

    def equal(self, x):
        return _cisstNumericalPython.SwigPyIterator_equal(self, x)

    def copy(self):
        return _cisstNumericalPython.SwigPyIterator_copy(self)

    def next(self):
        return _cisstNumericalPython.SwigPyIterator_next(self)

    def __next__(self):
        return _cisstNumericalPython.SwigPyIterator___next__(self)

    def previous(self):
        return _cisstNumericalPython.SwigPyIterator_previous(self)

    def advance(self, n):
        return _cisstNumericalPython.SwigPyIterator_advance(self, n)

    def __eq__(self, x):
        return _cisstNumericalPython.SwigPyIterator___eq__(self, x)

    def __ne__(self, x):
        return _cisstNumericalPython.SwigPyIterator___ne__(self, x)

    def __iadd__(self, n):
        return _cisstNumericalPython.SwigPyIterator___iadd__(self, n)

    def __isub__(self, n):
        return _cisstNumericalPython.SwigPyIterator___isub__(self, n)

    def __add__(self, n):
        return _cisstNumericalPython.SwigPyIterator___add__(self, n)

    def __sub__(self, *args):
        return _cisstNumericalPython.SwigPyIterator___sub__(self, *args)
    def __iter__(self):
        return self
SwigPyIterator_swigregister = _cisstNumericalPython.SwigPyIterator_swigregister
SwigPyIterator_swigregister(SwigPyIterator)

import cisstCommonPython
import cisstVectorPython
class nmrSVDDynamicData(object):
    """Proxy of C++ nmrSVDDynamicData class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def WorkspaceSize(m, n):
        """WorkspaceSize(nmrSVDDynamicData::size_type m, nmrSVDDynamicData::size_type n) -> nmrSVDDynamicData::size_type"""
        return _cisstNumericalPython.nmrSVDDynamicData_WorkspaceSize(m, n)

    WorkspaceSize = staticmethod(WorkspaceSize)

    def Allocate(self, m, n, storageOrder):
        """Allocate(nmrSVDDynamicData self, nmrSVDDynamicData::size_type m, nmrSVDDynamicData::size_type n, bool storageOrder)"""
        return _cisstNumericalPython.nmrSVDDynamicData_Allocate(self, m, n, storageOrder)


    def S(self):
        """S(nmrSVDDynamicData self) -> vctDynamicVectorRef< CISSTNETLIB_DOUBLE > const &"""
        return _cisstNumericalPython.nmrSVDDynamicData_S(self)


    def U(self):
        """U(nmrSVDDynamicData self) -> vctDynamicMatrixRef< CISSTNETLIB_DOUBLE > const &"""
        return _cisstNumericalPython.nmrSVDDynamicData_U(self)


    def Vt(self):
        """Vt(nmrSVDDynamicData self) -> vctDynamicMatrixRef< CISSTNETLIB_DOUBLE > const &"""
        return _cisstNumericalPython.nmrSVDDynamicData_Vt(self)


    def __init__(self, *args):
        """
        __init__(nmrSVDDynamicData self) -> nmrSVDDynamicData
        __init__(nmrSVDDynamicData self, nmrSVDDynamicData::size_type m, nmrSVDDynamicData::size_type n, bool storageOrder) -> nmrSVDDynamicData
        __init__(nmrSVDDynamicData self, vctDynamicMatrixBase< vctDynamicMatrixOwner< double >,CISSTNETLIB_DOUBLE > const & A) -> nmrSVDDynamicData
        __init__(nmrSVDDynamicData self, vctDynamicMatrixBase< vctDynamicMatrixRefOwner< double >,CISSTNETLIB_DOUBLE > const & A) -> nmrSVDDynamicData
        """
        this = _cisstNumericalPython.new_nmrSVDDynamicData(*args)
        try:
            self.this.append(this)
        except Exception:
            self.this = this
    __swig_destroy__ = _cisstNumericalPython.delete_nmrSVDDynamicData
    __del__ = lambda self: None
nmrSVDDynamicData_swigregister = _cisstNumericalPython.nmrSVDDynamicData_swigregister
nmrSVDDynamicData_swigregister(nmrSVDDynamicData)

def nmrSVDDynamicData_WorkspaceSize(m, n):
    """nmrSVDDynamicData_WorkspaceSize(nmrSVDDynamicData::size_type m, nmrSVDDynamicData::size_type n) -> nmrSVDDynamicData::size_type"""
    return _cisstNumericalPython.nmrSVDDynamicData_WorkspaceSize(m, n)


def nmrSVD(*args):
    """
    nmrSVD(vctDynamicMatrixBase< vctDynamicMatrixOwner< double >,CISSTNETLIB_DOUBLE > & A, nmrSVDDynamicData data) -> CISSTNETLIB_INTEGER
    nmrSVD(vctDynamicMatrixBase< vctDynamicMatrixRefOwner< double >,CISSTNETLIB_DOUBLE > & A, nmrSVDDynamicData data) -> CISSTNETLIB_INTEGER
    """
    return _cisstNumericalPython.nmrSVD(*args)
class nmrPInverseDynamicData(object):
    """Proxy of C++ nmrPInverseDynamicData class."""

    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def WorkspaceSize(m, n):
        """WorkspaceSize(nmrPInverseDynamicData::size_type m, nmrPInverseDynamicData::size_type n) -> nmrPInverseDynamicData::size_type"""
        return _cisstNumericalPython.nmrPInverseDynamicData_WorkspaceSize(m, n)

    WorkspaceSize = staticmethod(WorkspaceSize)

    def __init__(self):
        """__init__(nmrPInverseDynamicData self) -> nmrPInverseDynamicData"""
        this = _cisstNumericalPython.new_nmrPInverseDynamicData()
        try:
            self.this.append(this)
        except Exception:
            self.this = this

    def S(self):
        """S(nmrPInverseDynamicData self) -> vctDynamicVectorRef< CISSTNETLIB_DOUBLE > const &"""
        return _cisstNumericalPython.nmrPInverseDynamicData_S(self)


    def U(self):
        """U(nmrPInverseDynamicData self) -> vctDynamicMatrixRef< CISSTNETLIB_DOUBLE > const &"""
        return _cisstNumericalPython.nmrPInverseDynamicData_U(self)


    def Vt(self):
        """Vt(nmrPInverseDynamicData self) -> vctDynamicMatrixRef< CISSTNETLIB_DOUBLE > const &"""
        return _cisstNumericalPython.nmrPInverseDynamicData_Vt(self)


    def PInverse(self):
        """PInverse(nmrPInverseDynamicData self) -> vctDynamicMatrixRef< CISSTNETLIB_DOUBLE > const &"""
        return _cisstNumericalPython.nmrPInverseDynamicData_PInverse(self)

    __swig_destroy__ = _cisstNumericalPython.delete_nmrPInverseDynamicData
    __del__ = lambda self: None
nmrPInverseDynamicData_swigregister = _cisstNumericalPython.nmrPInverseDynamicData_swigregister
nmrPInverseDynamicData_swigregister(nmrPInverseDynamicData)

def nmrPInverseDynamicData_WorkspaceSize(m, n):
    """nmrPInverseDynamicData_WorkspaceSize(nmrPInverseDynamicData::size_type m, nmrPInverseDynamicData::size_type n) -> nmrPInverseDynamicData::size_type"""
    return _cisstNumericalPython.nmrPInverseDynamicData_WorkspaceSize(m, n)


def nmrPInverse(A, PInverse):
    """nmrPInverse(vctDynamicMatrixBase< vctDynamicMatrixOwner< double >,CISSTNETLIB_DOUBLE > & A, vctDynamicMatrixBase< vctDynamicMatrixOwner< double >,CISSTNETLIB_DOUBLE > & PInverse) -> CISSTNETLIB_INTEGER"""
    return _cisstNumericalPython.nmrPInverse(A, PInverse)

def nmrRegistrationRigid(dataSet1, dataSet2):
    """nmrRegistrationRigid(vctDynamicMatrix< double > const & dataSet1, vctDynamicMatrix< double > const & dataSet2) -> std::pair< vctFrm3,double >"""
    return _cisstNumericalPython.nmrRegistrationRigid(dataSet1, dataSet2)



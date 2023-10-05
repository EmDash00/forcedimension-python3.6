import ctypes as ct
from ctypes import POINTER, c_double, c_int, c_ubyte, c_uint, c_ushort
from typing import (
    TYPE_CHECKING, Any, Container, Generic, List, Sized, Tuple,
    TypeVar, Union, MutableSequence
)
from typing_extensions import Literal, Protocol

_KT_contra = TypeVar("_KT_contra", contravariant=True)
_VT = TypeVar("_VT")
_VT_co = TypeVar("_VT_co", covariant=True)

MutableFloatReturnArray = List[float]
MutableFloatReturnArray2D = List[List[float]]
MutableIntReturnArray = List[int]

ComModeStr = Literal['sync', 'async', 'virtual', 'network']

class _Array(Sized, Protocol[_KT_contra, _VT_co]):
    def __getitem__(self, __k: _KT_contra) -> _VT_co: ...

class _MutableArray(
    _Array[_KT_contra, _VT], Protocol[_KT_contra, _VT]
):
    def __setitem__(self, __k: _KT_contra, __v: _VT) -> None: ...

c_double_ptr = POINTER(c_double)
c_ubyte_ptr = POINTER(c_ubyte)
c_ushort_ptr = POINTER(c_ushort)
c_int_ptr = POINTER(c_int)
c_uint_ptr = POINTER(c_uint)


class SupportsPtr(Protocol):
    @property
    def ptr(self) -> Any:
        ...


class SupportsPtrs3(Protocol):
    @property
    def ptrs(self) -> Any:
        ...

#: Represents the type of a homogenous array of floats
#: specifically, it implements ``__getitem__`` and ``__len__``
FloatArray = _Array[int, float]

#: Represents the type of a homogenous array of ints
#: specifically, it implements ``__getitem__`` and ``__len__``
IntArray = _Array[int, int]

#: Represents the type of a mutable homogenous array of floats
#: specifically, it implements ``__setitem__``, ``__getitem__``, and
#: ``__len__``
MutableFloatArray = _MutableArray[int, float]

#: Represents the type of a mutable homogenous array of ints
#: specifically, it implements ``__setitem__``, ``__getitem__``, and
#: ``__len__``
MutableIntArray = _MutableArray[int, int]

#: Represents the type of a homogenous array of floats.
#: Used specifically to simplify the typing of various returns since
#: Functions that take in FloatArray are assumed to return the same kind
#: of float array.
FloatVectorLike = FloatArray

#: Represents the type of a mutable homogenous array of floats.
#: Used specifically to simplify the typing of various returns since
#: Functions that take in FloatArray are assumed to return the same kind
#: of float array.
MutableFloatVectorLike = Union[MutableFloatArray, MutableFloatReturnArray]

#: Represents the type of a homogenous array of ints.
#: Used specifically to simplify the typing of various returns since
#: functions that take in FloatArray are assumed to return the same kind
#: of float array.
IntVectorLike = IntArray


#: Represents the type of a mutable homogenous array of ints.
#: Used specifically to simplify the typing of various returns since
#: functions that take in FloatArray are assumed to return the same kind
#: of float array.

MutableIntVectorLike = Union[MutableIntArray, MutableIntReturnArray]


#: Represents a 2D array of floats
MutableFloatArray2D = _MutableArray[int, MutableFloatVectorLike]

#: Represents the type of a homogenous 2D array of floats.
#: Used specifically to simplify the typing of various returns since
#: functions that take in MutableFloatArray2D are assumed to return the same
#: of 2D float array.
MutableFloatMatrixLike = Union[MutableFloatArray2D, MutableFloatReturnArray2D]

IntDOFTuple = Tuple[int, int, int, int, int, int, int, int]
FloatDOFTuple = Tuple[float, float, float, float, float, float, float, float]

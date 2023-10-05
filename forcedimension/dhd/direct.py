from ctypes import c_byte, c_double, c_int

import forcedimension.runtime as _runtime
from forcedimension.typing import (
    SupportsPtr, SupportsPtrs3, c_double_ptr
)

_libdhd = _runtime.load("libdrd")

if _libdhd is None:
    raise ImportError("There were problems loading libdhd.")


_libdhd.dhdGetPosition.argtypes = [
    c_double_ptr,
    c_double_ptr,
    c_double_ptr,
    c_byte
]
_libdhd.dhdGetPosition.restype = c_int


def getPosition(out: SupportsPtrs3, ID: int = -1) -> int:
    """
    Retrieve the position of the end-effector about the X, Y, and Z axes.
    Please refer to your device user manual for more information on your device
    coordinate system.

    :param SupportsPtrs3 out:
        An output buffer to store the position of the end-effector (in [m]).

    :param int ID:
         Device ID (see multiple devices section for details).

    :raises AttributeError:
        If ``out.ptrs`` is not a valid attribute of ``out``

    :raises TypeError:
        If ``out.ptrs`` is not iterable.

    :raises ArgumentError:
        If ``out.ptrs`` does not expand into a tuple of 3
        ``Pointer`` types.

    :raises ArgumentError:
        If ``ID`` is not implicitly convertible to C char.

    :returns:
        0 or :data:`forcedimension.dhd.TIMEGUARD` on success,
        -1 otherwise.
    """

    return _libdhd.dhdGetPosition(*out.ptrs, ID)


_libdhd.dhdGetForce.argtypes = [
    c_double_ptr,
    c_double_ptr,
    c_double_ptr,
    c_byte
]
_libdhd.dhdGetForce.restype = c_int


def getForce(out: SupportsPtrs3, ID: int = -1) -> int:
    """
    Retrieve the force vector applied to the end-effector (in [N])
    about the X, Y, and Z axes Please refer to your device user manual for more
    information on your device coordinate system.

    :param SupportsPtrs3 out:
        An output buffer to store the applied forces on the end-effector
        (in [N]).

    :param int ID:
         Device ID (see multiple devices section for details).

    :raises AttributeError:
        If ``out.ptrs`` is not a valid attribute of ``out``

    :raises TypeError:
        If ``out`` does not support item assignment either
        because its immutable or not subscriptable.

    :raises TypeError:
        If ``out.ptrs`` is not iterable.

    :raises ArgumentError:
        If ``out.ptrs`` does not expand into a tuple of 3
        ``Pointer`` types.

    :raises ArgumentError:
        If ``ID`` is not implicitly convertible to C char.

    :returns:
        0 on success, -1 otherwise.
    """

    return _libdhd.dhdGetForce(*out.ptrs, ID)


_libdhd.dhdGetOrientationRad.argtypes = [
    c_double_ptr,
    c_double_ptr,
    c_double_ptr,
    c_byte
]
_libdhd.dhdGetOrientationRad.restype = c_int


def getOrientationRad(
    out: SupportsPtrs3, ID: int = -1
) -> int:
    """
    For devices with a wrist structure, retrieve individual angle (in [rad])
    of each joint, starting with the one located nearest to the wrist base
    plate.

    This feature only applies to the following devices
        :data:`forcedimension.dhd.constants.DeviceType.OMEGA6_RIGHT`
        :data:`forcedimension.dhd.constants.DeviceType.OMEGA6_LEFT`
        :data:`forcedimension.dhd.constants.DeviceType.OMEGA7_RIGHT`
        :data:`forcedimension.dhd.constants.DeviceType.OMEGA7_LEFT`
        :data:`forcedimension.dhd.constants.DeviceType.SIGMA7_RIGHT`
        :data:`forcedimension.dhd.constants.DeviceType.SIGMA7_LEFT`
        :data:`forcedimension.dhd.constants.DeviceType.LAMBDA7_RIGHT`
        :data:`forcedimension.dhd.constants.DeviceType.LAMBDA7_LEFT`


    Info
    ----
    :data:`forcedimension.dhd.constants.DeviceType.OMEGA6_RIGHT` and
    :data:`forcedimension.dhd.constants.DeviceType.OMEGA6_LEFT`
    have angles that are instead computed with respect to their internal
    reference frame, which is rotated π/4 radians around the Y axis.
    Please refer to your device user manual for more information on your
    device coordinate system.


    :param SupportsPtrs3 out:
        An output buffer to store the joint angles (in [rad]).

    :param int ID:
         Device ID (see multiple devices section for details).

    :raises AttributeError:
        If ``out.ptrs`` is not a valid attribute of ``out``

    :raises TypeError:
        If ``out`` does not support item assignment either
        because its immutable or not subscriptable.

    :raises TypeError:
        If ``out.ptrs`` is not iterable.

    :raises ArgumentError:
        If ``out.ptrs`` does not expand into a tuple of 3
        ``Pointer`` types.

    :raises ArgumentError:
        If ``ID`` is not implicitly convertible to C char.

    :returns:
        0 or :data:`forcedimension.dhd.constants.TIMEGUARD` on success,
        -1 otherwise.
    """

    return _libdhd.dhdGetOrientationRad(*out.ptrs, ID)


_libdhd.dhdGetOrientationDeg.argtypes = [
    c_double_ptr,
    c_double_ptr,
    c_double_ptr,
    c_byte
]
_libdhd.dhdGetOrientationDeg.restype = c_int


def getOrientationDeg(
    out: SupportsPtrs3, ID: int = -1
) -> int:
    """
    For devices with a wrist structure, retrieve individual angle (in [deg])
    of each joint, starting with the one located nearest to the wrist base
    plate.

    This feature only applies to the following devices
        :data:`forcedimension.dhd.constants.DeviceType.OMEGA6_RIGHT`
        :data:`forcedimension.dhd.constants.DeviceType.OMEGA6_LEFT`
        :data:`forcedimension.dhd.constants.DeviceType.OMEGA7_RIGHT`
        :data:`forcedimension.dhd.constants.DeviceType.OMEGA7_LEFT`
        :data:`forcedimension.dhd.constants.DeviceType.SIGMA7_RIGHT`
        :data:`forcedimension.dhd.constants.DeviceType.SIGMA7_LEFT`
        :data:`forcedimension.dhd.constants.DeviceType.LAMBDA7_RIGHT`
        :data:`forcedimension.dhd.constants.DeviceType.LAMBDA7_LEFT`


    Info
    ----
    :data:`forcedimension.dhd.constants.DeviceType.OMEGA6_RIGHT` and
    :data:`forcedimension.dhd.constants.DeviceType.OMEGA6_LEFT`
    have angles that are instead computed with respect to their internal
    reference frame, which is rotated π/4 radians around the Y axis.
    Please refer to your device user manual for more information on your
    device coordinate system.


    :param SupportsPtrs3 out:
        An output buffer to store the joint angles (in [deg]).

    :param int ID:
         Device ID (see multiple devices section for details).

    :raises AttributeError:
        If ``out.ptrs`` is not a valid attribute of ``out``

    :raises TypeError:
        If ``out`` does not support item assignment either
        because its immutable or not subscriptable.

    :raises TypeError:
        If ``out.ptrs`` is not iterable.

    :raises ArgumentError:
        If ``out.ptrs`` does not expand into a tuple of 3
        ``Pointer`` types.

    :raises ArgumentError:
        If ``ID`` is not implicitly convertible to C char.

    :returns:
        0 or :data:`forcedimension.dhd.constants.TIMEGUARD` on success,
        -1 otherwise.
    """

    return _libdhd.dhdGetOrientationDeg(*out.ptrs, ID)


_libdhd.dhdGetPositionAndOrientationRad.argtypes = [
    c_double_ptr,
    c_double_ptr,
    c_double_ptr,
    c_double_ptr,
    c_double_ptr,
    c_double_ptr,
    c_byte
]
_libdhd.dhdGetPositionAndOrientationRad.restype = c_int


def getPositionAndOrientationRad(
    p_out: SupportsPtrs3,
    o_out: SupportsPtrs3,
    ID: int = -1
) -> int:
    """
    Retrieve the position (in [m]) and
    for devices with a wrist structure, retrieve individual angle
    of each joint (in [rad]), starting with the one located nearest to the wrist
    base plate.

    Note:

    :data:`forcedimension.dhd.constants.DeviceType.OMEGA6_RIGHT`
    :data:`forcedimension.dhd.constants.DeviceType.OMEGA6_LEFT`

    have angles that are instead computed with respect to their internal
    reference frame, which is rotated π/4 radians around the Y axis.
    Please refer to your device user manual for more information on your
    device coordinate system.

    This feature only applies to the following devices
        :data:`forcedimension.dhd.constants.DeviceType.OMEGA6_RIGHT`
        :data:`forcedimension.dhd.constants.DeviceType.OMEGA6_LEFT`
        :data:`forcedimension.dhd.constants.DeviceType.OMEGA7_RIGHT`
        :data:`forcedimension.dhd.constants.DeviceType.OMEGA7_LEFT`
        :data:`forcedimension.dhd.constants.DeviceType.SIGMA7_RIGHT`
        :data:`forcedimension.dhd.constants.DeviceType.SIGMA7_LEFT`
        :data:`forcedimension.dhd.constants.DeviceType.LAMBDA7_RIGHT`
        :data:`forcedimension.dhd.constants.DeviceType.LAMBDA7_LEFT`


    :param int ID:
         Device ID (see multiple devices section for details).

    :param SupportsPtrs3 p_out:
        An output buffer to store the position (in [m]).

    :param SupportsPtrs3 o_out:
        An output buffer to store the joint angles (in [rad]).

    :raises AttributeError:
        If ``p_out.ptrs`` is not a valid attribute of ``out``

    :raises TypeError:
        If ``p_out.ptrs`` is not iterable.

    :raises ArgumentError:
        If ``p_out.ptrs`` does not expand into a tuple of 3
        ``Pointer`` types.

    :raises AttributeError:
        If ``o_out.ptrs`` is not a valid attribute of ``out``

    :raises TypeError:
        If ``o_out`` does not support item assignment either
        because its immutable or not subscriptable.

    :raises TypeError:
        If ``o_out.ptrs`` is not iterable.

    :raises ArgumentError:
        If ``o_out.ptrs`` does not expand into a tuple of 3
        ``Pointer`` types.

    :raises ArgumentError:
        If ``ID`` is not implicitly convertible to C char.

    :returns:
        0 or :data:`forcedimension.dhd.constants.TIMEGUARD` on success,
        -1 otherwise.
    """

    return _libdhd.dhdGetPositionAndOrientationRad(
        *p_out.ptrs, *o_out.ptrs, ID
    )


_libdhd.dhdGetPositionAndOrientationDeg.argtypes = [
    c_double_ptr,
    c_double_ptr,
    c_double_ptr,
    c_double_ptr,
    c_double_ptr,
    c_double_ptr,
    c_byte
]
_libdhd.dhdGetPositionAndOrientationDeg.restype = c_int


def getPositionAndOrientationDeg(
    p_out: SupportsPtrs3,
    o_out: SupportsPtrs3,
    ID: int = -1
) -> int:
    """
    Retrieve the position (in [m]) and
    for devices with a wrist structure, retrieve individual angle
    of each joint (in [deg]), starting with the one located nearest to the wrist
    base plate.

    Note:

    :data:`forcedimension.dhd.constants.DeviceType.OMEGA6_RIGHT`
    :data:`forcedimension.dhd.constants.DeviceType.OMEGA6_LEFT`

    have angles that are instead computed with respect to their internal
    reference frame, which is rotated π/4 radians around the Y axis.
    Please refer to your device user manual for more information on your
    device coordinate system.

    This feature only applies to the following devices
        :data:`forcedimension.dhd.constants.DeviceType.OMEGA6_RIGHT`
        :data:`forcedimension.dhd.constants.DeviceType.OMEGA6_LEFT`
        :data:`forcedimension.dhd.constants.DeviceType.OMEGA7_RIGHT`
        :data:`forcedimension.dhd.constants.DeviceType.OMEGA7_LEFT`
        :data:`forcedimension.dhd.constants.DeviceType.SIGMA7_RIGHT`
        :data:`forcedimension.dhd.constants.DeviceType.SIGMA7_LEFT`
        :data:`forcedimension.dhd.constants.DeviceType.LAMBDA7_RIGHT`
        :data:`forcedimension.dhd.constants.DeviceType.LAMBDA7_LEFT`


    :param int ID:
         Device ID (see multiple devices section for details).

    :param SupportsPtrs3 p_out:
        An output buffer to store the position (in [m]).

    :param SupportsPtrs3 o_out:
        An output buffer to store the joint angles (in [rad]).

    :raises AttributeError:
        If ``p_out.ptrs`` is not a valid attribute of ``out``

    :raises TypeError:
        If ``p_out.ptrs`` is not iterable.

    :raises ArgumentError:
        If ``p_out.ptrs`` does not expand into a tuple of 3
        ``Pointer`` types.

    :raises AttributeError:
        If ``o_out.ptrs`` is not a valid attribute of ``out``

    :raises TypeError:
        If ``o_out`` does not support item assignment either
        because its immutable or not subscriptable.

    :raises TypeError:
        If ``o_out.ptrs`` is not iterable.

    :raises ArgumentError:
        If ``o_out.ptrs`` does not expand into a tuple of 3
        ``Pointer`` types.

    :raises ArgumentError:
        If ``ID`` is not implicitly convertible to C char.

    :returns:
        0 or :data:`forcedimension.dhd.constants.TIMEGUARD` on success,
        -1 otherwise.
    """

    return _libdhd.dhdGetPositionAndOrientationDeg(
        *p_out.ptrs, *o_out.ptrs, ID
    )


_libdhd.dhdGetPositionAndOrientationFrame.argtypes = [
    c_double_ptr,
    c_double_ptr,
    c_double_ptr,
    c_double_ptr,
    c_byte
]
_libdhd.dhdGetPositionAndOrientationFrame.restype = c_int


def getPositionAndOrientationFrame(
    p_out: SupportsPtrs3,
    matrix_out: SupportsPtr,
    ID: int = -1
) -> int:
    """
    Retrieve the position (in [m]) and orientation matrix of the end-effector
    about the X, Y, and Z axes. Please refer to your device user manual for
    more information on your device coordinate system.

    :param int ID:
         Device ID (see multiple devices section for details).

    :raises AttributeError:
        If ``p_out.ptrs`` is not a valid attribute of ``p_out``

    :raises TypeError:
        If ``p_out.ptrs`` is not iterable.

    :raises ArgumentError:
        If ``p_out.ptrs`` does not expand into a tuple of 3
        ``Pointer`` types.

    :raises AttributeError:
        If ``matrix_out.ptr`` is not a valid attribute of ``matrix_out``

    :raises ArgumentError:
        If ``p_out.ptr`` is not a ``Pointer`` type.

    :raises ArgumentError:
        If ``ID`` is not implicitly convertible to C char.

    :returns:
        0 or :data:`forcedimension.dhd.constants.TIMEGUARD` on success,
        -1 otherwise.
    """

    return _libdhd.dhdGetPositionAndOrientationFrame(
        *p_out.ptrs, matrix_out.ptr, ID
    )


_libdhd.dhdGetForceAndTorque.argtypes = [
    c_double_ptr,
    c_double_ptr,
    c_double_ptr,
    c_double_ptr,
    c_double_ptr,
    c_double_ptr,
    c_byte
]
_libdhd.dhdGetForceAndTorque.restype = c_int


def getForceAndTorque(
    f_out: SupportsPtrs3,
    t_out: SupportsPtrs3,
    ID: int = -1
) -> int:
    """
    Retrieve the forces (in [N]) and torques (in [Nm]) applied to the device
    end-effector about the X, Y, and Z axes. Please refer to your device user
    manual for more information on your device coordinate system.

    :param int ID:
         Device ID (see multiple devices section for details).

    :param SupportsPtrs3 f_out:
        An output buffer to store the applied forces on the end-effector
        (in [N]).

    :param SupportsPtrs3 t_out:
        An output buffer to store the applied torques on the end-effector
        (in [N]).

    :raises AttributeError:
        If ``f_out.ptrs`` is not a valid attribute of ``f_out``

    :raises TypeError:
        If ``f_out.ptrs`` is not iterable.

    :raises ArgumentError:
        If ``f_out.ptrs`` does not expand into a tuple of 3
        ``Pointer`` types.

    :raises AttributeError:
        If ``t_out.ptrs`` is not a valid attribute of ``t_out``

    :raises TypeError:
        If ``t_out.ptrs`` is not iterable.

    :raises ArgumentError:
        If ``t_out.ptrs`` does not expand into a tuple of 3
        ``Pointer`` types.

    :raises ArgumentError:
        If ``ID`` is not implicitly convertible to C char.

    :returns:
        0, on success, -1 otherwise.
    """

    return _libdhd.dhdGetForceAndTorque(*f_out.ptrs, *t_out.ptrs, ID)


_libdhd.dhdGetOrientationFrame.argtypes = [
    c_double_ptr,
    c_byte
]
_libdhd.dhdGetOrientationFrame.restype = c_int


def getOrientationFrame(out: SupportsPtr, ID: int = -1) -> int:
    """
    Retrieve the rotation matrix of the wrist structure. The identity matrix
    is returned for devices that do not support orientations.

    :param int ID:
         Device ID (see multiple devices section for details).

    :param SupportsPtr out:
        An output buffer to store the orientation frame.

    :raises ArgumentError:
        If ``ID`` is not implicitly convertible to C char.

    :raises AttributeError:
        If ``out.ptr`` is not a valid attribute of ``p_out``

    :raises ArgumentError:
        If ``out.ptr`` is not a ``Pointer`` type.

    :returns:
        0 or :data:`forcedimension.dhd.constants.TIMEGUARD` on success,
        -1 otherwise.
    """

    return _libdhd.dhdGetOrientationFrame(out.ptr, ID)


_libdhd.dhdGetGripperAngleDeg.argtypes = [c_double_ptr, c_byte]
_libdhd.dhdGetGripperAngleDeg.restype = c_int


def getGripperAngleDeg(out: c_double, ID: int = -1) -> int:
    """
    Get the gripper opening angle (in [deg]).

    This feature only applies to the following devices
        :data:`forcedimension.dhd.constants.DeviceType.OMEGA7_RIGHT`
        :data:`forcedimension.dhd.constants.DeviceType.OMEGA7_LEFT`
        :data:`forcedimension.dhd.constants.DeviceType.SIGMA7_RIGHT`
        :data:`forcedimension.dhd.constants.DeviceType.SIGMA7_LEFT`
        :data:`forcedimension.dhd.constants.DeviceType.LAMBDA7_RIGHT`
        :data:`forcedimension.dhd.constants.DeviceType.LAMBDA7_LEFT`

    See Also
    --------
    :func:`forcedimension.dhd.direct.getGripperAngleRad()`


    :param c_double out:
        Buffer to store the gripper opening angle (in [deg]).

    :param int ID:
         Device ID (see multiple devices section for details).

    :raises ArgumentError:
        If ``ID`` is not implicitly convertible to C char.

    :returns:
        0 or :data:`forcedimension.dhd.constants.TIMEGUARD` on success,
        -1 otherwise.
    """

    return _libdhd.dhdGetGripperAngleDeg(out, ID)


_libdhd.dhdGetGripperAngleRad.argtypes = [c_double_ptr, c_byte]
_libdhd.dhdGetGripperAngleRad.restype = c_int


def getGripperAngleRad(out: c_double, ID: int = -1) -> int:
    """
    Get the gripper opening angle (in [rad]).

    This feature only applies to the following devices
        :data:`forcedimension.dhd.constants.DeviceType.OMEGA7_RIGHT`
        :data:`forcedimension.dhd.constants.DeviceType.OMEGA7_LEFT`
        :data:`forcedimension.dhd.constants.DeviceType.SIGMA7_RIGHT`
        :data:`forcedimension.dhd.constants.DeviceType.SIGMA7_LEFT`
        :data:`forcedimension.dhd.constants.DeviceType.LAMBDA7_RIGHT`
        :data:`forcedimension.dhd.constants.DeviceType.LAMBDA7_LEFT`

    See Also
    --------
    :func:`forcedimension.dhd.direct.getGripperAngleDeg()`


    :param c_double out:
        Buffer to store the gripper opening angle (in [rad]).

    :param int ID:
         Device ID (see multiple devices section for details).

    :raises ArgumentError:
        If ``ID`` is not implicitly convertible to C char.

    :returns:
        0 or :data:`forcedimension.dhd.constants.TIMEGUARD` on success,
        -1 otherwise.
    """

    return _libdhd.dhdGetGripperAngleRad(out, ID)


_libdhd.dhdGetGripperGap.argtypes = [c_double_ptr, c_byte]
_libdhd.dhdGetGripperGap.restype = c_int


def getGripperGap(out: c_double, ID: int = -1) -> int:
    """
    Get the gripper opening distance (in [m]).

    This feature only applies to the following devices
        :data:`forcedimension.dhd.constants.DeviceType.OMEGA7_RIGHT`
        :data:`forcedimension.dhd.constants.DeviceType.OMEGA7_LEFT`
        :data:`forcedimension.dhd.constants.DeviceType.SIGMA7_RIGHT`
        :data:`forcedimension.dhd.constants.DeviceType.SIGMA7_LEFT`
        :data:`forcedimension.dhd.constants.DeviceType.LAMBDA7_RIGHT`
        :data:`forcedimension.dhd.constants.DeviceType.LAMBDA7_LEFT`

    :param c_double out:
        buffer to store the gripper opening distance (in [m]).

    :param int ID:
         Device ID (see multiple devices section for details).

    :raises ArgumentError:
        If ``ID`` is not implicitly convertible to C char.

    :returns:
        0 or :data:`forcedimension.dhd.constants.TIMEGUARD` on success,
        -1 otherwise.
    """

    return _libdhd.dhdGetGripperGap(out, ID)


_libdhd.dhdGetGripperThumbPos.argtypes = [
    c_double_ptr,
    c_double_ptr,
    c_double_ptr,
    c_byte
]
_libdhd.dhdGetGripperThumbPos.restype = c_int


def getGripperThumbPos(
    out: SupportsPtrs3, ID: int = -1
) -> int:
    """
    Read the position (in [m]) of thumb rest location about the x, y and z axes
    of the force gripper structure if present.

    This feature only applies to the following devices
        :data:`forcedimension.dhd.constants.DeviceType.OMEGA7_RIGHT`
        :data:`forcedimension.dhd.constants.DeviceType.OMEGA7_LEFT`
        :data:`forcedimension.dhd.constants.DeviceType.SIGMA7_RIGHT`
        :data:`forcedimension.dhd.constants.DeviceType.SIGMA7_LEFT`
        :data:`forcedimension.dhd.constants.DeviceType.LAMBDA7_RIGHT`
        :data:`forcedimension.dhd.constants.DeviceType.LAMBDA7_LEFT`

    :param int ID:
         Device ID (see multiple devices section for details).

    :param SupportsPtrs3 out:
        An output buffer to store the grippper thumb position (in [m]).

    :raises AttributeError:
        If ``out.ptrs`` is not a valid attribute of ``out``

    :raises TypeError:
        If ``out.ptrs`` is not iterable.

    :raises ArgumentError:
        If ``out.ptrs`` does not expand into a tuple of 3
        ``Pointer`` types.

    :raises ArgumentError:
        If ``ID`` is not implicitly convertible to C char.

    :returns:
        0 or :data:`forcedimension.dhd.constants.TIMEGUARD` on success,
        -1 otherwise.

    """

    return _libdhd.dhdGetGripperFingerPos(*out.ptrs, ID)


_libdhd.dhdGetGripperFingerPos.argtypes = [
    c_double_ptr,
    c_double_ptr,
    c_double_ptr,
    c_byte
]
_libdhd.dhdGetGripperFingerPos.restype = c_int


def getGripperFingerPos(
    out: SupportsPtrs3, ID: int = -1
) -> int:
    """
    Read the position (in [m]) of forefinger rest location about the x, y, and
    z axes of the force gripper structure if present.

    This feature only applies to the following devices
        :data:`forcedimension.dhd.constants.DeviceType.OMEGA7_RIGHT`
        :data:`forcedimension.dhd.constants.DeviceType.OMEGA7_LEFT`
        :data:`forcedimension.dhd.constants.DeviceType.SIGMA7_RIGHT`
        :data:`forcedimension.dhd.constants.DeviceType.SIGMA7_LEFT`
        :data:`forcedimension.dhd.constants.DeviceType.LAMBDA7_RIGHT`
        :data:`forcedimension.dhd.constants.DeviceType.LAMBDA7_LEFT`

    :param int ID:
         Device ID (see multiple devices section for details).

    :param SupportsPtrs3 out:
        An output buffer to store the gripper finger position (in [m]).

    :raises AttributeError:
        If ``out.ptrs`` is not a valid attribute of ``out``

    :raises TypeError:
        If ``out.ptrs`` is not iterable.

    :raises ArgumentError:
        If ``out.ptrs`` does not expand into a tuple of 3
        ``Pointer`` types.

    :raises ArgumentError:
        If ``ID`` is not implicitly convertible to C char.

    :returns:
        0 or :data:`forcedimension.dhd.constants.TIMEGUARD` on success,
        -1 otherwise.

    """

    return _libdhd.dhdGetGripperFingerPos(*out.ptrs, ID)


_libdhd.dhdGetForceAndTorqueAndGripperForce.argtypes = [
    c_double_ptr,
    c_double_ptr,
    c_double_ptr,
    c_double_ptr,
    c_double_ptr,
    c_double_ptr,
    c_double_ptr,
    c_byte
]
_libdhd.dhdGetForceAndTorqueAndGripperForce.restype = c_int


def getForceAndTorqueAndGripperForce(
    f_out: SupportsPtrs3,
    t_out: SupportsPtrs3,
    fg_out: c_double,
    ID: int = -1
) -> int:
    """
    Retrieve the forces (in [N]) and torques (in [Nm]) applied to the device
    end-effector as well as the gripper force (in [N]).
    Forces and torques are about the X, Y, and Z axes.

    :param int ID:
         Device ID (see multiple devices section for details).

    :param SupportsPtrs3 f_out:
        An output buffer to store the applied forces on the end-effector
        (in [N]).

    :param SupportsPtrs3 t_out:
        An output buffer to store the applied torques on the end-effector
        (in [Nm]).

    :raises AttributeError:
        If ``f_out.ptrs`` is not a valid attribute of ``f_out``

    :raises TypeError:
        If ``f_out.ptrs`` is not iterable.

    :raises ArgumentError:
        If ``f_out.ptrs`` does not expand into a tuple of 3
        ``Pointer`` types.

    :raises AttributeError:
        If ``t_out.ptrs`` is not a valid attribute of ``t_out``

    :raises TypeError:
        If ``t_out.ptrs`` is not iterable.

    :raises ArgumentError:
        If ``t_out.ptrs`` does not expand into a tuple of 3
        ``Pointer`` types.

    :raises AttributeError:
        If ``fg_out.ptr`` is not a valid attribute of ``fg_out``

    :raises ArgumentError:
        If ``fg_out.ptr`` is not a ``Pointer``.

    :raises ArgumentError:
        If ``ID`` is not implicitly convertible to C char.

    :returns:
       0, on success, -1 otherwise.
    """

    err = _libdhd.dhdGetForceAndTorqueAndGripperForce(
        *f_out.ptrs, *t_out.ptrs, fg_out, ID
    )
    return err


_libdhd.dhdGetLinearVelocity.argtypes = [
    c_double_ptr,
    c_double_ptr,
    c_double_ptr,
    c_byte
]
_libdhd.dhdGetLinearVelocity.restype = c_int


def getLinearVelocity(out: SupportsPtrs3, ID: int = -1) -> int:
    """
    Retrieve the estimated instanteous linear velocity (in [m/s]).

    By default :data:`forcedimension.dhd.constants.VELOCITY_WINDOW` and
    :data:`forcedimension.dhd.constants.VELOCITY_WINDOWING`
    are used. See velocity estimator for details.

    Info
    ----
    The velocity estimator requires at least 2 position
    updates during the time interval defined in
    :func:`forcedimension.dhd.configLinearVelocity()` in order to be able to
    compute the estimate. Otherwise, e.g. if there are no calls to
    :func:`forcedimension.dhd.getPosition(), dhd.libdhd.getLinearVelocity()`,
    or :func:`forcedimension.dhd.getLinearVelocity()` will return an error
    (:data:`forcedimension.dhd.constants.ErrorNum.TIMEOUT`).


    See Also
    --------
    :func:`forcedimension.dhd.configLinearVelocity()`


    :param int ID:
         Device ID (see multiple devices section for details).

    :param SupportsPtr out:
        An output buffer to store the linear velocity (in [m/s]).

    :raises AttributeError:
        If ``out.ptrs`` is not a valid attribute of ``out``

    :raises TypeError:
        If ``out.ptrs`` is not iterable.

    :raises ArgumentError:
        If ``out.ptrs`` does not expand into a tuple of 3
        ``Pointer`` types.


   :raises ArgumentError:
        If ``ID`` is not implicitly convertible to C char.

    :returns:
        0 on success, -1 otherwise.
    """

    return _libdhd.dhdGetLinearVelocity(*out.ptrs, ID)


_libdhd.dhdGetAngularVelocityRad.argtypes = [
    c_double_ptr,
    c_double_ptr,
    c_double_ptr,
    c_byte
]
_libdhd.dhdGetAngularVelocityRad.restype = c_int


def getAngularVelocityRad(
    out: SupportsPtrs3, ID: int = -1
) -> int:
    """
    Retrieve the estimated angular velocity (in [rad/s]).

    Info
    ----
    The velocity estimator requires at least 2 position
    updates during the time interval defined in
    :func:`forcedimension.dhd.configLinearVelocity()` in order to be able to
    compute the estimate. Otherwise, e.g. if there are no calls to
    :func:`forcedimension.dhd.getPosition(), dhd.libdhd.getLinearVelocity()`,
    or :func:`forcedimension.dhd.getLinearVelocity()` will return an error
    (:data:`forcedimension.dhd.constants.ErrorNum.TIMEOUT`).

    See Also
    --------
    :func:`forcedimension.dhd.configAngularVelocity()`
    :func:`forcedimension.dhd.getAngularVelocityDeg()`


    :param int ID:
         Device ID (see multiple devices section for details).

    :param out:
        An output buffer to store the angular velocity (in [rad/s]).

    :raises AttributeError:
        If ``out.ptrs`` is not a valid attribute of ``out``

   :raises TypeError:
        If ``out.ptrs`` is not iterable.

    :raises ArgumentError:
        If ``out.ptrs`` does not expand into a tuple of 3
        ``Pointer`` types.


    :raises ArgumentError:
        If ``ID`` is not implicitly convertible to C char.

    :returns:
        0 on success, -1 otherwise.
    """

    return _libdhd.dhdGetAngularVelocityRad(*out.ptrs, ID)


_libdhd.dhdGetAngularVelocityDeg.argtypes = [
    c_double_ptr,
    c_double_ptr,
    c_double_ptr,
    c_byte
]
_libdhd.dhdGetAngularVelocityDeg.restype = c_int


def getAngularVelocityDeg(
    out: SupportsPtrs3, ID: int = -1
) -> int:
    """
    Retrieve the estimated angular velocity (in [deg/s]).

    Info
    ----
    The velocity estimator requires at least 2 position
    updates during the time interval defined in
    :func:`forcedimension.dhd.configLinearVelocity()` in order to be able to
    compute the estimate. Otherwise, e.g. if there are no calls to
    :func:`forcedimension.dhd.getPosition(), dhd.libdhd.getLinearVelocity()`,
    or :func:`forcedimension.dhd.getLinearVelocity()` will return an error
    (:data:`forcedimension.dhd.constants.ErrorNum.TIMEOUT`).

    See Also
    --------
    :func:`forcedimension.dhd.configAngularVelocity()`
    :func:`forcedimension.dhd.getAngularVelocityDeg()`


    :param int ID:
         Device ID (see multiple devices section for details).

    :param out:
        An output buffer to store the angular velocity (in [deg/s]).

    :raises AttributeError:
        If ``out.ptrs`` is not a valid attribute of ``out``

   :raises TypeError:
        If ``out.ptrs`` is not iterable.

    :raises ArgumentError:
        If ``out.ptrs`` does not expand into a tuple of 3
        ``Pointer`` types.


    :raises ArgumentError:
        If ``ID`` is not implicitly convertible to C char.

    :returns:
        0 on success, -1 otherwise.
    """

    return _libdhd.dhdGetAngularVelocityDeg(*out.ptrs, ID)


_libdhd.dhdGetGripperLinearVelocity.argtypes = [c_double_ptr, c_byte]
_libdhd.dhdGetGripperLinearVelocity.restype = c_int


def getGripperLinearVelocity(out: c_double, ID: int = -1) -> int:
    """
    Retrieve the estimated linear velocity of the gripper (in [m/s]).

    Please note that the velocity estimator requires at least 2 position
    updates during the time interval defined in
    :func:`forcedimension.dhd.configLinearVelocity()` in order to be able to
    compute the estimate. Otherwise, e.g. if there are no calls to
    :func:`forcedimension.dhd.getPosition(), dhd.libdhd.getLinearVelocity()`,
    or :func:`forcedimension.dhd.getLinearVelocity()` will return an error
    (:data:`forcedimension.dhd.constants.ErrorNum.TIMEOUT`).

    See Also
    --------
    :data:`forcedimension.dhd.configGripperVelocity()`
    :data:`forcedimension.dhd.getGripperAngularVelocityRad()`
    :func:`forcedimension.dhd.getGripperAngularVelocityDeg()`


    :param c_double out:
        Output buffer to store the gripper linear velocity (in [m/s]).

    :param int ID:
         Device ID (see multiple devices section for details).

    :param SupportsPtr out:
        An output buffer to store the gripper linear velocity (in [m/s]).

    :raises TypeError:
        If ``out`` does not support item assignment either
        because its immutable or not subscriptable.

    :raises IndexError:
        If ``len(out) < 3``.

    :raises ArgumentError:
        If ``ID`` is not implicitly convertible to C char.

    :returns:
        0 on success, -1 otherwise.
    """

    return _libdhd.dhdGetGripperLinearVelocity(out, ID)


_libdhd.dhdGetGripperAngularVelocityRad.argtypes = [c_double_ptr, c_byte]
_libdhd.dhdGetGripperAngularVelocityRad.restype = c_int


def getGripperAngularVelocityRad(out: c_double, ID: int = -1) -> int:
    """
    Retrieve the estimated angular velocity of the gripper (in [rad/s]).

    Info
    ----
    The velocity estimator requires at least 2 position
    updates during the time interval defined in
    :func:`forcedimension.dhd.configGripperVelocity()` in order to be able to
    compute the estimate. Otherwise, e.g. if there are no calls to
    :func:`forcedimension.dhd.getPosition()`,
    :func:`forcedimension.dhd.getGripperAngularVelocityRad()`,
    or :func:`forcedimension.dhd.getGripperAngularVelocityRad()` will return an
    error (:data:`forcedimension.dhd.constants.ErrorNum.TIMEOUT`).

    See Also
    --------
    :func:`forcedimension.dhd.configGripperVelocity()`
    :func:`forcedimension.dhd.getGripperLinearVelocity()`
    :func:`forcedimension.dhd.getGripperAngularVelocityDeg()`


    :param int ID:
         Device ID (see multiple devices section for details).

    :param c_double out:
        An output buffer to store the gripper angular velocity (in [rad/s])

    :raises ArgumentError:
        If ``ID`` is not implicitly convertible to C char.

    :returns:
        0 on success, -1 otherwise.
    """

    return _libdhd.dhdGetGripperAngularVelocityRad(out, ID)


_libdhd.dhdGetGripperAngularVelocityDeg.argtypes = [c_double_ptr, c_byte]
_libdhd.dhdGetGripperAngularVelocityDeg.restype = c_int


def getGripperAngularVelocityDeg(out: c_double, ID: int = -1) -> int:
    """
    Retrieve the estimated angular velocity of the gripper (in [rad/s]).
    Velocity computation can be figured by calling:

    :func:`forcedimension.dhd.configGripperVelocity()`

    By default:
    :func:`forcedimension.dhd.constants.VELOCITY_WINDOW` and
    :func:`forcedimension.dhd.constant.VELOCITY_WINDOWING`
    are used. See velocity estimator for details.

    Please note that the velocity estimator requires at least 2 position
    updates during the time interval defined in:
    :func:`forcedimension.dhd.configGripperVelocity()`

    in order to be able to compute the estimate. Otherwise, e.g. if there are
    no calls to:
    :func:`forcedimension.dhd.getPosition()`
    :func:`forcedimension.dhd.getGripperLinearVelocity()`
    within the time interval window, this function will set an error with:
    :data:`forcedimension.dhd.constants.ErrorNum.TIMEOUT`

    See Also
    --------
    :func:`forcedimension.dhd.configGripperVelocity()`
    :func:`forcedimension.dhd.getGripperLinearVelocity()`
    :func:`forcedimension.dhd.getGripperAngularVelocityRad()`


    :param int ID:
         Device ID (see multiple devices section for details).

    :param c_double out:
        An output buffer to store the gripper angular velocity (in [deg/s]).

    :returns:
        0 on success, and -1 otherwise.
    """

    return _libdhd.dhdGetGripperAngularelocityDeg(out, ID)

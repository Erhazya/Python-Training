# Copyright (C) 2022 The Qt Company Ltd.
# SPDX-License-Identifier: LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only
from __future__ import annotations

"""
This file contains the exact signatures for all functions in module
PySide6.Qt3DInput, except for defaults which are replaced by "...".
"""

# Module `PySide6.Qt3DInput`

import PySide6.Qt3DInput
import PySide6.QtCore
import PySide6.QtGui
import PySide6.Qt3DCore

import enum
from typing import ClassVar, List, Optional, Sequence, Type, overload
from PySide6.QtCore import Signal
from shiboken6 import Shiboken


NoneType = type(None)


class QIntList(object): ...


class Qt3DInput(Shiboken.Object):

    class QAbstractActionInput(PySide6.Qt3DCore.Qt3DCore.QNode): ...

    class QAbstractAxisInput(PySide6.Qt3DCore.Qt3DCore.QNode):

        sourceDeviceChanged      : ClassVar[Signal] = ... # sourceDeviceChanged(QAbstractPhysicalDevice*)
        def setSourceDevice(self, sourceDevice: PySide6.Qt3DInput.Qt3DInput.QAbstractPhysicalDevice) -> None: ...
        def sourceDevice(self) -> PySide6.Qt3DInput.Qt3DInput.QAbstractPhysicalDevice: ...

    class QAbstractPhysicalDevice(PySide6.Qt3DCore.Qt3DCore.QNode):

        def __init__(self, parent: Optional[PySide6.Qt3DCore.Qt3DCore.QNode] = ...) -> None: ...

        def addAxisSetting(self, axisSetting: PySide6.Qt3DInput.Qt3DInput.QAxisSetting) -> None: ...
        def axisCount(self) -> int: ...
        def axisIdentifier(self, name: str) -> int: ...
        def axisNames(self) -> List[str]: ...
        def axisSettings(self) -> List[PySide6.Qt3DInput.Qt3DInput.QAxisSetting]: ...
        def buttonCount(self) -> int: ...
        def buttonIdentifier(self, name: str) -> int: ...
        def buttonNames(self) -> List[str]: ...
        def removeAxisSetting(self, axisSetting: PySide6.Qt3DInput.Qt3DInput.QAxisSetting) -> None: ...

    class QAction(PySide6.Qt3DCore.Qt3DCore.QNode):

        activeChanged            : ClassVar[Signal] = ... # activeChanged(bool)

        def __init__(self, parent: Optional[PySide6.Qt3DCore.Qt3DCore.QNode] = ...) -> None: ...

        def addInput(self, input: PySide6.Qt3DInput.Qt3DInput.QAbstractActionInput) -> None: ...
        def inputs(self) -> List[PySide6.Qt3DInput.Qt3DInput.QAbstractActionInput]: ...
        def isActive(self) -> bool: ...
        def removeInput(self, input: PySide6.Qt3DInput.Qt3DInput.QAbstractActionInput) -> None: ...

    class QActionInput(PySide6.Qt3DInput.Qt3DInput.QAbstractActionInput):

        buttonsChanged           : ClassVar[Signal] = ... # buttonsChanged(QList<int>)
        sourceDeviceChanged      : ClassVar[Signal] = ... # sourceDeviceChanged(QAbstractPhysicalDevice*)

        def __init__(self, parent: Optional[PySide6.Qt3DCore.Qt3DCore.QNode] = ...) -> None: ...

        def buttons(self) -> List[int]: ...
        def setButtons(self, buttons: Sequence[int]) -> None: ...
        def setSourceDevice(self, sourceDevice: PySide6.Qt3DInput.Qt3DInput.QAbstractPhysicalDevice) -> None: ...
        def sourceDevice(self) -> PySide6.Qt3DInput.Qt3DInput.QAbstractPhysicalDevice: ...

    class QAnalogAxisInput(PySide6.Qt3DInput.Qt3DInput.QAbstractAxisInput):

        axisChanged              : ClassVar[Signal] = ... # axisChanged(int)

        def __init__(self, parent: Optional[PySide6.Qt3DCore.Qt3DCore.QNode] = ...) -> None: ...

        def axis(self) -> int: ...
        def setAxis(self, axis: int) -> None: ...

    class QAxis(PySide6.Qt3DCore.Qt3DCore.QNode):

        valueChanged             : ClassVar[Signal] = ... # valueChanged(float)

        def __init__(self, parent: Optional[PySide6.Qt3DCore.Qt3DCore.QNode] = ...) -> None: ...

        def addInput(self, input: PySide6.Qt3DInput.Qt3DInput.QAbstractAxisInput) -> None: ...
        def inputs(self) -> List[PySide6.Qt3DInput.Qt3DInput.QAbstractAxisInput]: ...
        def removeInput(self, input: PySide6.Qt3DInput.Qt3DInput.QAbstractAxisInput) -> None: ...
        def value(self) -> float: ...

    class QAxisAccumulator(PySide6.Qt3DCore.Qt3DCore.QComponent):

        scaleChanged             : ClassVar[Signal] = ... # scaleChanged(float)
        sourceAxisChanged        : ClassVar[Signal] = ... # sourceAxisChanged(Qt3DInput::QAxis*)
        sourceAxisTypeChanged    : ClassVar[Signal] = ... # sourceAxisTypeChanged(QAxisAccumulator::SourceAxisType)
        valueChanged             : ClassVar[Signal] = ... # valueChanged(float)
        velocityChanged          : ClassVar[Signal] = ... # velocityChanged(float)

        class SourceAxisType(enum.Enum):

            Velocity                 : Qt3DInput.QAxisAccumulator.SourceAxisType = ... # 0x0
            Acceleration             : Qt3DInput.QAxisAccumulator.SourceAxisType = ... # 0x1


        def __init__(self, parent: Optional[PySide6.Qt3DCore.Qt3DCore.QNode] = ...) -> None: ...

        def scale(self) -> float: ...
        def setScale(self, scale: float) -> None: ...
        def setSourceAxis(self, sourceAxis: PySide6.Qt3DInput.Qt3DInput.QAxis) -> None: ...
        def setSourceAxisType(self, sourceAxisType: PySide6.Qt3DInput.Qt3DInput.QAxisAccumulator.SourceAxisType) -> None: ...
        def sourceAxis(self) -> PySide6.Qt3DInput.Qt3DInput.QAxis: ...
        def sourceAxisType(self) -> PySide6.Qt3DInput.Qt3DInput.QAxisAccumulator.SourceAxisType: ...
        def value(self) -> float: ...
        def velocity(self) -> float: ...

    class QAxisSetting(PySide6.Qt3DCore.Qt3DCore.QNode):

        axesChanged              : ClassVar[Signal] = ... # axesChanged(QList<int>)
        deadZoneRadiusChanged    : ClassVar[Signal] = ... # deadZoneRadiusChanged(float)
        smoothChanged            : ClassVar[Signal] = ... # smoothChanged(bool)

        def __init__(self, parent: Optional[PySide6.Qt3DCore.Qt3DCore.QNode] = ...) -> None: ...

        def axes(self) -> List[int]: ...
        def deadZoneRadius(self) -> float: ...
        def isSmoothEnabled(self) -> bool: ...
        def setAxes(self, axes: Sequence[int]) -> None: ...
        def setDeadZoneRadius(self, deadZoneRadius: float) -> None: ...
        def setSmoothEnabled(self, enabled: bool) -> None: ...

    class QButtonAxisInput(PySide6.Qt3DInput.Qt3DInput.QAbstractAxisInput):

        accelerationChanged      : ClassVar[Signal] = ... # accelerationChanged(float)
        buttonsChanged           : ClassVar[Signal] = ... # buttonsChanged(QList<int>)
        decelerationChanged      : ClassVar[Signal] = ... # decelerationChanged(float)
        scaleChanged             : ClassVar[Signal] = ... # scaleChanged(float)

        def __init__(self, parent: Optional[PySide6.Qt3DCore.Qt3DCore.QNode] = ...) -> None: ...

        def acceleration(self) -> float: ...
        def buttons(self) -> List[int]: ...
        def deceleration(self) -> float: ...
        def scale(self) -> float: ...
        def setAcceleration(self, acceleration: float) -> None: ...
        def setButtons(self, buttons: Sequence[int]) -> None: ...
        def setDeceleration(self, deceleration: float) -> None: ...
        def setScale(self, scale: float) -> None: ...

    class QInputAspect(PySide6.Qt3DCore.Qt3DCore.QAbstractAspect):

        def __init__(self, parent: Optional[PySide6.QtCore.QObject] = ...) -> None: ...

        def availablePhysicalDevices(self) -> List[str]: ...
        def createPhysicalDevice(self, name: str) -> PySide6.Qt3DInput.Qt3DInput.QAbstractPhysicalDevice: ...

    class QInputChord(PySide6.Qt3DInput.Qt3DInput.QAbstractActionInput):

        timeoutChanged           : ClassVar[Signal] = ... # timeoutChanged(int)

        def __init__(self, parent: Optional[PySide6.Qt3DCore.Qt3DCore.QNode] = ...) -> None: ...

        def addChord(self, input: PySide6.Qt3DInput.Qt3DInput.QAbstractActionInput) -> None: ...
        def chords(self) -> List[PySide6.Qt3DInput.Qt3DInput.QAbstractActionInput]: ...
        def removeChord(self, input: PySide6.Qt3DInput.Qt3DInput.QAbstractActionInput) -> None: ...
        def setTimeout(self, timeout: int) -> None: ...
        def timeout(self) -> int: ...

    class QInputSequence(PySide6.Qt3DInput.Qt3DInput.QAbstractActionInput):

        buttonIntervalChanged    : ClassVar[Signal] = ... # buttonIntervalChanged(int)
        timeoutChanged           : ClassVar[Signal] = ... # timeoutChanged(int)

        def __init__(self, parent: Optional[PySide6.Qt3DCore.Qt3DCore.QNode] = ...) -> None: ...

        def addSequence(self, input: PySide6.Qt3DInput.Qt3DInput.QAbstractActionInput) -> None: ...
        def buttonInterval(self) -> int: ...
        def removeSequence(self, input: PySide6.Qt3DInput.Qt3DInput.QAbstractActionInput) -> None: ...
        def sequences(self) -> List[PySide6.Qt3DInput.Qt3DInput.QAbstractActionInput]: ...
        def setButtonInterval(self, buttonInterval: int) -> None: ...
        def setTimeout(self, timeout: int) -> None: ...
        def timeout(self) -> int: ...

    class QInputSettings(PySide6.Qt3DCore.Qt3DCore.QComponent):

        eventSourceChanged       : ClassVar[Signal] = ... # eventSourceChanged(QObject*)

        def __init__(self, parent: Optional[PySide6.Qt3DCore.Qt3DCore.QNode] = ...) -> None: ...

        def eventSource(self) -> PySide6.QtCore.QObject: ...
        def setEventSource(self, eventSource: PySide6.QtCore.QObject) -> None: ...

    class QKeyEvent(PySide6.QtCore.QObject):

        @overload
        def __init__(self, ke: PySide6.QtGui.QKeyEvent) -> None: ...
        @overload
        def __init__(self, type: PySide6.QtCore.QEvent.Type, key: int, modifiers: PySide6.QtCore.Qt.KeyboardModifier, text: str = ..., autorep: bool = ..., count: int = ...) -> None: ...

        def count(self) -> int: ...
        def isAccepted(self) -> bool: ...
        def isAutoRepeat(self) -> bool: ...
        def key(self) -> int: ...
        def matches(self, key_: PySide6.QtGui.QKeySequence.StandardKey) -> bool: ...
        def modifiers(self) -> int: ...
        def nativeScanCode(self) -> int: ...
        def setAccepted(self, accepted: bool) -> None: ...
        def text(self) -> str: ...
        def type(self) -> PySide6.QtCore.QEvent.Type: ...

    class QKeyboardDevice(PySide6.Qt3DInput.Qt3DInput.QAbstractPhysicalDevice):

        activeInputChanged       : ClassVar[Signal] = ... # activeInputChanged(QKeyboardHandler*)

        def __init__(self, parent: Optional[PySide6.Qt3DCore.Qt3DCore.QNode] = ...) -> None: ...

        def activeInput(self) -> PySide6.Qt3DInput.Qt3DInput.QKeyboardHandler: ...
        def axisCount(self) -> int: ...
        def axisIdentifier(self, name: str) -> int: ...
        def axisNames(self) -> List[str]: ...
        def buttonCount(self) -> int: ...
        def buttonIdentifier(self, name: str) -> int: ...
        def buttonNames(self) -> List[str]: ...

    class QKeyboardHandler(PySide6.Qt3DCore.Qt3DCore.QComponent):

        asteriskPressed          : ClassVar[Signal] = ... # asteriskPressed(Qt3DInput::QKeyEvent*)
        backPressed              : ClassVar[Signal] = ... # backPressed(Qt3DInput::QKeyEvent*)
        backtabPressed           : ClassVar[Signal] = ... # backtabPressed(Qt3DInput::QKeyEvent*)
        callPressed              : ClassVar[Signal] = ... # callPressed(Qt3DInput::QKeyEvent*)
        cancelPressed            : ClassVar[Signal] = ... # cancelPressed(Qt3DInput::QKeyEvent*)
        context1Pressed          : ClassVar[Signal] = ... # context1Pressed(Qt3DInput::QKeyEvent*)
        context2Pressed          : ClassVar[Signal] = ... # context2Pressed(Qt3DInput::QKeyEvent*)
        context3Pressed          : ClassVar[Signal] = ... # context3Pressed(Qt3DInput::QKeyEvent*)
        context4Pressed          : ClassVar[Signal] = ... # context4Pressed(Qt3DInput::QKeyEvent*)
        deletePressed            : ClassVar[Signal] = ... # deletePressed(Qt3DInput::QKeyEvent*)
        digit0Pressed            : ClassVar[Signal] = ... # digit0Pressed(Qt3DInput::QKeyEvent*)
        digit1Pressed            : ClassVar[Signal] = ... # digit1Pressed(Qt3DInput::QKeyEvent*)
        digit2Pressed            : ClassVar[Signal] = ... # digit2Pressed(Qt3DInput::QKeyEvent*)
        digit3Pressed            : ClassVar[Signal] = ... # digit3Pressed(Qt3DInput::QKeyEvent*)
        digit4Pressed            : ClassVar[Signal] = ... # digit4Pressed(Qt3DInput::QKeyEvent*)
        digit5Pressed            : ClassVar[Signal] = ... # digit5Pressed(Qt3DInput::QKeyEvent*)
        digit6Pressed            : ClassVar[Signal] = ... # digit6Pressed(Qt3DInput::QKeyEvent*)
        digit7Pressed            : ClassVar[Signal] = ... # digit7Pressed(Qt3DInput::QKeyEvent*)
        digit8Pressed            : ClassVar[Signal] = ... # digit8Pressed(Qt3DInput::QKeyEvent*)
        digit9Pressed            : ClassVar[Signal] = ... # digit9Pressed(Qt3DInput::QKeyEvent*)
        downPressed              : ClassVar[Signal] = ... # downPressed(Qt3DInput::QKeyEvent*)
        enterPressed             : ClassVar[Signal] = ... # enterPressed(Qt3DInput::QKeyEvent*)
        escapePressed            : ClassVar[Signal] = ... # escapePressed(Qt3DInput::QKeyEvent*)
        flipPressed              : ClassVar[Signal] = ... # flipPressed(Qt3DInput::QKeyEvent*)
        focusChanged             : ClassVar[Signal] = ... # focusChanged(bool)
        hangupPressed            : ClassVar[Signal] = ... # hangupPressed(Qt3DInput::QKeyEvent*)
        leftPressed              : ClassVar[Signal] = ... # leftPressed(Qt3DInput::QKeyEvent*)
        menuPressed              : ClassVar[Signal] = ... # menuPressed(Qt3DInput::QKeyEvent*)
        noPressed                : ClassVar[Signal] = ... # noPressed(Qt3DInput::QKeyEvent*)
        numberSignPressed        : ClassVar[Signal] = ... # numberSignPressed(Qt3DInput::QKeyEvent*)
        pressed                  : ClassVar[Signal] = ... # pressed(Qt3DInput::QKeyEvent*)
        released                 : ClassVar[Signal] = ... # released(Qt3DInput::QKeyEvent*)
        returnPressed            : ClassVar[Signal] = ... # returnPressed(Qt3DInput::QKeyEvent*)
        rightPressed             : ClassVar[Signal] = ... # rightPressed(Qt3DInput::QKeyEvent*)
        selectPressed            : ClassVar[Signal] = ... # selectPressed(Qt3DInput::QKeyEvent*)
        sourceDeviceChanged      : ClassVar[Signal] = ... # sourceDeviceChanged(QKeyboardDevice*)
        spacePressed             : ClassVar[Signal] = ... # spacePressed(Qt3DInput::QKeyEvent*)
        tabPressed               : ClassVar[Signal] = ... # tabPressed(Qt3DInput::QKeyEvent*)
        upPressed                : ClassVar[Signal] = ... # upPressed(Qt3DInput::QKeyEvent*)
        volumeDownPressed        : ClassVar[Signal] = ... # volumeDownPressed(Qt3DInput::QKeyEvent*)
        volumeUpPressed          : ClassVar[Signal] = ... # volumeUpPressed(Qt3DInput::QKeyEvent*)
        yesPressed               : ClassVar[Signal] = ... # yesPressed(Qt3DInput::QKeyEvent*)

        def __init__(self, parent: Optional[PySide6.Qt3DCore.Qt3DCore.QNode] = ...) -> None: ...

        def focus(self) -> bool: ...
        def setFocus(self, focus: bool) -> None: ...
        def setSourceDevice(self, keyboardDevice: PySide6.Qt3DInput.Qt3DInput.QKeyboardDevice) -> None: ...
        def sourceDevice(self) -> PySide6.Qt3DInput.Qt3DInput.QKeyboardDevice: ...

    class QLogicalDevice(PySide6.Qt3DCore.Qt3DCore.QComponent):

        def __init__(self, parent: Optional[PySide6.Qt3DCore.Qt3DCore.QNode] = ...) -> None: ...

        def actions(self) -> List[PySide6.Qt3DInput.Qt3DInput.QAction]: ...
        def addAction(self, action: PySide6.Qt3DInput.Qt3DInput.QAction) -> None: ...
        def addAxis(self, axis: PySide6.Qt3DInput.Qt3DInput.QAxis) -> None: ...
        def axes(self) -> List[PySide6.Qt3DInput.Qt3DInput.QAxis]: ...
        def removeAction(self, action: PySide6.Qt3DInput.Qt3DInput.QAction) -> None: ...
        def removeAxis(self, axis: PySide6.Qt3DInput.Qt3DInput.QAxis) -> None: ...

    class QMouseDevice(PySide6.Qt3DInput.Qt3DInput.QAbstractPhysicalDevice):

        sensitivityChanged       : ClassVar[Signal] = ... # sensitivityChanged(float)
        updateAxesContinuouslyChanged: ClassVar[Signal] = ... # updateAxesContinuouslyChanged(bool)

        class Axis(enum.Enum):

            X                        : Qt3DInput.QMouseDevice.Axis = ... # 0x0
            Y                        : Qt3DInput.QMouseDevice.Axis = ... # 0x1
            WheelX                   : Qt3DInput.QMouseDevice.Axis = ... # 0x2
            WheelY                   : Qt3DInput.QMouseDevice.Axis = ... # 0x3


        def __init__(self, parent: Optional[PySide6.Qt3DCore.Qt3DCore.QNode] = ...) -> None: ...

        def axisCount(self) -> int: ...
        def axisIdentifier(self, name: str) -> int: ...
        def axisNames(self) -> List[str]: ...
        def buttonCount(self) -> int: ...
        def buttonIdentifier(self, name: str) -> int: ...
        def buttonNames(self) -> List[str]: ...
        def sensitivity(self) -> float: ...
        def setSensitivity(self, value: float) -> None: ...
        def setUpdateAxesContinuously(self, updateAxesContinuously: bool) -> None: ...
        def updateAxesContinuously(self) -> bool: ...

    class QMouseEvent(PySide6.QtCore.QObject):

        class Buttons(enum.Enum):

            NoButton                 : Qt3DInput.QMouseEvent.Buttons = ... # 0x0
            LeftButton               : Qt3DInput.QMouseEvent.Buttons = ... # 0x1
            RightButton              : Qt3DInput.QMouseEvent.Buttons = ... # 0x2
            MiddleButton             : Qt3DInput.QMouseEvent.Buttons = ... # 0x4
            BackButton               : Qt3DInput.QMouseEvent.Buttons = ... # 0x8


        class Modifiers(enum.Enum):

            NoModifier               : Qt3DInput.QMouseEvent.Modifiers = ... # 0x0
            ShiftModifier            : Qt3DInput.QMouseEvent.Modifiers = ... # 0x2000000
            ControlModifier          : Qt3DInput.QMouseEvent.Modifiers = ... # 0x4000000
            AltModifier              : Qt3DInput.QMouseEvent.Modifiers = ... # 0x8000000
            MetaModifier             : Qt3DInput.QMouseEvent.Modifiers = ... # 0x10000000
            KeypadModifier           : Qt3DInput.QMouseEvent.Modifiers = ... # 0x20000000


        def __init__(self, e: PySide6.QtGui.QMouseEvent) -> None: ...

        def button(self) -> PySide6.Qt3DInput.Qt3DInput.QMouseEvent.Buttons: ...
        def buttons(self) -> int: ...
        def isAccepted(self) -> bool: ...
        def modifiers(self) -> PySide6.Qt3DInput.Qt3DInput.QMouseEvent.Modifiers: ...
        def setAccepted(self, accepted: bool) -> None: ...
        def type(self) -> PySide6.QtCore.QEvent.Type: ...
        def wasHeld(self) -> bool: ...
        def x(self) -> int: ...
        def y(self) -> int: ...

    class QMouseHandler(PySide6.Qt3DCore.Qt3DCore.QComponent):

        clicked                  : ClassVar[Signal] = ... # clicked(Qt3DInput::QMouseEvent*)
        containsMouseChanged     : ClassVar[Signal] = ... # containsMouseChanged(bool)
        doubleClicked            : ClassVar[Signal] = ... # doubleClicked(Qt3DInput::QMouseEvent*)
        entered                  : ClassVar[Signal] = ... # entered()
        exited                   : ClassVar[Signal] = ... # exited()
        positionChanged          : ClassVar[Signal] = ... # positionChanged(Qt3DInput::QMouseEvent*)
        pressAndHold             : ClassVar[Signal] = ... # pressAndHold(Qt3DInput::QMouseEvent*)
        pressed                  : ClassVar[Signal] = ... # pressed(Qt3DInput::QMouseEvent*)
        released                 : ClassVar[Signal] = ... # released(Qt3DInput::QMouseEvent*)
        sourceDeviceChanged      : ClassVar[Signal] = ... # sourceDeviceChanged(QMouseDevice*)
        wheel                    : ClassVar[Signal] = ... # wheel(Qt3DInput::QWheelEvent*)

        def __init__(self, parent: Optional[PySide6.Qt3DCore.Qt3DCore.QNode] = ...) -> None: ...

        def containsMouse(self) -> bool: ...
        def setContainsMouse(self, contains: bool) -> None: ...
        def setSourceDevice(self, mouseDevice: PySide6.Qt3DInput.Qt3DInput.QMouseDevice) -> None: ...
        def sourceDevice(self) -> PySide6.Qt3DInput.Qt3DInput.QMouseDevice: ...

    class QWheelEvent(PySide6.QtCore.QObject):

        class Buttons(enum.Enum):

            NoButton                 : Qt3DInput.QWheelEvent.Buttons = ... # 0x0
            LeftButton               : Qt3DInput.QWheelEvent.Buttons = ... # 0x1
            RightButton              : Qt3DInput.QWheelEvent.Buttons = ... # 0x2
            MiddleButton             : Qt3DInput.QWheelEvent.Buttons = ... # 0x4
            BackButton               : Qt3DInput.QWheelEvent.Buttons = ... # 0x8


        class Modifiers(enum.Enum):

            NoModifier               : Qt3DInput.QWheelEvent.Modifiers = ... # 0x0
            ShiftModifier            : Qt3DInput.QWheelEvent.Modifiers = ... # 0x2000000
            ControlModifier          : Qt3DInput.QWheelEvent.Modifiers = ... # 0x4000000
            AltModifier              : Qt3DInput.QWheelEvent.Modifiers = ... # 0x8000000
            MetaModifier             : Qt3DInput.QWheelEvent.Modifiers = ... # 0x10000000
            KeypadModifier           : Qt3DInput.QWheelEvent.Modifiers = ... # 0x20000000


        def __init__(self, e: PySide6.QtGui.QWheelEvent) -> None: ...

        def angleDelta(self) -> PySide6.QtCore.QPoint: ...
        def buttons(self) -> int: ...
        def isAccepted(self) -> bool: ...
        def modifiers(self) -> PySide6.Qt3DInput.Qt3DInput.QWheelEvent.Modifiers: ...
        def setAccepted(self, accepted: bool) -> None: ...
        def type(self) -> PySide6.QtCore.QEvent.Type: ...
        def x(self) -> int: ...
        def y(self) -> int: ...


# eof
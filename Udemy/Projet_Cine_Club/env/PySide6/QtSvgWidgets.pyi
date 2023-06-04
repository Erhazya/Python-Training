# Copyright (C) 2022 The Qt Company Ltd.
# SPDX-License-Identifier: LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only
from __future__ import annotations

"""
This file contains the exact signatures for all functions in module
PySide6.QtSvgWidgets, except for defaults which are replaced by "...".
"""

# Module `PySide6.QtSvgWidgets`

import PySide6.QtSvgWidgets
import PySide6.QtCore
import PySide6.QtGui
import PySide6.QtWidgets
import PySide6.QtSvg

from typing import Optional, Union, overload


NoneType = type(None)


class QGraphicsSvgItem(PySide6.QtWidgets.QGraphicsObject):

    @overload
    def __init__(self, fileName: str, parentItem: Optional[PySide6.QtWidgets.QGraphicsItem] = ...) -> None: ...
    @overload
    def __init__(self, parentItem: Optional[PySide6.QtWidgets.QGraphicsItem] = ...) -> None: ...

    def boundingRect(self) -> PySide6.QtCore.QRectF: ...
    def elementId(self) -> str: ...
    def isCachingEnabled(self) -> bool: ...
    def maximumCacheSize(self) -> PySide6.QtCore.QSize: ...
    def paint(self, painter: PySide6.QtGui.QPainter, option: PySide6.QtWidgets.QStyleOptionGraphicsItem, widget: Optional[PySide6.QtWidgets.QWidget] = ...) -> None: ...
    def renderer(self) -> PySide6.QtSvg.QSvgRenderer: ...
    def setCachingEnabled(self, arg__1: bool) -> None: ...
    def setElementId(self, id: str) -> None: ...
    def setMaximumCacheSize(self, size: PySide6.QtCore.QSize) -> None: ...
    def setSharedRenderer(self, renderer: PySide6.QtSvg.QSvgRenderer) -> None: ...
    def type(self) -> int: ...


class QIntList(object): ...


class QSvgWidget(PySide6.QtWidgets.QWidget):

    @overload
    def __init__(self, file: str, parent: Optional[PySide6.QtWidgets.QWidget] = ...) -> None: ...
    @overload
    def __init__(self, parent: Optional[PySide6.QtWidgets.QWidget] = ...) -> None: ...

    @overload
    def load(self, contents: Union[PySide6.QtCore.QByteArray, bytes]) -> None: ...
    @overload
    def load(self, file: str) -> None: ...
    def paintEvent(self, event: PySide6.QtGui.QPaintEvent) -> None: ...
    def renderer(self) -> PySide6.QtSvg.QSvgRenderer: ...
    def sizeHint(self) -> PySide6.QtCore.QSize: ...


# eof

# -*- coding: utf-8 -*-
"""LINZ Redistricting Plugin - GUI Utilities

.. note:: This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.
"""

__author__ = '(C) 2018 by Nyall Dawson'
__date__ = '20/04/2018'
__copyright__ = 'Copyright 2018, LINZ'
# This will get replaced with a git SHA1 when you do a git archive
__revision__ = '$Format:%H$'

import os
from qgis.PyQt.QtGui import QIcon


class GuiUtils:
    """
    Utilities for GUI plugin components
    """

    @staticmethod
    def get_icon(icon: str):
        """
        Returns a plugin icon
        :param icon: icon name (svg file name)
        :return: QIcon
        """
        path = os.path.join(
            os.path.dirname(__file__),
            '..',
            'images',
            icon)
        if not os.path.exists(path):
            return QIcon()

        return QIcon(path)

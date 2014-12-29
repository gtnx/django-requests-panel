# -*- coding: utf-8 -*-

"""
requests_panel
~~~~~~~~~~~~~~

:copyright: (c) 2014 by .
:license: See LICENSE for more details.

"""

import pkg_resources

try:
    __version__ = pkg_resources.get_distribution('requests_panel').version
except Exception:
    __version__ = 'unknown'


__title__ = 'requests_panel'
__author__ = 'Guillaume Thomas'
__copyright__ = 'Copyright 2014 Guillaume Thomas'

VERSION = __version__

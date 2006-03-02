##############################################################################
#
# Copyright (c) 2004 Zope Corporation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
"""Setup for zope.interface package

$Id$
"""

import os

try:
    from setuptools import setup, Extension
except ImportError, e:
    from distutils.core import setup, Extension
    
setup(name='zope.interface',
      version='3.0',

      url='http://svn.zope.org/zope.interface',
      license='ZPL 2.1',
      description='Zope 3 Interface Infrastructure',
      author='Zope Corporation and Contributors',
      author_email='zope3-dev@zope.org',
      long_description='The implementation of interface definitions for Zope 3.',
      
      packages=["zope", "zope.interface"],
      package_dir = {'': os.path.join(os.path.dirname(__file__), 'src')},
      ext_package='zope.interface',
      ext_modules=[Extension("_zope_interface_coptimizations",
                             [os.path.join('src', 'zope', 'interface',
                                           "_zope_interface_coptimizations.c")
                              ]),
                   ],

      tests_require = ['zope.testing'],
      include_package_data = True,
      zip_safe = False,
      )
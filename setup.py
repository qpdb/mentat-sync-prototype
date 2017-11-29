# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.

from setuptools import setup, find_packages
import os
import re

install_requires = ['SQLALchemy', 'unittest2', 'simplejson', 'pyramid',
                    'mozsvc>=0.8', 'cornice', 'PyMySQL',
                    'pymysql_sa', 'wsgiproxy',
                    'webtest', 'requests', 'testfixtures']

entry_points = """
[paste.app_factory]
main = mentatsync:main
"""

version = "0.0.1"


setup(name='MentatSync',
      version=version,
      packages=find_packages(),
      install_requires=install_requires,
      entry_points=entry_points,
      license='MPLv2.0',
      classifiers=[
        "Programming Language :: Python",
        "License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)",
        ],
      package_data={
          "mentatsync.tests": ["*.ini"],
      },
      include_package_data=True,
)

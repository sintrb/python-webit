# -*- coding: utf-8 -*-
import os, io
from setuptools import setup

from webit.webit import __version__
here = os.path.abspath(os.path.dirname(__file__))
README = io.open(os.path.join(here, 'README.rst'), encoding='UTF-8').read()
CHANGES = io.open(os.path.join(here, 'CHANGES.rst'), encoding='UTF-8').read()
setup(name='webit',
      version=__version__,
      description='A web tools by Python.',
      keywords=('web', 'tools', 'web tools'),
      long_description=README + '\n\n\n' + CHANGES,
      url='https://github.com/sintrb/webit',
      classifiers=[
          'Intended Audience :: End Users/Desktop',
          'Operating System :: OS Independent',
          'Programming Language :: Python :: 2.7',
      ],
      author='sintrb',
      author_email='sintrb@gmail.com',
      license='Apache',
      packages=['webit'],
      scripts=['webit/webit', 'webit/webit.bat'],
      include_package_data=True,
      zip_safe=False)

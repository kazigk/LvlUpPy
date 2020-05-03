#!/usr/bin/env python3

import setuptools

setuptools.setup(
  name='lvluppy',
  version='1.0',
  description='Python bindings for LvlUp.pro API',
  author='Gaweł Kazimierczuk',
  author_email='kazi@kazigk.me',
  url='https://github.com/kazigk/lvluppy',
  packages=setuptools.find_packages(),
  requires=['requests']
  )

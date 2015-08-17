#!/usr/bin/env python
# -*- coding: utf-8; mode: python; tab-width: 4; indent-tabs-mode: nil; c-basic-offset: 4 -*- vim:fenc=utf-8:ft=python:et:sw=4:ts=4:sts=4

from setuptools import setup
import os

package = 'foramt-logger'
version = '0.1'
required_packages = os.path.walk(os.path.dirname(__file__))

setup(name=package,
      version=version,
      description="description",
      url='url')


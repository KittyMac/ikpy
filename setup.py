#!/usr/bin/env python
from setuptools import setup

setup(name='ikpy',
      version='2.2.3',
      author="Pierre Manceron",
      description="An inverse kinematics library aiming performance and modularity",
      url="https://github.com/Phylliade/ikpy",
      license="GNU GENERAL PUBLIC LICENSE Version 3",
      packages=['ikpy'],
      package_dir={'': 'src'},
      setup_requires=['numpy'],
      install_requires=['numpy', 'scipy', 'sympy', "matplotlib"],
      # TODO: Move maptlotlib to extra_requires
      classifiers=[
          "Programming Language :: Python :: 2",
          "Programming Language :: Python :: 3",
          "Topic :: Scientific/Engineering",
      ]
      )

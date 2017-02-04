#!/usr/env/bin python3

import os
from setuptools import setup

setup(name="neuralmonkey",
      packages=["neuralmonkey",
                "neuralmonkey.config",
                "neuralmonkey.decoders",
                "neuralmonkey.encoders",
                "neuralmonkey.nn",
                "neuralmonkey.evaluators",
                "neuralmonkey.logbook",
                "neuralmonkey.model",
                "neuralmonkey.processors",
                "neuralmonkey.runners",
                "neuralmonkey.trainers",
                "neuralmonkey.tests",
                "neuralmonkey.readers",
            ],
      install_requires=[
          "termcolor",
          "python-magic>=0.4.12",
          "flask",
          "ansiconv",
          "numpy",
          "pillow",
          "pygments",
          "typeguard",
          "pyter",
          "tensorflow"],
      dependency_links=[
          "http://github.com/aflc/pyter/tarball/master#egg=pyter-999.0.0"],
      scripts=["bin/neuralmonkey-train", "bin/neuralmonkey-run",
               "bin/neuralmonkey-logbook", "bin/neuralmonkey-server"],
      version="0.1.0",
      description="Neural Monkey: Sequence Learning Using TensorFlow",
      author="Jindřich Helcl, Jindřich Libovický, Tomáš Musil",
      author_email="helcl@ufal.ms.mff.cuni.cz",
      url="https://github.com/ufal/neuralmonkey",
      download_url="https://github.com/ufal/neuralmonkey/archive/0.1.0.tar.gz",
      keywords=["neural-machine-translation", "sequence-to-sequence",
                "neural-networks", "nlp", "tensorflow"],
      classifiers=["Development Status :: 3 - Alpha",
                   "Intended Audience :: Science/Research",
                   "License :: OSI Approved :: BSD License",
                   "Operating System :: OS Independent",
                   "Topic :: Scientific/Engineering"],
      license="BSD 3-clause")

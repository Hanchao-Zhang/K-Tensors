import os
from setuptools import find_packages, setup
import numpy as np
# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "KTensors",
    version = "0.1.0",
    author = "Hanchao Zhang",
    author_email = "hz1641@nyu.edu",
    license = "BSD",
    keywords = "Clustering Positive Semi-Denfinite Matrices",
    url = "https://github.com/Hanchao-Zhang/KTensors",
    packages=find_packages("KTensors"),
    py_modules=["KTensors"],
    long_description=read('README.md'),
    requires=['numpy'],
    install_requires=[
        'numpy',
    ]
    # classifiers=[
    #     "Development Status :: 3 - Alpha",
    #     "Topic :: Utilities",
    #     "License :: OSI Approved :: BSD License",
    # ],    
)
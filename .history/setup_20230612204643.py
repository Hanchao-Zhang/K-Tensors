import os
from setuptools import find_packages, setup

# read the contents of your README file
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()


# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="KTensors",
    description="K-Tensors",
    long_description=long_description,
    long_description_content_type="text/markdown",
    version="0.1.6",
    author="Hanchao Zhang",
    author_email="hz1641@nyu.edu",
    license="MIT",
    keywords="KTensors: Clustering Positive Semi-Denfinite Matrices",
    url="https://github.com/Hanchao-Zhang/KTensors",
    packages=find_packages("KTensors"),
    py_modules=["KTensors"],
    requires=["numpy", "scipy"],
    install_requires=["numpy", "scipy"],
    # classifiers=[
    #     "Development Status :: 3 - Alpha",
    #     "Topic :: Utilities",
    #     "License :: OSI Approved :: BSD License",
    # ],
)

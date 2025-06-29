from setuptools import find_packages, setup

#find_packages() will lookfor every construction file (__init__()) in every folder
# and will try to install that folder as a Local Package, so we can import


setup(
    name= "SmartCCTVHighway",
    version= "0.0.0",
    author= "Esmaeil Fakheri Alamdari",
    author_email= "mralamdari2000@gmail.com",
    packages= find_packages(),
    install_requires = []
)
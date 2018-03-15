from setuptools import find_packages
from setuptools import setup

setup(
  name="py-list-html-translator", 
  
  version="1.0.0",
  
  description='convert lists to html with py-list-html-translator', 

  url="https://github.com/critical-path/py-list-html-translator",

  author="critical-path",

  author_email="n/a",

  license="MIT",

  classifiers=[
    "Development Status :: 3 - Alpha",
    
    "Intended Audience :: Developers",

    "License :: OSI Approved :: MIT License",
    
    "Programming Language :: Python :: 3"
  ],

  keywords="py-list-html-translator python lists html translator",

  packages=find_packages(),

  extras_require={
    "test": [
      "py-test"
    ]
  }
)


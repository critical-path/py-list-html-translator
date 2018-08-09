from setuptools import (
    find_packages,
    setup
)


setup(
    name="py-list-html-translator",
    version="1.0.0",
    description="convert lists to html with py-list-html-translator",
    url="https://github.com/critical-path/py-list-html-translator",
    author="critical-path",
    author_email="n/a",
    license="MIT",
    classifiers=[
        "Development Status :: 2 - Alpha",
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3"
    ],
    keywords="python lists html translator translate",
    packages=find_packages(),
    extras_require={
        "test": [
            "coveralls",
            "pytest",
            "pytest-cov"
        ]
    }
)

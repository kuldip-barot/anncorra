"""Setup for the anncorra package."""

import setuptools


with open('README.md') as f:
    README = f.read()

setuptools.setup(
    author="Kuldeep Barot",
    #author_email="shay.palachy@gmail.com",
    name="anncorra",
    license="Apache License 2.0",
    description="Anncorra is a python package for giving meaning to POS (Part of Speech) tags.",
    version="v0.0.2",
    long_description=README,
    url='https://github.com/kuldip-barot/anncorra',
    packages=setuptools.find_packages(),
    python_requires=">=3.5",
    install_requires=[],
    classifiers=[
        # Trove classifiers
        # (https://pypi.python.org/pypi?%3Aaction=list_classifiers)
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Intended Audience :: Developers',
    ],
)

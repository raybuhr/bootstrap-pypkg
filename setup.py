# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='bootstrap-pypkg',
    version='0.1.0',
    description='Minimal CLI to help create new python packages',
    long_description=readme,
    author='Ray Buhr',
    author_email='raymond.buhr@gmail.com',
    url='https://github.com/raybuhr/bootstrap-pypkg',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os


def make_license(year, author):
    license = """Copyright (c) {year} {author}
All rights reserved.

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.
Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. 
IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; 
OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
""".format(year=year, author=author)
    return license


def make_setup(proj_name, author, email, description):
    setup_template = """# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='{name}',
    version='0.1.0',
    description='{desc}',
    long_description=readme,
    author='{author}',
    author_email='{email}',
    url='',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
""".format(name=proj_name, author=author, email=email, desc=description)
    return setup_template


def make_proj(proj_name, author, year, email, description):
    """Builds python package structure based on minimal user inputs.
    
    Arguments:
    proj_name -- PROJECT_NAME = input("Project name: ")
    author -- AUTHOR = input("Author name: ")
    year -- YEAR = datetime.date.today().year
    email -- EMAIL = input("Email: ")
    description -- SHORT_DESCRIPTION = input("Short description: ")
    """
    # create project directory structure
    pwd = os.path.abspath(os.curdir)
    proj_dir = os.path.join(pwd, proj_name)

    # create top level project files
    os.mkdir(proj_dir)
    os.chdir(proj_dir)
    with open("README.md", "w") as f:
        f.write("# {}\n\n{}\n".format(proj_name, description))
    open("requirements.txt", "a").close()
    with open("LICENSE", "w") as f:
        proj_license = make_license(year, author)
        f.write(proj_license)
    with open("setup.py", "w") as f:
        proj_setup = make_setup(proj_name, author, email, description)
        f.write(proj_setup)
    
    # make python package files
    proj_app = os.path.join(proj_name)
    os.mkdir(proj_app)
    os.chdir(proj_app)
    open("__init__.py", "a").close()
    open("{}.py".format(proj_name), "a").close()
    
    # create test init file
    os.chdir(proj_dir)
    os.mkdir("tests")
    os.chdir("tests")
    open("__init__.py", "a").close()
    open("test_{}.py".format(proj_name), "a").close()
    
    # return to original directory
    os.chdir(pwd)

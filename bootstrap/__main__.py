#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
import os
from bootstrap import *

PROJECT_NAME = input("Project name: ")
AUTHOR = input("Author name: ")
EMAIL = input("Email: ")
YEAR = datetime.date.today().year
SHORT_DESCRIPTION = input("Short description: ")

if not os.path.exists(PROJECT_NAME):
    make_proj(PROJECT_NAME, AUTHOR, YEAR, EMAIL, SHORT_DESCRIPTION)
else:
    raise SystemError("A directory for" + PROJECT_NAME + "already exists.")

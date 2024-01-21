#!/usr/bin/env python3
"""Script that sets up a Flask Blueprint (app_views) 
with a specified URL prefix, 
-imports views from different modules, 
-loads user data from a file using the User class. 
"""
from flask import Blueprint

app_views = Blueprint("app_views", __name__, url_prefix="/api/v1")

from api.v1.views.index import *
from api.v1.views.users import *
from api.v1.views.session_auth import *


User.load_from_file()
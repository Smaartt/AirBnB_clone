#!/usr/bin/python3
"""user classs
"""

from models.base_model import BaseModel
import json


class User(BaseModel):
    '''base modell class'''

    email = ""
    password = ""
    first_name = ""
    last_name = ""

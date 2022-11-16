#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
""" Playing with geopanda an panda

"""

import json
import math
import re
import os
import argparse
import sys
import requests  # Tested with Version: 2.27.1
import zipfile
from sqlalchemy import create_engine
from sqlalchemy import text
from sqlalchemy import insert
from sqlalchemy import MetaData
from sqlalchemy import Table, Column, Integer, String
from sqlalchemy import select
from sqlalchemy import update
from datetime import datetime
from datetime import timedelta
import logging

__author__      = "Pascal Vuylsteker"
__copyright__   = "Copyright 2022, Pascal Vuylsteker"
__credits__     = []
__license__     = "Copyright"
__version__     = "0.5.0"
__maintainer__  = "Pascal Vuylsteker"
__email__       = "pvk@vuylsteker.net"
__status__      = "Prototype"


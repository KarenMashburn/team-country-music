import io
from datetime import date
from typing import Optional

import pandas as pd
import requests
from bs4 import BeautifulSoup

from . import cache
from .utils import 

def get_soup(start_dt: date, end_dt: date) -> BeautifulSoup:
    # get most recent standings if date not specified
    # if((start_dt is None) or (end_dt is None)):
    #    print('Error: a date range needs to be specified')
    #    return None
    url = https://www.baseball-reference.com/leagues/majors/2020-standard-batting.shtml
     s = requests.get(url).content
    return BeautifulSoup(s, "lxml")



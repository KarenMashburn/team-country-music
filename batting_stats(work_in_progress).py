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

def get_table(soup: BeautifulSoup) -> pd.DataFrame:
    table = soup.find_all('table')[0]
    data = []
    headings = [th.get_text() for th in table.find("tr").find_all("th")][1:]
    data.append(headings)
    table_body = table.find('tbody')
    rows = table_body.find_all('tr')
    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        data.append([ele for ele in cols])
    df = pd.DataFrame(data)
    df = df.rename(columns=df.iloc[0])
    df = df.reindex(df.index.drop(0))
    return df

def batting_stats_range(start_dt: Optional[str] = None, end_dt: Optional[str] = None) -> pd.DataFrame:
    """
    Get all batting stats for a set time range. This can be the past week, the
    month of August, anything. Just supply the start and end date in YYYY-MM-DD
    format.
    """
    # make sure date inputs are valid
    start_dt_date, end_dt_date = sanitize_date_range(start_dt, end_dt)
    if start_dt_date.year < 2008:
        raise ValueError("Year must be 2008 or later")
    if end_dt_date.year < 2008:
        raise ValueError("Year must be 2008 or later")
    # retrieve html from baseball reference
    soup = get_soup(start_dt_date, end_dt_date)
    table = get_table(soup)
    table = table.dropna(how='all')  # drop if all columns are NA
    # scraped data is initially in string format.
    # convert the necessary columns to numeric.
    for column in ['Age', '#days', 'G', 'PA', 'AB', 'R', 'H', '2B', '3B',
                    'HR', 'RBI', 'BB', 'IBB', 'SO', 'HBP', 'SH', 'SF', 'GDP',
                    'SB', 'CS', 'BA', 'OBP', 'SLG', 'OPS']:
        #table[column] = table[column].astype('float')
        table[column] = pd.to_numeric(table[column])
        #table['column'] = table['column'].convert_objects(convert_numeric=True)
    table = table.drop('', 1)
    return table


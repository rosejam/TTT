#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from datetime import datetime, timedelta
import math
import re

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# --------------------------------------------------------
# 문자열 처리 유틸
# --------------------------------------------------------
def rm_sign(v):
    return re.sub(r'\+|\-', '', v)

# --------------------------------------------------------
# 시간 관련 유틸
# --------------------------------------------------------
FORMAT_DATE = "%Y%m%d"
FORMAT_DATETIME = "%Y%m%d%H%M%S"
FORMAT_MONTH = "%Y/%m"
FORMAT_MONTHDAY = "%m/%d"

import time
from pytz import timezone

def get_str_now():
    str_now = datetime.now().strftime(FORMAT_DATETIME)
    return str_now

def get_today():
    dt = datetime.fromtimestamp(time.time(), timezone('Asia/Seoul'))
    date = dt.date()
    return date

def get_date_ago(n):
    return get_today() - timedelta(days=n)

def get_str_today():
    str_today = get_today().strftime(FORMAT_DATE)
    return str_today
    
def get_str_date_ago(n):
    str_date = get_date_ago(n).strftime(FORMAT_DATE)
    return str_date

def get_str_month():
    str_month = get_today().strftime(FORMAT_MONTH)
    return str_month

def get_str_date_nago(n=20, base_date=None):
    if base_date is None:
        base_date = get_today()
    if type(base_date) is str:
        base_date = datetime.strptime()
    d = base_date - timedelta(days=n)
    return d.strftime(FORMAT_DATE)

def get_dayofweek():
    """
    :return: 0-4 평일, 5-6 주말
    """
    date_today = datetime.date.today()
    int_week = date_today.weekday()
    return int_week

def get_hour_min():
    dt_now = datetime.now()
    int_hour = dt_now.hour
    int_minute = dt_now.minute
    return int_hour, int_minute

def convert_date2month(str_date):
    if len(str_date) != 8:
        return None
    return '{}/{}'.format(str_date[:4], str_date[4:6])

def convert_str2date(str_date):
    return datetime.strptime(str_date, FORMAT_DATE)

def convert_date2str(dt):
    return dt.strftime(FORMAT_DATE)

def add_months(dt, months=1):
    return dt.replace(year=dt.year + math.floor((dt.month + months) / 12), month=max((dt.month + months) % 12, 1))

def convert_datetime2str(x):
    for k in x:
        if isinstance(x[k], datetime):
            x[k] = x[k].__str__()
    return x
    
# --------------------------------------------------------
# 변환 관련 유틸
# --------------------------------------------------------
def safe_cast(val, to_type, default=None):
    try:
        return to_type(val)
    except (ValueError, TypeError):
        return default

dict_conv = {
    '종목코드': ('code', str),
    '업종코드': ('code', str),
    '종목명': ('name', str),
    '회사명': ('name', str),
    '체결시간': ('time', int),
    '일자': ('date', int),
    '시가': ('open', float),
    '고가': ('high', float),
    '저가': ('low', float),
    '종가': ('close', float),
    '거래량': ('volume', float),
}

def convert_kv(d):
    _d = {}
    for k, v in d.items():
        if k in dict_conv:
            newk, vtype = dict_conv[k]
            _d[newk] = vtype(v)
        else:
            _d[k] = v
    return _d

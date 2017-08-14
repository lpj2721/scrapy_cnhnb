#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Tommy on 2017/8/14 12:08
import uuid
from datetime import datetime


def get_id():
    return str(uuid.uuid1())


def date_time():
    dt = datetime.now()
    return dt.strftime("%Y-%m-%d %H:%M:%S")


if __name__ == '__main__':
    print date_time()
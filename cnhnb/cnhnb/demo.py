#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Tommy on 2017/8/14 12:12
import uuid

name = "test_name"
name1 = "test"
namespace = uuid.uuid4()
print type(str(uuid.uuid1()))
print uuid.uuid3(namespace, name)
print uuid.uuid3(namespace, name1)
print uuid.uuid4()
print uuid.uuid5(namespace, name)
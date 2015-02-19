#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A complex testcase."""

EXPENSE = 14.23
LOOKS_NICE = True
MAX_EXPENSE = 12
GET_OUT_ALIVE = False

if not (LOOKS_NICE is True and EXPENSE <= MAX_EXPENSE):
    GET_OUT_ALIVE = True
    SACRIFICE = '{}'.format(GET_OUT_ALIVE)
    print SACRIFICE

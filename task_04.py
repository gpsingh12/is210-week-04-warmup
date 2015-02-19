#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A single if statement."""

MYINPUT = raw_input('Tell me a story! ')
MAX_LENGTH = 80
LONGSTR = 'long'
LENGTH = len(MYINPUT)

if not LENGTH > MAX_LENGTH:

    LONGSTR = 'short'

OUTPUT = 'That certainly was a {} story!'.format(LONGSTR)
print OUTPUT

#!/usr/bin/env python
#-*- coding: utf-8 -*-
""" Docstring."""
BP = raw_input('What is your blood pressure? ')
BP_STATUS = 'Low'

if   BP <= 89:

    BP_STATUS = 'Low'
    print 'Your status is currently {}'.format(BP_STATUS)

elif 90 <= BP <= 119:
     BP_STATUS = 'Ideal'
     print 'Your status is currently {}'.format(BP_STATUS)

elif 120 <= BP <= 139:
     BP_STATUS = 'Warning'
     print 'Your status is currently {}'.format(BP_STATUS)

elif 140 <= BP <= 159:
    BP_STATUS = 'High'
    print 'Your status is currently {}'.format(BP_STATUS)

else:
    BP_STATUS = 'Emergency'
    print  'Your status is currently {}'.format(BP_STATUS)

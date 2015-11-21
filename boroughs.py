#!usr/bin/env python
#-*- coding: utf-8 -*-
"""Restaurantuer scores"""


Grades = {
        'A': '{0:3f}.format(100%)',
        'B': '{0:3f}.format(90%)',
        'C': '{0:3f}.format(80%)',
        'D': '{0:3f}.format(70)',
        'F': '{0:3f}.format(60%)'
        }
def get_score_summary():
    rest_grades = open('inspection_result.csv', 'r')
    line = rest_grades.readline()
    while line != '':
        line = rest_grades.readline()
    print rest_grades()
    rest_grade.close()

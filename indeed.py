#coding:utf-8

import sys
import os
from utils import *
from collections import defaultdict

## mapping location to MSA
def trans_location(l):
    if "," not in location.split(" ")[-1]:
        return ' '.join(location.split(" ")[:-1])
    else:
        l

## statistic of 
def date_count_statistic():
    sql = 'select id,title,company,location,publishdate from job'

    query_op = dbop()
    cursor = query_op.query_database(sql)

    location_count = defaultdict(int)
    for row in cursor:
        jid,title,company,location,publishdate = row
        location = trans_location(location)
        location_count[location]+=1


    for location in location_count.keys():
        print location,location_count[location]



if __name__ == '__main__':
    date_count_statistic()








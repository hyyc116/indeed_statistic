#coding:utf-8

import sys
import os
from utils import *
from collections import defaultdict
import re



## mapping location to MSA
def trans_location(location):
    location = re.sub(r'\d+','===',location)
    return location.split("===")[0]

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

def salary():
    for f in os.listdir('Pages'):
        content = open('Pages/'+f).read().strip()

        if 'salary' in content or '$' in content:
            print f,content



if __name__ == '__main__':
    # date_count_statistic()
    salary()








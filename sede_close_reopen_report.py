#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 15:57:36 2017

@author: dhartig
"""

import mysql.connector, datetime
from matplotlib import pyplot as plt

def get_wb_cursor():
    db = mysql.connector.connect(user='dbuser', password='dbpass', database='worldbuilding')
    cursor = db.cursor()  
    return db, cursor

def gini(list_of_values):
    sorted_list = sorted(list_of_values)
    height, area = 0, 0
    for value in sorted_list:
        height += value
        area += height - value / 2.
    fair_area = height * len(list_of_values) / 2.
    return (fair_area - area) / fair_area

# Goes to worldbuilding database and reports on the gini score by month 
def report_gini():
    db, cursor = get_wb_cursor()
    
    qry = "SELECT userid, DATE_FORMAT(time, '%Y %m') AS month, COUNT(*) as cnt FROM user_time GROUP BY userid, month;"
    cursor.execute(qry)
    
    lst_by_month = {}
    
    for usrid, yrmon, cnt in cursor.fetchall():
        month = datetime.datetime.strptime(yrmon, "%Y %m")
        if month in lst_by_month:
            lst_by_month[month].append(cnt)
        else:
            lst_by_month[month] = [cnt]
            
    gini_by_month = [(month, gini(lst)) for month, lst in lst_by_month.items()]
    
    for m, g in sorted(gini_by_month, key = lambda x: x[0]):
        print(m, g)
        
    return gini_by_month
        
if __name__ == "__main__":
    ginilist = report_gini()
    plt.plot_date([m[0] for m in ginilist[:-1]], [s[1] for s in ginilist[-1]])
    plt.show()
    
    
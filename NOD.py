#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import datetime
import timeit
import xlwt
from xlwt import Workbook

wb = Workbook()
sheet1 = wb.add_sheet("Sheet 1")

def N1(a, b):
    gcd = 1
    for d in range(2, min(a, b) + 1):
        if a % d == 0 and b % d == 0:
            gcd = d
    return gcd

def N2(a, b):
    while b:
        a, b = b, a % b
    return a
count = 0

if __name__ == '__main__':
    for i in range(39188480,39188480+5):
        for j in range(16532640,16532640+5):
            print(count)
            st = datetime.datetime.now()
            g = N1(i,j)
            ed = datetime.datetime.now()
            elapsed = ed-st

            sheet1.write(count,0,i)
            sheet1.write(count, 1, j)
            sheet1.write(count,2,elapsed.total_seconds())

            a = 1000000
            elapsed = timeit.timeit(lambda: N2(i,j),number=a)

            sheet1.write(count,4,i)
            sheet1.write(count,5,j)
            sheet1.write(count,6,elapsed/a)
            count+=1

    wb.save("NOD.xls")
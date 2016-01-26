#!/usr/bin/python
# -*- coding: utf-8 -*-
import pandas as pd


train = pd.read_csv("mex_final.csv",header=0,delimiter=",",error_bad_lines=False)

fo = open("reviews_line.txt", 'w')

for i in xrange(0,train['reviews'].size):
	fo.write(str(train['reviews'][i]))

# Close opend file
fo.close()
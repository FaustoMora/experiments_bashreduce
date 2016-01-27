#!/usr/bin/python
# -*- coding: utf-8 -*-
import pandas as pd
import os

fileDir = os.path.dirname(os.path.realpath('__file__'))
train = pd.read_csv(os.path.join(fileDir, 'datasets/mex_final.csv'),header=0,delimiter=",",error_bad_lines=False)
fo = open(os.path.join(fileDir, 'datasets/reviews_line.txt'),'w')

for i in xrange(0,train['reviews'].size):
	if not pd.isnull(train['reviews'][i]):
		aux = str(train['reviews'][i]).replace('\n','.')
		aux = aux + '\n'
		fo.write(aux)

for i in xrange(0,train['descripcion'].size):
	if not pd.isnull(train['descripcion'][i]):
		aux = str(train['descripcion'][i]).replace('\n','.')
		aux = aux.replace('\r','')
		aux = aux.replace('\t',' ')
		aux = aux + '\n'
		fo.write(aux)

# Close opend file
fo.close()
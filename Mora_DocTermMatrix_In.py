#!/usr/bin/python
# -*- coding: utf-8 -*-
import pandas as pd
import os

fileDir = os.path.dirname(os.path.realpath('__file__'))
train = pd.read_csv(os.path.join(fileDir, 'datasets/mex_final.csv'),header=0,delimiter=",",error_bad_lines=False)
uk = pd.read_csv(os.path.join(fileDir, 'datasets/uk_final.csv'),header=0,delimiter=",",error_bad_lines=False)
fo1 = open(os.path.join(fileDir, 'datasets/reviews_line_1.txt'),'w')
fo2 = open(os.path.join(fileDir, 'datasets/reviews_line_2.txt'),'w')
fo3 = open(os.path.join(fileDir, 'datasets/reviews_line_3.txt'),'w')
fo4 = open(os.path.join(fileDir, 'datasets/reviews_line_4.txt'),'w')
fo5 = open(os.path.join(fileDir, 'datasets/reviews_line_5.txt'),'w')
fo6 = open(os.path.join(fileDir, 'datasets/reviews_line_8.txt'),'w')
fo7 = open(os.path.join(fileDir, 'datasets/reviews_line_7.txt'),'w')

#todos los reviews mex
for i in xrange(0,train['reviews'].size):
	if not pd.isnull(train['reviews'][i]):
		aux = str(train['reviews'][i])
		fo1.write(aux)

#todos los reviews y la descripcion de mex
for i in xrange(0,train['reviews'].size):
	if not pd.isnull(train['reviews'][i]):
		aux = str(train['reviews'][i])
		fo2.write(aux)
		fo3.write(aux)
		fo4.write(aux)
		fo5.write(aux)

for i in xrange(0,train['descripcion'].size):
	if not pd.isnull(train['descripcion'][i]):
		aux = str(train['descripcion'][i])
		fo2.write(aux)
		fo3.write(aux)
		fo4.write(aux)
		fo5.write(aux)

#todos los reviews/desc de mex y medio reviews de uk
for i in xrange(0,(uk['reviews'].size)/2):
	if not pd.isnull(uk['reviews'][i]):
		aux = str(uk['reviews'][i])
		fo3.write(aux)

#todos los reviews/desc de mex y todos los reviews de uk
for i in xrange(0,(uk['reviews'].size)):
	if not pd.isnull(uk['reviews'][i]):
		aux = str(uk['reviews'][i])
		fo4.write(aux)

#todos los reviews/desc de mex y todos los reviews/desc de uk
for i in xrange(0,uk['reviews'].size):
	if not pd.isnull(uk['reviews'][i]):
		aux = str(uk['reviews'][i])
		fo5.write(aux)

for i in xrange(0,uk['descripcion'].size):
	if not pd.isnull(uk['descripcion'][i]):
		aux = str(uk['descripcion'][i])
		fo5.write(aux)

#todos los reviews de mex x2 y todos los reviews de uk
for i in xrange(0,train['reviews'].size):
	if not pd.isnull(train['reviews'][i]):
		aux = str(train['reviews'][i])
		fo6.write(aux)
		fo7.write(aux)

for i in xrange(0,uk['reviews'].size):
	if not pd.isnull(uk['reviews'][i]):
		aux = str(uk['reviews'][i])
		fo6.write(aux)
		fo7.write(aux)

for i in xrange(0,train['reviews'].size):
	if not pd.isnull(train['reviews'][i]):
		aux = str(train['reviews'][i])
		fo6.write(aux)
		fo7.write(aux)

#todos los reviews de mex x2 y todos los reviews de uk x2
for i in xrange(0,uk['reviews'].size):
	if not pd.isnull(uk['reviews'][i]):
		aux = str(uk['reviews'][i])
		fo6.write(aux)
		fo7.write(aux)

for i in xrange(0,uk['descripcion'].size):
	if not pd.isnull(uk['descripcion'][i]):
		aux = str(uk['descripcion'][i])
		fo6.write(aux)

for i in xrange(0,train['descripcion'].size):
	if not pd.isnull(train['descripcion'][i]):
		aux = str(train['descripcion'][i])
		fo6.write(aux)

# Close opend file
fo1.close()
fo2.close()
fo3.close()
fo4.close()
fo5.close()
fo6.close()
fo7.close()

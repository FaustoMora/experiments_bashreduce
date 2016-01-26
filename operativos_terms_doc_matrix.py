#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import re

dictionario = {}
#for line in var:
for line in sys.stdin:
	line = line.replace('á','a').replace('é','e').replace('í','i').replace('ó','o').replace('ú','u');
	line = re.sub('[0-9,#,!,¡,&,.]','',line)
	line = re.sub('[^a-zA-Z]'," ",line)
	array_review = 	line.lower().split()

	for i in array_review:
		if i not in dictionario:
			dictionario[i]=1
		else:
			a = dictionario[i]
			dictionario.update({i:a+1})
	
	for key,value in dictionario.items():
		print str(key)+','+str(value)

		


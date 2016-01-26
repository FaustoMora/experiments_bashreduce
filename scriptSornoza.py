#!/usr/bin/python
#coding=utf-8
import re
import sys

i = 0
for line in sys.stdin:
	n1 = re.sub(r'[^a-zA-Z0-9ñÑáéíóúÁÉÍÓÚ]',r',',line)
	n2 = re.sub(r'[\t\n\r\f]',r' ',n1)
	n3 = re.sub(r'[,]+',' ', n2)
	if n3.strip():
		i = i + 1
		salto = '\n'
		n4 = 'Recorrido ' +  str(i) + ':'+ salto  + n3 + salto
		print n4

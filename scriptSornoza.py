#!/usr/bin/python

import re
import sys
from random import randint

i = 0
for line in sys.stdin:
	n1 = re.sub(r'[?|$|.|!]',r'',line)
	n2 = re.sub(r'[^a-zA-Z0-9 ]',r'',n1)
	if n2.strip():
		i = i + 1
		salto = '\n'
		n3 = 'Recorrido ' +  str(i) + ':'+ salto  + n2 + salto
		print n3

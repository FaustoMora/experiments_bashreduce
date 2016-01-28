#!/usr/bin/python
# -*- coding: utf-8 -*-
import re
import sys


for line in sys.stdin:
	
	line1 = re.sub(r'[^a-zA-ZñÑáéíóúÁÉÍÓÚ]',r' ',line)
	line2 = line1.upper()
	print line2

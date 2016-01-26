#!/usr/bin/python

import re
import sys

for line in sys.stdin:
	nstr = re.sub(r'[?|$|.|!]',r'',line)
	nestr = re.sub(r'[^a-zA-Z0-9 ]',r'',nstr)
	if line != '\n' or '':
		print nestr

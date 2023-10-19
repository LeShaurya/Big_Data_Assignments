#!/usr/bin/env python3
"""mapper.py"""

import sys

for line in sys.stdin:
	line = line.strip()
	word = line.split('\t')

	if word[0] == "order":
		print('%s\t%s\t%s\t%s\t%s'%(word[3], word[2], word[0], word[4], word[5]))
	elif word[0] == "review":
		print('%s\t%s\t%s\t%s\t%s'%(word[2], word[3], word[0], word[4], word[5]))
	else:
		continue
		
	

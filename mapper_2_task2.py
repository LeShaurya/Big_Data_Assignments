#!/usr/bin/env python3
"""mapper.py"""

import sys

for line in sys.stdin:
	line = line.strip()
	word = line.split('\t')

	print(f'{word[0]}\t{word[1]}\t{word[2]}\t{word[3]}')


	

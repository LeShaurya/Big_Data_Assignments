#!/usr/bin/env python3
"""mapper.py"""

import sys

for line in sys.stdin:
	line = line.strip()
	pid, cid , qty, stars = line.split('\t')
	print(f'{pid}\t{qty}')


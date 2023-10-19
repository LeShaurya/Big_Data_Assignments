#!/usr/bin/env python3
"""reducer.py"""

import sys

prev_cid = None
prev_pid = None
prev_star = None
prev_qty = None
prev_price = None
prev_text = None

prev_word = None
prev_count = 0


for line in sys.stdin:
	line = line.strip()
	product_id, qty= line.split('\t')

	if prev_pid == product_id:
		prev_qty += int(qty)

	else:
		if prev_pid:
			prev_qty = str(prev_qty)
			prev_star = str(prev_star)
			print(f'{prev_pid}\t{prev_qty}')
		prev_pid = product_id
		prev_qty = int(qty)


if prev_pid:
	prev_qty = str(prev_qty)

	print(f'{prev_pid}\t{prev_qty}')

	


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
	product_id, customer_id, qty, stars= line.split('\t')
	if (int(stars)<3 and int(stars)>0 ):
		print(f'{product_id}\t{customer_id}\t{qty}\t{stars}')
'''		
	else:
		if prev_pid == product_id:
			prev_qty += int(qty)
		else:
			if prev_pid:
				prev_star = "0"
				print('%s\t%s\t%s\t%s'%(prev_pid,prev_cid,prev_qty,prev_star))
			prev_cid = customer_id
			prev_pid = product_id
			prev_qty = int(qty)
			prev_star = stars'''

	
	


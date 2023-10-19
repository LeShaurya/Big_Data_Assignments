#!/usr/bin/env python3
"""mapper.py"""

import sys

result = {}


for line in sys.stdin:
	line = line.strip()
	word = line.split('\t')
#	type_table, some_id, product_id, customer_id, qty_or_star, price_or_review = word

	if word[0] == "order":
#		key = f"{customer_id}\t{product_id}\t"
#		value = f"{type_table}\t{qty_or_star}"

		print('%s\t%s\t%s\t%s'%(word[3], word[2], word[0], word[4]))
	elif word[0] == "review":
#	key = f"{product_id}\t{customer_id}\t"
#		value = f"{type_table}\t{qty_or_star}"
		print('%s\t%s\t%s\t%s'%(word[2], word[3], word[0], word[4]))
	else:
		continue
		
#	result[key] = [value]
#	print(f"{key}\t{value}")
		
	

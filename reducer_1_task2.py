#!/usr/bin/env python3
"""reducer.py"""


import sys

if __name__ == "__main__":


	result = {}
	
	for line in sys.stdin:
		line = line.strip()
		product_id, customer_id,table_type, qty_or_star = line.split('\t')
		
		if (product_id, customer_id) not in result:
			result.setdefault((product_id, customer_id),{'qty':0, 'stars':0})
			
		if table_type == "order":
			result[(product_id, customer_id)]['qty'] += int(qty_or_star)
		elif table_type == "review":
			result[(product_id, customer_id)]['stars'] += int(qty_or_star)
		else:
			continue
			
	for keys, values in result.items():
		qty = values["qty"]
		stars = values["stars"]
		print('%s\t%s\t%s\t%s\t'%(keys[0], keys[1], qty, stars))


#		print(word)

'''
	for 
		
		if (prev_cid == customer_id and prev_pid == product_id):
#			print('%s\t%s\t%s\t%s'%(product_id,customer_id,prev_qty_or_star,qty_or_star))
			print(f"{product_id}\t{customer_id}\t{prev_qty_or_star}\t{qty_or_star}")
			prev_cid = customer_id
			prev_pid = product_id
			prev_qty_or_star = qty_or_star
			prev_type = type_table
			
		elif (prev_cid == None):
			prev_cid = customer_id
			prev_pid = product_id
			prev_qty_or_star = qty_or_star
			prev_type = type_table
		else:
			if (prev_type == type_table):
				stars = "0"
#				print('%s\t%s\t%s\t%s'%(product_id,customer_id,prev_qty_or_star,stars))
				print(f"{product_id}\t{customer_id}\t{prev_qty_or_star}\t{stars}")
			prev_cid = customer_id
			prev_pid = product_id
			prev_qty_or_star = qty_or_star
			prev_type = type_table
	
	
'''

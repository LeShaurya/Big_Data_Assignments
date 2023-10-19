#!/usr/bin/env python3
import sys
if __name__ == "__main__":
    prevName = None
    match = 0
    sum_strike_rate = float(0)
    for line in sys.stdin:
    	name, local_strike_rate = line.strip().split('\t')
        if prevName == name:
            sum_strike_rate += float(local_strike_rate)
        else:
            if prevName:
                data = {"name": prevName,"strike_rate": round(sum_strike_rate/match, 3)}
                print(f'{{"name": "{data["name"]}", "strike_rate": {data["strike_rate"]}}}')
            prevName = name
            match = 0
            sum_strike_rate = float(local_strike_rate)
        match += 1
    if prevName:
        data = {"name": prevName,"strike_rate": round(sum_strike_rate/match, 3)}
        print(f'{{"name": "{data["name"]}", "strike_rate": {data["strike_rate"]}}}')

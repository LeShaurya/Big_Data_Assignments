#!/usr/bin/env python3

import sys
import json

if __name__ == "__main__":

    for line in sys.stdin:
        if line.startswith('[') or line.startswith(']'):
            continue
        data = json.loads(line.strip().rstrip(','))
        runs = float(data['runs'])
        balls = float(data['balls'])
        
        strike_rate = float(0)
        
        if balls == 0:
            strike_rate = 0
        else:
            strike_rate = round((runs / balls)*100, 3)

        print(f"{data['name']}\t{strike_rate}")

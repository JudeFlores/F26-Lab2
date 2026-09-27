# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Jude Flores
# Date: September 27, 2026
# Purpose: Learn how to use while loops with break and continue.
# Usage: ./lab2j.py
import math
while True:
    num = input("Enter a number: ")
    num = float(num)
    if num < 0:
        print("Invalid number")
        continue
    elif num == 0:
        print("Exiting...")
        break
    else:
        print(f"{math.sqrt(num):.1f}")

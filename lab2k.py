# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Jude Flores
# Date: September 27, 2026
# Purpose: use for loop.
# Usage: ./lab2k.py

# TO DO 1: 
#Follow the instructions given in the README.md file.
num = 0
for i in range (1, 101):
    if i % 2 == 0:
        num = num + i
print("Total is ", num)
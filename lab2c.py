
# Add comments before you do anything else.

#!/usr/bin/env python3
# Author:Jude Flores
# Date:September 23, 2026
# Purpose: Practice using if, elif, and else statments.
# Usage: ./lab2c.py

str1 = input("Enter a sentence: ")
str2 = input("Enter another sentence: ")

if len(str1) > len(str2):
    print("str1 is longer than str2")
elif len(str1) == len(str2):
    print("str1 and str2 are equal.")
else:
    print("str2 is longer than str1")


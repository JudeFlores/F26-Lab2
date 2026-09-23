# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Jude Flores
# Date: September 23, 2026
# Purpose: Learn how and practice using nested if, elif, and else statments..
# Usage: ./lab2g.py

# TO DO 1: Follow the instructions given in README.md file
# Initialize constant variables for the tax rates and rate limits.
income = int(input("Enter your income: "))
status = input("Enter wheter you are 'single' or 'married':").lower()
if status == "single":
    if income <= 32000:
        tax = income*0.1
        print(f"Your tax is ${tax}")
    else:
        tax = ((income-32000)*.25)+3200
        print(f"Your tax is ${tax}")
else:
    if income <=64000:
        tax = income*0.1
        print(f"Your tax is ${tax}")
    else:
        tax = ((income-64000)*0.25)+6400
        print(f"your tax is ${tax}")


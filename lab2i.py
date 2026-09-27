# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Jude Flores
# Date: September 27, 2026
# Purpose: Learn how to use while loops for validating user input.
# Usage: ./lab2i.py

pin = input("Please type in your pin: ")
while pin != "1234" :
    print("Incorrect...try again")
    pin = input("Please type in your pin: ")
print("Correct PIN, you can enter!")

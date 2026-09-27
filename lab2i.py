# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Jude Flores
# Date: September 27, 2026
# Purpose: Learn how to use while loops for validating user input.
# Usage: ./lab2i.py

# TO DO 1: 
# Creat variable pin. The value of pin should be a 4 digit code inputted by the user.
# Add a while loop to create program that wont end until the user enters 1234.
# Follow the specific instructions given in the README.md file.
# Define the correct PIN
pin = input("Please type in your pin: ")
while pin != "1234" :
    print("Incorrect...try again")
    pin = input("Please type in your pin: ")
print("Correct PIN, you can enter!")

# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Jude Flores
# Date: September 23, 2026
# Purpose: Learn how to use command line arguments.
# Usage: ./lab2f.py

# TO DO 1: Follow the instructions given in README.md file
import sys

num_args = len(sys.argv)-1
if num_args < 2:
    print("This script requires at least two arguments")
else:
    name = sys.argv[1]
    age = sys.argv[2]
    if num_args == 2:
        print(f"Hi {name}, you are {age} years old and the script received {num_args} arguments")
    else:
        print(f"Hi {name}, you are {age} and the script has recieved {num_args} arguments.")

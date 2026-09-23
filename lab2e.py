# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Jude Flores
# Date: September 23, 2026
# Purpose: Learn how to use command line arguments.
# Usage: ./lab2e.py

# TO DO 1: Follow the instructions given in README.md file
import sys

print(sys.argv)
print(len(sys.argv))
num_args = len(sys.argv) - 1
if num_args < 2:
    print("This script requires exactly two arguments. No arguments were provided!")
else:
    name = sys.argv[1]
    age = sys.argv[2]
    if num_args == 2:
        print("Hello user, good job, you provided two arguments!")
    else:
        print(f"This script requires exactly two arguments. You provided {num_args} arguments")

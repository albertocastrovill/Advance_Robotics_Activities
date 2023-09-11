# This code adds two numbers
# The two numbers to add come from a C++ program
import sys

def addNumbers():
    if len(sys.argv) != 3:
        print("This Python code addTwoNumbers.py requieres two numbers")
        sys.exit(1)

numA = float(sys.argv[1])
numB = float(sys.argv[2])
result = numA + numB
print(f"Sum of {numA} and {numB} is {result}")

if __name__ == "__main__":
    addNumbers()
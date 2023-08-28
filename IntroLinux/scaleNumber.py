import sys 

def scaleNumberBy10(number):
    scaledNumber = number *10
    return scaledNumber

if __name__ == "__main__":

        for line in sys.stdin:
            try:
                inputNumber = int(line.strip())
                scaledResult = scaleNumberBy10(inputNumber)
                print(f"The scaled number is : {scaledResult}")
            except ValueError:
                print("Invalid input.")            
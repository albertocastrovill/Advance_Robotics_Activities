import sys

def bubbleSort(arrayToSort):
    n = len(arrayToSort)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arrayToSort[j] > arrayToSort[j+1]:
                arrayToSort[j], arrayToSort[j+1] = arrayToSort[j+1], arrayToSort[j]

if __name__ == "__main__":

    # Read input from stdin
    inputStrData = sys.stdin.read().strip()
    # Print input vector with the unsorted integers
    print(inputStrData)
    # Remove the bracket format in which the string of integers is read
    inputStrData = inputStrData.strip('[]')
    # Convert input Data to an array of integers
    #arrayOfIntegers = list(map(int, inputStrData.split()))
    inputData = [int(num) for num in inputStrData.split(',')]
    # Call the Bubble sort and print the result
    bubbleSort(inputData)
    print(inputData)



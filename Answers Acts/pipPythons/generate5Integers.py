import random

def createIntegerArray(size):
    return [random.randint(1,20)for _ in range(size)]

if __name__ == "__main__":
    randomArray = createIntegerArray(5)
    print(randomArray)
    
import subprocess

def main():

    subprocess.run(["gcc", "square_2nd_way.c", "-o", "squareFunction"])

    num = float(input("Enter a number: "))

    result = subprocess.run(["./squareFunction"], input=str(num), text=True, capture_output=True)

    print(result.stdout)

if __name__ == "__main__":
    main()
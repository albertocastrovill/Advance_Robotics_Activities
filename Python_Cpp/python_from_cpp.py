import subprocess

def main():

    #Compile the C++ program
    cppCompileCommands = ["g++", "main.cpp", "-o", "main"]
    subprocess.run(cppCompileCommands, check=True)

    #Call the compiled C++ file & let C++ do the rest
    cppExecuteCommand = ["./main"]
    result = subprocess.run(cppExecuteCommand, check=True)

if __name__ == "__main__":
    main()

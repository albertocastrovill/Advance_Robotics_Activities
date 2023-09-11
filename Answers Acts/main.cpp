// Use input/output stream library
#include <iostream>
// Use stringstream library for string convertions
#include <sstream>
// Use string library to manipulate strings
#include <string>
// Use cstdlib library for the system function
#include <cstdlib>
// Use cstdio library for standard input/output operations
#include <cstdio>

int main(){
    // Set the value of the numbers
    double numA = 5.0;
    double numB = 8.0;

    // Convert these numbers into strgins
    std::ostringstream os1, os2; // declare two string objects
    os1 << numA;                 // convert numA to string   
    os2 << numB;                 // convert numB to string
    std::string numAStr = os1.str(); // Get string representation on numA
    std::string numBStr = os2.str(); // Get string representation on numB

    // Now, set the command to call the Python script
    // Construct a command string to call the Python script with both numbers
    // NOTE: You may have both program files (.cpp & .py) in the same folder.
    // In my case, I have the .py file in a separated folder; so I need to set
    // this command with the correct path to the .py file
    std::string command = "python3 /home/gil/Python101/cppCallsPy/addTwoNumbers.py " + numAStr + " " + numBStr;

    // Execute the call to Python from C++
    int ret = system(command.c_str());

    // GOOD PRACTICE
    // Check if the Python script was executed correctly
    if (ret == 0){
        std::cout << "Python script ran as expected." << std::endl;
    }else{
        std::cout << "Error Python executing the Python script." << std::endl;
    }

    return 0;
}
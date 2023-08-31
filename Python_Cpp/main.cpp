#include <iostream>

int main(){
    int num1, num2;

    std::cout << "You need to enter two integer number\n";
    std::cout <<"Type the first value: ";
    std::cin >> num1;
    std::cout << "Type the second value: ";
    std::cin >> num2;

    int result = num1 + num2;

    std::cout << "Adding " << num1 << " and " << num2 << " gives: " << result << std::endl;

    return 0;
}
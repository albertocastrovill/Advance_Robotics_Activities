#include <iostream>
#include "product.h"

int main() {
    int a, b;
    std::cout << "Enter two integers: ";
    std::cin >> a >> b;
    
    int product = multiply(a, b);
    
    std::cout << "Product: " << product << std::endl;
    return 0;
}

#include <stdio.h>

int main(){

    double num;
    printf("Enter a number: ");
    scanf("%lf", &num);

    double square = num*num;
    printf("Square of %.2lf is %.2lf\n",num,square);

    return 0;

}

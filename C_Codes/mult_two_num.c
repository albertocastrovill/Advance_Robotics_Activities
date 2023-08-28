#include <stdio.h>


int main(){
    float n_a = 2;
    float n_b = 4;
    float result = n_a * n_b;

    // Case 1 : With operator 
    printf("Case 1 : With operator ");
    printf("\nAdding %0.4f times %0.4f equals %0.4f\n", n_a, n_b, result);

    // Case 2 : With imported fuction
    //printf("\nCase 2 : With imported fuction");
    //printf("\nAdding %0.4f times %0.4f equals %0.4f\n", n_a, n_b, productOperation(n_a,n_b));

    return 0;
}

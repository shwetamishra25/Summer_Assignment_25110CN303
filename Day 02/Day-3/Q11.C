//program to find gcd of two numbers
#include <stdio.h>

int main() {
    int a, b, gcd;

    printf("Enter two numbers: ");
    scanf("%d %d", &a, &b);

    for (gcd = (a < b ? a : b); gcd >= 1; gcd--) {
        if (a % gcd == 0 && b % gcd == 0) {
            printf("GCD = %d", gcd);
            break;
        }
    }

    return 0;
}
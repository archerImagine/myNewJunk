#include <stdio.h>
/*
 * Modify the temperature convesion program to print
 * the table in reverse order.
 */

int main(int argc, const char *argv[])
{
    int fahr,celsius;
    int lower,upper,step;

    lower = 0;          //Lower limit of temeprature table
    upper = 300;        //Upper Limit
    step = 20;          //Step Size
    printf("fahr \t celsius\n");
    fahr = upper;
    while (fahr >= lower) {
        celsius = (5 * (fahr - 32)) / 9;
        printf("%3d \t %6d\n",fahr,celsius);
        fahr = fahr - step;
    }
    return 0;
}


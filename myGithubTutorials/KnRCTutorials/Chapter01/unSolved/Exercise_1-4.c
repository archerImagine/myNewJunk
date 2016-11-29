#include <stdio.h>
/*
 * Write a program to print the corresponding Celsius to Fahrenheit table
 * */
int main(int argc, const char *argv[])
{
    float fahr,celsius;
    int lower,upper,step;

    lower = 0;      //Lower limit of temperature table
    upper = 300;    //Upper Limit
    step = 20;

    celsius = lower;
    while (celsius <= upper) {
       fahr = ((9.0 * celsius) /5.0) +32.0;
       printf("%3.0f\t%6.1f\n",celsius,fahr);
       celsius = celsius + step;
    }
    return 0;
}

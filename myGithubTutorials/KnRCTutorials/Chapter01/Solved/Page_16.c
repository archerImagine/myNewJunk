#include <stdio.h>
/*
 * Copy input to output: 1st Version
 */
int main(int argc, const char *argv[])
{
    int c;

    c = getchar();
    while (c != EOF) {
        putchar(c);
        c = getchar();
    }
    return 0;
}

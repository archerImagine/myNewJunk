#include <stdio.h>
/*
 * Copy input to output: 2st Version
 */
int main(int argc, const char *argv[])
{
    int c;

    while ((c = getchar() )!= EOF) {
        putchar(c);
        printf("\n");
        c = getchar();
    }
    return 0;
}

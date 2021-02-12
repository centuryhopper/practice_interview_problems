#include <stdio.h>

#define null NULL

typedef struct Hello
{
    int hithere;
}Hello;

int main(int argc, char const *argv[])
{
    Hello* hi = null;
    if (hi == null) {printf("null\n");return 0;}
    hi->hithere = 5;
    int a[] = {1,2,3};
    printf("%d\n", a[2]);

    printf("Hello\n");

    return 0;
}

#define null NULL
#include <string.h>
#include <stdio.h>
#include <stdlib.h>

int strStr(char * haystack, char * needle)
{
    int l = strlen(needle), len = strlen(haystack);
    printf("%d, %d\n",l,len);
    
    if (needle == null || l == 0) return 0;
    
    int i;
    for (i = 0; i < len-l+1;++i)
    {
        char *str = malloc(sizeof(char) * (l+1));
        str[l] = '\0';
        strncpy(str, haystack+i,l);
        if (strcmp(str,needle) == 0)
        {
            free(str);
            return i;
        }
        free(str);
    }
    
    
    return -1;
}
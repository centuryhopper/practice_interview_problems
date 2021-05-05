#include "../templates/template.h"

bool get_flag(uintptr_t p)
{
    return p & 1;
}

void *get_pointer(uintptr_t p)
{
    return (void *)(p & (UINTPTR_MAX ^ 1));
}

uintptr_t set_flag(uintptr_t p, bool value)
{
    return (p & (UINTPTR_MAX ^ 1)) | value;
}



int main()
{
    return 0;
}
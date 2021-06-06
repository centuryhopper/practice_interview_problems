#include <cstdio>
#include <cstdlib>
#include <numeric>
#include <iostream>
#include <cstring>
#define null NULL

using namespace std;

struct node
{
    int data;
    struct node *next;
};

struct Stack
{
    int *array;
    // current number of elements in the stack
    int top;
    // current max number of elements this stack is allowed contain
    int capacity;
};

void growStack(struct Stack *s, int increase)
{
    // Calculates new size as an increase to current capacity
    // 1 point
    int new_size = s->capacity + increase;

    // Has a mechanism to prevent “losing” the current array pointer
    // 2 points
    int *hold = s->array;

    // Allocates space for the increased stack array
    // 2 points
    s->array = (int *)malloc(sizeof(int) * new_size);

    int i;
    // Copies values from old array to new array
    // 3 points
    for (i = 0; i < s->top; i++)
        s->array[i] = hold[i];

    // Cleans up old memory space
    // 1 point
    free(hold);

    // Updates capacity
    // 1 point
    s->capacity = new_size;
}

Stack *create_stack(int capacity = 5)
{
    Stack *s = (Stack *)malloc(sizeof(Stack));
    s->top = 0;
    s->capacity = capacity;
    s->array = (int *)malloc(sizeof(int) * capacity);
    return s;
}

void fill_stack(Stack *s, int startNum = 0)
{
    // update size
    s->top = s->capacity;
    std::iota(s->array, s->array + s->capacity, startNum);
}

void printStack(Stack *s)
{
    for (int i = 0; i < s->top; ++i)
        cout << s->array[i] << " ";
    cout << "\n";
}

void destroyStack(Stack *s)
{
    free(s->array);
    free(s);
}

void studentGrowStack(struct Stack *s, int increase)
{
    // int *new_location = (int *) calloc(s->capacity + increase, sizeof(int) * s->capacity);
    // memcpy(new_location, s->array, sizeof(int) * s->capacity);
    // free(s->array);
    // s->array = new_location;

    int *temparray = (int *)malloc(sizeof(int) * (s->capacity + increase));

    for (int i = 0; i < s->top; i++)
    {
        temparray[i] = s->array[i];
    }

    s->capacity += increase;
    free(s->array);
    s->array = temparray;
}

int main(int argc, char const *argv[])
{
    std::cout << std::boolalpha << std::endl;

    // create a stack of size 5 containing elements 0-4
    Stack *s = create_stack();
    fill_stack(s, 0);
    printStack(s);
    int increase = 5;

    // TEST
    studentGrowStack(s, increase);

    // capacity check
    cout << (s->capacity == s->top + increase) << endl;

    // array contents check
    printStack(s);

    destroyStack(s);

    return 0;
}

/*
    if (s == NULL) // small chance to be a free 2 points, probably not since function return void..
        return;
    int new_size = s->capacity + increase;
    int *new_array = (int *)malloc(new_size * sizeof(int));
    if (s->array != NULL)
    {                                        // don’t crash on a stack with no capacity
        memcpy(new_array, s->array, sizeof(int) * s->top); // could copy s->capacity, a waste though
        free(s->array);
        puts("here");
    }
    s->capacity = new_size;
    s->array = new_array;
*/
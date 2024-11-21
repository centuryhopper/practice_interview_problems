
#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>

typedef struct {
  int n;
  int shouldRun;
} FooBar;

FooBar *fooBarCreate(int n) {
  FooBar *obj = (FooBar *)malloc(sizeof(FooBar));
  obj->n = n;
  obj->shouldRun = 1;
  return obj;
}

void foo(FooBar *obj) {

  int i = 0;
  while (i < obj->n) {
    // printFoo() outputs "foo". Do not change or remove this line.
    if (obj->shouldRun) {
      printFoo();
      obj->shouldRun = 0;
      i++;
    }
  }
}

void bar(FooBar *obj) {

  int i = 0;
  while (i < obj->n) {
    // printBar() outputs "bar". Do not change or remove this line.
    if (!obj->shouldRun) {
      printBar();
      obj->shouldRun = 1;
      i++;
    }
  }
}

void fooBarFree(FooBar *obj) { free(obj); }

#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/*
 https://leetcode.com/problems/rotate-string/
 */

char *rotateAction(char *str) {
  int len = strlen(str);
  // make sure string is not null or empty
  if (str == NULL || len == 0) {
    return NULL;
  }
  // account for null terminator
  char *dest = (char *)malloc(sizeof(char) * (len + 1));
  dest[len] = '\0';
  // copy str[1:] into dest
  memcpy(dest, &str[1], len - 1);
  // append first character of str to dest
  dest[len - 1] = str[0];

  return dest;
}

bool rotateString(char *s, char *goal) {
  if (strlen(s) != strlen(goal)) {
    return 0;
  }
  if (strcmp(s, goal) == 0) {
    return 1;
  }
  int len = strlen(s);
  // account for null terminator
  char *tmp = (char *)malloc(sizeof(char) * (len + 1));
  tmp[len] = '\0';

  strcpy(tmp, s);

  for (int i = 1; i < len; i++) {
    char *rotated = rotateAction(tmp);
    // printf("%s\n", rotated);
    if (strcmp(rotated, goal) == 0) {
      free(rotated);
      free(tmp);
      return 1;
    }
    strcpy(tmp, rotated);
    free(rotated);
  }

  free(tmp);

  return 0;
}
int main(void) {
  bool ans = rotateString("abcde", "cdeab");
  printf("ans: %d\n", ans);

  return EXIT_SUCCESS;
}

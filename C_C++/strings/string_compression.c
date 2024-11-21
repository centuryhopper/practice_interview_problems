#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char *compressedString(char *word) {
  int n = strlen(word);
  int cntArray[n];
  memset(cntArray, 0, sizeof(int));
  cntArray[0] = 1;
  // worst case string is if you repeat a string a-z enough times to hit the max
  // allowed word length of this problem, so then it would be 1a1b1c...1z
  // repeated so
  char *retVal = (char *)malloc(sizeof(char) * ((n * 2) + 1));
  retVal[2 * n] = 0;
  int returnSize = 0;
  // should be reset every 9 times
  int allowedCnt = 1;
  for (int i = 1; i < n; i++) {
    if (word[i] == word[i - 1] && allowedCnt < 9) {
      allowedCnt += 1;
      cntArray[i] = cntArray[i - 1] + 1;
    } else {
      allowedCnt = 1;
      cntArray[i] = 1;
      retVal[returnSize++] = cntArray[i - 1] + '0';
      retVal[returnSize++] = word[i - 1];
    }
  }

  // Add the last sequence count and character
  retVal[returnSize++] = cntArray[n - 1] + '0';
  retVal[returnSize++] = word[n - 1];

  // Null terminate the string
  retVal[returnSize] = '\0';

  // Resize retVal to the actual used space
  retVal = (char *)realloc(retVal, sizeof(char) * (returnSize + 1));

  // for(int i = 0;i<n;i++)
  // {
  //     printf("%d ", cntArray[i]);
  // }

  printf("\n");

  return retVal;
}

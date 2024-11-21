/**
 * Note: The returned array must be malloced, assume caller calls free().
 */

/*

[bella],
[label],
[roller],

[abcdefghijklmonpqrstuvwxyz],
[abcdefghijklmonpqrstuvwxyz],
[abcdefghijklmonpqrstuvwxyz],


[11001000000200000000000000], // first row of cnterarray
[11001000000200000000000000], // second row of cnterarray
[00001000000200000000000000], // third row of cnterarray

each row starting at the second row will take the minimum value of either itself
or the previous row's value

We take the minimum because the returned array of strings is constrained by the
word with the least number of character occurrences. For example, r may appear
twice in 'roller' but r appears 0 times in the other two words so the overall
sum for r at index r - 'a' is 0


https://leetcode.com/problems/find-common-characters/submissions/1442050428/

*/

#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char **buildReturnLst(char **words) {
  char **returnLst = (char **)malloc(sizeof(char *) * 100);
  for (int i = 0; i < 100; i++) {
    returnLst[i] = (char *)malloc(sizeof(char) * (1 + 1));
    returnLst[i][1] = '\0';
  }

  return returnLst;
}

void printStringArray(char **words) {
  for (int i = 0; i < 100; i++) {
    printf("%c ", words[i][0]);
  }
  printf("\n");
}

// dynamic programming approach
char **commonChars(char **words, int wordsSize, int *returnSize) {
  char **returnLst = buildReturnLst(words);
  *returnSize = 0;
  // printf("%d\n", wordsSize);
  // printf("%d\n", *returnSize);
  // printf("%d\n", sizeof(returnLst) / sizeof(char**));

  int seen[26] = {0};
  int cnterArray[26] = {0};
  // for(int i=0;i<26;i++)
  //     printf("%d ",seen[i]);

  for (int i = 0; i < wordsSize; i++) {
    for (int j = 0; words[i][j] != '\0'; j++) {
      int idx = words[i][j] - 'a';
      cnterArray[idx] += 1;
    }

    // fill seen array accordingly for the second array and onwards
    if (i > 0) {
      for (char ch = 'a'; ch <= 'z'; ch++) {
        // take the minimum
        seen[ch - 'a'] = seen[ch - 'a'] < cnterArray[ch - 'a']
                             ? seen[ch - 'a']
                             : cnterArray[ch - 'a'];
      }
    } else {
      for (int x = 0; x < 26; x++) {
        seen[x] = cnterArray[x];
      }
    }

    // reset cnterArray
    memset(cnterArray, 0, sizeof(cnterArray));
  }

  // for(int i=0;i<26;i++)
  //     printf("%d ",seen[i]);

  for (int i = 0; i < 26; i++) {
    while (seen[i]-- > 0) {
      returnLst[(*returnSize)++][0] = i + 'a';
    }
  }

  // printStringArray(returnLst);

  return returnLst;
}

// Time: O(m * n) where m is the number of words and n is the length of the
// longest word

// Space: O(26) since we know the input is constrained to lowercase english
// letters

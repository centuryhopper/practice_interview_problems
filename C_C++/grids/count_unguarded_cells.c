
static void markGuardedCells(char **array2D, int m, int n, int guardX,
                             int guardY) {
  // up
  for (int i = guardX - 1; i >= 0; i--) {
    // stop immediately if hit a wall or another guard
    if (array2D[i][guardY] == 'w' || array2D[i][guardY] == 'g') {
      break;
    }
    array2D[i][guardY] = 'u';
  }

  // down
  for (int i = guardX + 1; i < m; i++) {
    // stop immediately if hit a wall or another guard
    if (array2D[i][guardY] == 'w' || array2D[i][guardY] == 'g') {
      break;
    }
    array2D[i][guardY] = 'u';
  }

  // left
  for (int i = guardY - 1; i >= 0; i--) {
    // stop immediately if hit a wall or another guard
    if (array2D[guardX][i] == 'w' || array2D[guardX][i] == 'g') {
      break;
    }
    array2D[guardX][i] = 'u';
  }

  // right
  for (int i = guardY + 1; i < n; i++) {
    // stop immediately if hit a wall or another guard
    if (array2D[guardX][i] == 'w' || array2D[guardX][i] == 'g') {
      break;
    }
    array2D[guardX][i] = 'u';
  }
}

int countUnguarded(int m, int n, int **guards, int guardsSize,
                   int *guardsColSize, int **walls, int wallsSize,
                   int *wallsColSize) {
  // represents the whole prison
  // s for safe, u for unsafe
  // g for guard, w for wall
  char **array2D = (char **)malloc(sizeof(char *) * m);
  for (int i = 0; i < m; i++) {
    array2D[i] = (char *)malloc(sizeof(char) * n);
    memset(array2D[i], 's', n);
  }

  for (int i = 0; i < guardsSize; i++) {
    int guardX = guards[i][0];
    int guardY = guards[i][1];
    array2D[guardX][guardY] = 'g';
  }

  for (int i = 0; i < wallsSize; i++) {
    int wallsX = walls[i][0];
    int wallsY = walls[i][1];
    array2D[wallsX][wallsY] = 'w';
  }

  // go thru each guard and look in all four directions
  for (int i = 0; i < guardsSize; i++) {
    int guardX = guards[i][0];
    int guardY = guards[i][1];
    markGuardedCells(array2D, m, n, guardX, guardY);
  }

  // for (int i = 0; i < m; i++)
  // {
  //     for (int j = 0; j < n; j++)
  //     {
  //         printf("%c ", array2D[i][j]);
  //     }
  //     printf("\n"); // Newline after each row
  // }

  int cnt = 0;
  for (int i = 0; i < m; i++) {
    for (int j = 0; j < n; j++) {
      if (array2D[i][j] == 's') {
        cnt += 1;
      }
      // printf("%c ", array2D[i][j]);
    }
    // printf("\n"); // Newline after each row
    free(array2D[i]);
  }

  free(array2D);

  return cnt;
}

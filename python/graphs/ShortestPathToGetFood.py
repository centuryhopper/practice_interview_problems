'''
Example 1 
Input: grid = 
[["X","X","X","X","X","X"],
["X","*","O","O","O","X"], 
["X","O","O","#","O","X"],
["X","X","X","X","X","X"]]
Output: 3
Explanation: It takes 3 steps to reach the food.

Example 2
Input: grid = 
[["X","X","X","X","X"],
["X","*","X","O","X"],
["X","O","X","#","X"],
["X","X","X","X","X"]]
Output: -1
Explanation: It is not possible to reach the food.

Example 3
Input: grid = 
[["X","X","X","X","X","X","X","X"],
["X","*","O","X","O","#","O","X"],
["X","O","O","X","O","O","X","X"],
["X","O","O","O","O","#","O","X"],
["X","X","X","X","X","X","X","X"]]
Output: 6
Explanation: There can be multiple food cells. It only takes 6 steps to reach the bottom food.


'''



def shortestPathToFood(grid) -> int:
  # Type Your Solution Here
  me = None
  m,n = len(grid),len(grid[0])
  seen = set()

  # find me
  for i in range(m):
    for j in range(n):
      cur = grid[i][j]
      if cur == '*':
        me = (i,j)

  
  def dfs(grid,i,j):
    # bounds check
    if i < 0 or i == m or j < 0 or j > n:
      return float('inf')
    if grid[i][j] == 'X':
      return float('inf')
    if grid[i][j] == '#':
      return 0
    if (i,j) in seen:
      return float('inf')
    seen.add((i,j))
    a = 1 + dfs(grid,i-1,j)
    seen.discard((i,j))

    seen.add((i,j))
    b = 1 + dfs(grid,i+1,j)
    seen.discard((i,j))

    seen.add((i,j))
    c = 1 + dfs(grid,i,j-1)
    seen.discard((i,j))

    seen.add((i,j))
    d = 1 + dfs(grid,i,j+1)
    seen.discard((i,j))
    
    
    return min(a,b,c,d)

  ans = dfs(grid, me[0],me[1])
  return -1 if ans == float('inf') else ans



if __name__ == '__main__':
  grid = [["X","X","X","X","X","X"],
["X","*","O","O","O","X"], 
["X","O","O","#","O","X"],
["X","X","X","X","X","X"]]
  print(f"The number of steps is { shortestPathToFood(grid) }.")

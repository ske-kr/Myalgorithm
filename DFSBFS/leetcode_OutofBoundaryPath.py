# DFS + Cache(dp)기법
# 단순 DFS로 구현하는것보다 훨씬 빠르다( leet code상에서는 DFS로만 구현하면 TLE)
# 여기서 dp를 적용해서 3-d array를 선언하지말고 2d어레이를 2개단위로 저장해서 갱신하면
# space cost를 줄일수있음

def findPaths(self, m: int, n: int, N: int, i: int, j: int) -> int:
        def dfs(i, j, m, n, N, mem):
            if N < 0: return 0
            if i < 0 or i >= m or j < 0 or j >= n: return 1
            if mem[i][j][N] is not None: return mem[i][j][N]
            count = 0
            for x, y in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                count += dfs(x, y, m, n, N-1, mem)
            mem[i][j][N] = count
            return count % (10 ** 9 + 7)
            
        mem = [[[None]*(N+1) for _ in range(n)] for _ in range(m)]
        return dfs(i, j, m, n, N, mem)


# JAVA버젼이긴 하지만 space cost 를 줄인 기법

class Solution {
  public int findPaths(int m, int n, int N, int x, int y) {
    int M = 1000000000 + 7;
    int dp[][] = new int[m][n];
    dp[x][y] = 1;
    int count = 0;
    for (int moves = 1; moves <= N; moves++) {
      int[][] temp = new int[m][n];
      for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
          if (i == m - 1) count = (count + dp[i][j]) % M;
          if (j == n - 1) count = (count + dp[i][j]) % M;
          if (i == 0) count = (count + dp[i][j]) % M;
          if (j == 0) count = (count + dp[i][j]) % M;
          temp[i][j] = (
              ((i > 0 ? dp[i - 1][j] : 0) + (i < m - 1 ? dp[i + 1][j] : 0)) % M +
              ((j > 0 ? dp[i][j - 1] : 0) + (j < n - 1 ? dp[i][j + 1] : 0)) % M
          ) % M;
        }
      }
      dp = temp;
    }
    return count;
  }
}
class Solution:
    def minPathSum(self, grid):
        '''
        My first attempt for this problem was using dfs -> 2^n complexitiy pretty bad
        My second attempt was using djkstra -> which is also 2^n complexity pretty bad
        My third attempt was using A* which was quicker but also technically had a worst case 2^n complexity

        The best solution is DP based ofc, goddamn DP. All the approaches above had a similar issue where I was doing
        a lot of recomputation of best paths. Best path from node A = min(best path from node left of A, bets path from node below A)

        If we memoize this the final answer would be so easy
        '''
        ROWS, COLS = len(grid)+1, len(grid[0])+1
        dists = [[float("inf")]*COLS for r in range(ROWS)]
        dists[ROWS-2][COLS-1] = 0

        for i in range(ROWS-2,-1,-1):
            for j in range(COLS-2,-1,-1):
                dists[i][j] = grid[i][j] + min(dists[i+1][j],dists[i][j+1])
        return dists[0][0]

    
s = Solution()
print(s.minPathSum([[1,3,1],[1,5,1],[4,2,1]]))

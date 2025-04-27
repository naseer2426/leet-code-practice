class Solution(object):
    def shortestDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        '''
        I iterate through every empty cell and use dfs to find the shortest distance to each building in a map
        Then I sum this map and find min total. Even though this should be O(M^2*N^2), this solution is not accepted by
        leetcode and it gives me time limit exceeded.

        The best solution involves bfs from each building instead of each empty cell to find the total distance to each
        cell from each building, we can maintain this in a common map for all building building iteration. A new building
        iteration will simply add distance in a specific cell

        In addition to this we need to keep track how many buildings can reach each cell.

        I am not implementing this solution due to lack of time, just noting it down
        ''' 
        building_idxs = []
        for row_idx in range(len(grid)):
            for col_idx in range(len(grid[row_idx])):
                if grid[row_idx][col_idx] != 1:
                    continue
                building_idxs.append((row_idx,col_idx))
        
        min_dist = 1e7
        for row_idx in range(len(grid)):
            for col_idx in range(len(grid[row_idx])):
                if grid[row_idx][col_idx] != 0:
                    continue
                reached = {}
                building_min_dist = {}
                for b_idx in building_idxs:
                    building_min_dist[str((b_idx[0],b_idx[1]))] = 1e7
                self.bfs(building_min_dist,(row_idx,col_idx),reached,grid)
                total = 0
                for building in building_min_dist:
                    if building_min_dist[building] == 1e7:
                        total = 0
                        break
                    total+=building_min_dist[building]
                if total < min_dist and total > 0:
                    min_dist = total
        return -1 if min_dist == 1e7 else min_dist
    
    def bfs(self, building_min_dist, home_idx, reached, grid):
        queue = [(home_idx,0)]
        while len(queue)!=0:
            curr_cell,curr_steps = queue.pop(0)
            if grid[curr_cell[0]][curr_cell[1]] == 1:
                building_min_dist[str((curr_cell[0],curr_cell[1]))] = curr_steps
            all_possible_moves = self.all_possible_moves(curr_cell,grid)
            for new_cell in all_possible_moves:
                if str((new_cell[0],new_cell[1])) in reached:
                    continue
                queue.append((new_cell,curr_steps+1))
                reached[str((new_cell[0],new_cell[1]))] = True

    def all_possible_moves(self, curr_cell,grid):
        if grid[curr_cell[0]][curr_cell[1]] == 1 or grid[curr_cell[0]][curr_cell[1]] == 2:
            return []
        moves = []
        up = (curr_cell[0]-1,curr_cell[1])
        down = (curr_cell[0]+1,curr_cell[1])
        left = (curr_cell[0],curr_cell[1]-1)
        right = (curr_cell[0],curr_cell[1]+1)
        if self.is_cell_valid_to_move(up,grid):
            moves.append(up)
        if self.is_cell_valid_to_move(down,grid):
            moves.append(down)
        if self.is_cell_valid_to_move(left,grid):
            moves.append(left)
        if self.is_cell_valid_to_move(right,grid):
            moves.append(right)   
        return moves
    
    def is_cell_valid_to_move(self,cell,grid):
        if cell[0] > len(grid)-1 or cell[0]<0:
            return False
        if cell[1] > len(grid[cell[0]]) - 1 or cell[1] < 0:
            return False
        if grid[cell[0]][cell[1]] == 2:
            return False
        return True

s = Solution()
print(s.shortestDistance([[2,0,0,2,2,0,0,0,2,2,2,2,2,0,0,0,0,0,2,1,2,0,2,2,0,0,2,0,2,0,1,2,0],[0,2,2,0,1,0,0,0,0,0,0,0,2,2,2,2,2,2,2,0,0,0,0,2,0,2,2,1,0,0,0,0,0],[0,0,1,0,0,2,2,0,0,0,0,0,2,2,0,0,0,2,2,2,2,0,0,2,2,1,0,0,0,2,0,0,0],[0,0,0,0,0,0,0,2,0,0,0,0,2,1,0,0,0,0,2,2,0,0,2,0,2,1,0,0,2,0,0,0,2],[2,0,0,2,2,0,0,2,0,1,0,0,2,0,0,0,0,0,2,2,0,2,2,0,2,0,2,0,0,0,2,0,0],[0,0,2,0,0,0,0,0,0,0,0,1,2,2,0,0,0,2,0,0,0,0,0,2,2,2,2,0,2,0,0,0,0],[0,2,0,0,0,2,0,2,0,0,1,0,2,0,2,2,2,0,1,0,0,0,0,2,1,2,0,2,0,2,0,0,0],[2,1,0,0,0,0,0,0,0,0,0,0,2,1,2,2,0,0,0,0,0,2,0,0,0,0,2,2,0,2,2,0,0],[0,2,2,2,2,0,0,0,2,0,0,2,2,0,0,2,2,2,0,2,0,0,0,2,0,0,0,0,2,2,0,2,0],[0,0,0,0,1,0,0,2,2,0,0,0,0,0,2,2,0,0,0,0,2,2,0,2,2,0,0,0,0,2,2,2,0],[0,0,0,0,2,0,2,0,0,1,0,0,1,0,0,0,0,2,2,0,0,2,0,2,2,2,0,0,0,0,0,0,2],[0,0,0,2,2,0,0,2,0,0,0,2,0,0,0,0,1,1,2,0,0,2,2,0,0,0,0,0,0,0,1,0,0],[0,0,2,0,0,0,0,2,0,2,0,0,2,0,2,2,0,2,0,0,2,0,0,0,0,0,2,0,0,2,2,2,2],[0,0,0,1,0,0,0,2,0,0,0,0,2,2,0,1,2,1,0,0,0,0,2,0,2,0,0,2,0,2,0,0,2],[2,0,0,2,2,0,0,2,0,0,0,0,2,0,0,0,2,0,0,0,0,0,2,0,1,0,2,2,2,2,0,2,2],[0,2,0,0,0,0,2,0,0,2,0,0,2,2,2,0,0,2,0,2,2,2,2,0,2,2,2,2,0,0,2,0,0],[0,2,0,0,1,0,0,0,0,0,2,0,2,0,0,0,0,0,2,2,0,2,0,0,0,2,2,2,0,2,0,1,2],[1,0,0,0,0,2,2,1,1,0,0,0,0,0,0,0,0,0,0,2,0,2,0,1,0,2,0,2,2,2,2,0,0],[2,2,2,2,0,2,0,0,2,0,0,1,0,0,0,0,0,0,2,0,2,0,1,0,0,0,1,0,0,2,0,2,0],[0,0,2,0,0,0,1,2,1,2,0,0,0,0,2,2,0,0,0,0,0,0,2,0,0,2,2,2,2,0,0,2,0],[2,2,2,2,0,0,0,2,2,2,2,0,0,2,2,2,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0],[2,1,0,2,0,0,0,2,0,0,0,0,0,0,0,0,1,0,0,0,2,2,0,0,0,0,2,0,0,0,2,2,0],[0,2,2,2,0,0,0,0,0,2,0,2,0,2,0,0,2,2,2,0,0,2,0,0,0,2,0,0,2,2,2,2,0],[2,0,0,1,0,1,0,0,2,0,2,2,0,0,1,0,0,0,2,0,2,2,0,0,2,0,2,0,2,0,0,0,0],[2,0,2,0,0,0,0,0,0,0,0,2,0,2,2,2,0,0,1,0,1,2,2,0,2,0,0,0,0,0,0,0,1],[0,0,2,0,0,0,2,0,1,0,0,2,0,0,0,0,0,2,0,0,0,0,2,2,0,0,0,0,0,0,2,2,0],[0,2,2,0,1,0,0,0,0,0,0,0,0,2,2,2,2,2,2,0,2,1,2,0,2,2,2,1,0,2,0,0,2],[1,0,0,0,0,2,0,0,0,0,0,2,0,1,0,0,2,0,2,2,0,0,0,0,0,0,2,2,2,0,2,2,0],[0,2,2,0,0,2,0,2,0,0,2,0,2,2,0,0,0,2,2,0,1,0,0,0,0,2,2,2,0,0,0,2,0],[0,0,2,0,0,0,0,0,2,2,2,2,0,0,0,2,2,2,0,2,0,0,0,1,2,2,0,2,2,0,0,0,2],[2,0,0,0,0,2,0,0,2,2,0,0,2,1,2,0,2,0,0,2,0,2,0,0,2,2,0,0,2,2,2,0,0],[0,0,2,1,0,1,0,2,0,0,0,0,2,0,0,0,0,0,0,0,2,2,2,2,2,0,0,0,2,1,0,2,2],[2,0,0,0,0,2,2,0,2,0,2,0,0,0,2,0,2,2,1,2,0,2,2,0,2,0,2,0,0,2,0,0,2],[0,2,0,2,0,0,1,2,2,0,0,0,0,0,0,0,2,0,2,0,0,0,1,0,0,0,1,1,2,0,0,2,2],[1,0,2,0,0,2,1,2,0,2,1,2,2,2,2,0,0,0,0,2,0,2,2,1,2,0,2,0,2,1,0,0,0],[2,0,2,2,2,0,0,0,2,0,2,0,2,2,0,0,2,0,2,0,2,0,0,0,2,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,2,0,2,2,0,0,2,2,2,2,0,2,2,2,0,0,2,2,0,0,2,2,0,0,0,2,2],[0,0,2,2,2,2,2,2,2,0,2,1,2,0,0,0,1,0,0,2,0,0,0,0,0,0,0,2,0,0,0,2,2],[0,2,0,0,2,0,2,0,2,2,0,0,0,0,1,2,0,2,0,0,2,2,2,2,2,0,2,0,2,2,1,0,0],[2,0,0,2,2,2,0,2,0,2,2,0,0,0,2,1,0,0,2,2,0,0,0,0,0,0,0,2,0,0,0,0,0]]))

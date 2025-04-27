'''
My initial attempt was both dfs and bfs using the actual coins array. This turned out to be not very optimal
because I was reprocessing a lot of total sums again. Instead of bfs/dfs on coins array, I can dfs on sum, with
a visited map so that I dont reprocess a sum. This method is pretty much identical to the DP approach where we have 
a memoized map of sum to min coins. 
'''

class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        
        queue  = [(0,0)]
        visited = {0:True}

        while len(queue) != 0:
            curr_amount,num_coins = queue.pop(0)
            if curr_amount == amount:
                return num_coins
            
            all_possible = self.all_possible_amounts(curr_amount,coins,amount)
            
            for next_amount in all_possible:
                if next_amount in visited:
                    continue
                visited[next_amount] = True
                queue.append((next_amount,num_coins+1))

        return -1
    
    def all_possible_amounts(self,curr_amount,coins,amount):
        
        all_possible_amounts = []
        for coin in coins:
            if curr_amount+coin > amount:
                continue
            all_possible_amounts.append(curr_amount+coin)
        return all_possible_amounts
        
s = Solution()
print(s.coinChange([186,419,83,408],6249))

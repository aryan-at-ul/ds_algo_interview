"""
Frog Jump Puzzle
A frog wants to cross a series of stones or steps. The frog starts at the first stone and wants to reach the nth stone. The frog can jump in specific ways:

The frog can jump one stone.
The frog can jump two stones.
The question is: In how many distinct ways can the frog reach the nth stone?
"""

"""
steps = [1, 2]

1st stone: 1 way (1), only 1 way to reach the first stone (from the ground)
2nd stone: 2 ways, 2 jump that is 1 + 1 or 1 jump of 2 steps, so total 2 ways to reach the second stone
3rd stone: 3 ways, do a 1 step 3 jumps, do a 1step jump and 2 step jump, or do a 2 step jump and then a 1 step jump.

4th stone: this will reveal the pattern, 1 step jumps (4 jumps), 2 step jumps (2 jumps of 2 steps), or a combination of 1 and 2 step jumps (in both order so 2 ways, 1,2 or 2,1).

1,2,3,5,.....<< this is fibonachi series

"""
import time


class FrogJump:

    def __init__(self, n):
        self.n = n
        self.memo = {}


    def count_ways_inefficient_way(self, n=None):
        """
        worst way to solve this is using recursion without memoization O(2^n)
        """

        if n is None:
            n = self.n

        if n <= 2:
            return n
        
        # the forumal is, at step n, f(n) = f(n-1) + f(n-2)
        return self.count_ways_inefficient_way(n -1) + self.count_ways_inefficient_way(n-2)
    

    def count_ways_memoization(self, n):
        """
        This is a better way to solve this problem using memoization O(n)
        """

        if n is None:
            n = self.n

        if n <= 2:
            return n
        
        #look up in the memo dictionary
        if n in self.memo:
            return self.memo[n]
        
        # the forumal is, at step n, f(n) = f(n-1) + f(n-2)
        self.memo[n] = self.count_ways_memoization(n -1) + self.count_ways_memoization(n-2)
        return self.memo[n]
    
    def count_ways_tabulation(self):
        """
        This is a better way to solve this problem using tabulation O(n): 1d DP 
        """

        if self.n <= 2:
            return self.n
        
        dp = [0] * (self.n + 1) # auxillary space to store all computed values
        dp[1] = 1 # base values that are know
        dp[2] = 2

        for i in range(3, self.n + 1):
            # same forumla f(n) = f(n-1) + f(n-2)
            dp[i] = dp[i-1] + dp[i-2]

        return dp[self.n]
    

    def count_ways_best(self):
        """
        No aurxilary space, 2 varaible to store base cases and return from there
        """

        a = 1
        b = 2 

        for i in range(3,self.n+1):
            c = a + b
            a = b
            b = c
        return b
    

if __name__ == '__main__':

    n = 40  # number of stones
    frog_jump = FrogJump(n)

    start_time = time.time()
    ways_inefficient = frog_jump.count_ways_inefficient_way(n)
    print(f"Ways to reach the {n}th stone (inefficient): {ways_inefficient}, Time taken: {time.time() - start_time:.6f} seconds")

    start_time = time.time()
    ways_memoization = frog_jump.count_ways_memoization(n)
    print(f"Ways to reach the {n}th stone (memoization): {ways_memoization}, Time taken: {time.time() - start_time:.6f} seconds")

    start_time = time.time()
    ways_tabulation = frog_jump.count_ways_tabulation()
    print(f"Ways to reach the {n}th stone (tabulation): {ways_tabulation}, Time taken: {time.time() - start_time:.6f} seconds")

    start_time = time.time()
    ways_best = frog_jump.count_ways_best()
    print(f"Ways to reach the {n}th stone (best): {ways_best}, Time taken: {time.time() - start_time:.6f} seconds")



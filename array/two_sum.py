"""
Leetcode Problem: Two Sum
Problem Statement:
Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
Example:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]

"""


class TwoSum:

    def __init__(self, nums, target):
        self.nums = nums
        self.target = target



    def dictionary_method(self):
        """
        this method iterates tought the list and maintains a dictionary taget - num : index, this is because diff = target - num will be constant for
        both the numbers that add up to target.
        """

        diff_index = {}

        for i, num in enumerate(self.nums):
            diff = self.target - num
            if diff in diff_index:
                return [diff_index[diff], i] # first index sores the first time diff was found, second index is the current index which hit the target
            
            diff_index[num] = i  # store the index of the current number

        return None 
    

    def brute_force(self):

        """
        O(n^2) brute force solution

        check each pair for taget
        """

        for i in range(len(self.nums)):
            for j in range(i+1, len(self.nums)):
                
                if self.nums[i] + self.nums[j] == self.target:
                    return [i, j]
                
            
        return None
    
    def sorted_method(self):
        """
        this method sorts the array and then uses two pointers to find the target.
        """

        sorted_nums = sorted((num, i) for i, num in enumerate(self.nums))
        print("Sorted nums with indices:", sorted_nums)
        start, end = 0 , len(sorted_nums) - 1
        while start < end: 
            current_sum = sorted_nums[start][0] + sorted_nums[end][0]
            if current_sum ==  self.target:
                return [sorted_nums[start][1], sorted_nums[end][1]]
            elif current_sum < self.target:
                start += 1
            else:
                end -= 1 
        
        return None



if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9
    two_sum = TwoSum(nums, target)
    result = two_sum.dictionary_method()
    print("Indices of the two numbers that add up to target:", result)  # Output: [0, 1]

    result = two_sum.brute_force()
    print("Indices of the two numbers that add up to target (brute force):", result)  # Output: [0, 1]

    result = two_sum.sorted_method()
    print("Indices of the two numbers that add up to target (sorted method):", result)  # Output: [0, 1]







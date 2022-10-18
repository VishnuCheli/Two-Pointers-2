#Time Complexity:: O(n^2*log(n))- 1 pointer fixed and other 2 does Binary Search
#Space Complexity:: O(c)-Custom sort used to sort array initially(in python we use tim sort)
#Did this code successfully run on Leetcode : Yes
#Any problem you faced while coding this : No
#tim sort uses auxillary space but if we did inplace, then O(1)

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        triplets = [] #result
        nums.sort() #sorting the numbers using tim sort
        
        for i in range(n-2): #i is the fixed pointer
            if i>0 and nums[i] == nums[i-1]:
                continue
            p1 = i + 1 #second pointer 
            p2 = n - 1 #third pointer
            target = 0 - nums[i] 
            
            while p1<p2: #stopping condition for iteration
                if (nums[p1] + nums[p2]) == target: #target is equal added values
                    res = [nums[i],nums[p1],nums[p2]] #largest value
                    triplets.append(res)
                    while p1<p2 and nums[p1] == nums[p1+1]: #incrementing p1
                        p1 += 1 
                    while p1<p2 and nums[p2] == nums[p2-1]: #decrementing p2
                        p2 -= 1
                    p1 += 1
                    p2 -= 1
                
                else: #target not equal to p1 + p2 values
                    if target < (nums[p1]+nums[p2]): #target is smaller  so decrease p2 to get closer to sum
                        p2 -= 1
                    
                    else:  #target is greater so  increase p1 to get closer to sum
                        p1 += 1 
            
        return triplets
        
        
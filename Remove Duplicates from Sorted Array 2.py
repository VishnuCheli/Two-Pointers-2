#Time Complexity:: O(n)- traversing through all elements in nums
#Space Complexity:: O(1)- no extra space allocated
#Did this code successfully run on Leetcode : Yes
#Any problem you faced while coding this : No

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        k=2 #number of duplicates allowed as we start with 1
        slow = 1
        count = 1 #starting with index 1
        for fast in range(1,len(nums)):
            if nums[fast] == nums[fast-1]:
                count += 1 #when duplicate detected increment count
            
            else:
                count = 1 #when not equal count is set to 1 again
                
            if count<=k:  #check if count is less than or equal 2
                nums[slow] = nums[fast]
                slow += 1
        return slow
        
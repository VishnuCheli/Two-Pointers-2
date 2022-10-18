#Time Complexity:: O(n)-traversing all the elements in the list nums
#Space Complexity:: O(1)-in-place operations only and no rtype
#Did this code successfully run on Leetcode : Yes
#Any problem you faced while coding this : No

class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        first = 0 
        zeroth = 0
        second = len(nums)-1
        
        while first<=second:
            if nums[first]==1: #for 1 keep the count
                first+=1
            elif nums[first]==0: #for 0 keep the count
                nums[first],nums[zeroth] = nums[zeroth],nums[first] #swap the zeroth and the first element when first pointer detects 0
                zeroth += 1 #
                first += 1
                
            else: #for 2 keep the count
                nums[first],nums[second] = nums[second],nums[first] #element from end of the list is copied to front when 2 is detected
                second -= 1
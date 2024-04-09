# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 22:31:02 2024

@author: Firas.Brinsi
"""

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums)>10**4 or len(nums)<=1:
            return 
        if target>10**9 or target<-10**9:
            return 
        else:
            for i in nums:
                if i>10**9 or i<-10**9:
                    return 
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i]+nums[j]==target and i!=j:
                    return (i,j)
#Test case                
#Solution().twoSum([3,3], 6)
#Solution().twoSum([3,2,4],6)


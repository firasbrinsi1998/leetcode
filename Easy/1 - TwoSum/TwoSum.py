# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 11:47:03 2024

@author: Firas.Brinsi
"""
"""
#Brute force solution  


class Solution:
    def twoSum(self, nums, target):
        if len(nums)>10**4 or len(nums)<=1:
            return 
        if target>10**9 or target<-10**9:
            return 
        else:
            for i in nums:
                if i>10**9 or i<-10**9:
                    return 
        
        numbers={}
        for i,number in enumerate(nums):
            numbers[number]=i
            a=target-number
            if a in numbers and (numbers[a]!=numbers[number]):
                return (numbers[a], numbers[number])
            else:
                numbers[number]=i
            
"""

#Optimized code through dictionary data struct

class Solution:
    def twoSum(self, nums: List[int], target:int) -> List[int]:
        dic=dict()
        for i, number in enumerate(nums):
            a=target-number
            if a in dic:
                return (i,dic[a])
            dic[number]=i
            
            
#Test case                
#print(Solution().twoSum([3,3], 6))
#print(Solution().twoSum([3,2,4],6))


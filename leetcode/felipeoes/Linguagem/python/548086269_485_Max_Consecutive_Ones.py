class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        for num in nums:
            if num == 1:
                count+=1
            elif num == 0:
                count = 0
                
        return count
        
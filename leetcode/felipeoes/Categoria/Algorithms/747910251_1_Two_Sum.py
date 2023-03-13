class Solution:
    
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        solutions = []
        visited = {}
        
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if nums[i] + nums[j] == target:
                    solutions.append(i)
                    solutions.append(j)
                    
                    return solutions
                
                visited[nums[i]] = True
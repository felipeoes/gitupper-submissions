class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        solutions = []
        visited = {}
        
        for i in range(len(nums)):
            for j in range(len(nums)):
                if not visited.get(nums[i]) and (nums[i] + nums[j] == target):
                    solutions.append(i)
                    solutions.append(j)
                    
                    return solutions
                
                visited[nums[i]] = True
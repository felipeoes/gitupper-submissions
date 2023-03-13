class Solution:
    
    def valid_sum(self, num1: int, num2: int, target: int):
        return num1 != num2 and (num1 + num2 == target)
    
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        solutions = []
        visited = {}
        
        for i in range(len(nums)):
            for j in range(len(nums)):
                if not visited.get(nums[i]) and self.valid_sum(nums[i], nums[j], target):
                    solutions.append(i)
                    solutions.append(j)
                    
                    return solutions
                
                visited[nums[i]] = True
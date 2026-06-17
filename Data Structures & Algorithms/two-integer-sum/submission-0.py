class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # array nums 
        # integer target 
        result = []
        for i, n in enumerate(nums):
            j = 0
            while j < len(nums)-1:
                if n + nums[j] == target:
                    result = [j, i]
                    break
                else:
                    j += 1
        return result


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for index, num  in enumerate(nums):
           x = target - num
           if x in nums:
                i = nums.index(x)
                j = index
        return [i, j]
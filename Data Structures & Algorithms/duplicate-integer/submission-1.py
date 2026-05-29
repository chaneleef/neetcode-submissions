class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        sorted_list = sorted(nums)
        for i in range(len(nums)-1):
            x = sorted_list[i]
            if x == sorted_list[i+1]:
                return True
        return False
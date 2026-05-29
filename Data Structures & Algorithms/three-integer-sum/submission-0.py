class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        for i in range(len(nums)-2):
            # first int is the smallest and if it is postive will not result in 0 
            if nums[i] > 0:
                break 
            if i > 0 and nums[i] == nums[i-1]:
                continue 
            
            l = i + 1
            r = len(nums)-1 
            while l < r: 
                x = nums[i] + nums[l] + nums[r]
                if x < 0:
                    l += 1
                elif x > 0:
                    r -= 1 
                else:
                    result.append([nums[i], nums[l], nums[r]])
                    #move pointers inward so you dont repeat 
                    l += 1 
                    r -= 1

                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1
        return result

        
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # input list 
        #output list 
        i = 0
        prod_lst = []
        while i < len(nums):
            result = 1 
            for j, x in enumerate(nums):
                if j == i:
                    continue 
                else:
                    result *= x 
            
            prod_lst.append(result)
            i += 1
        return prod_lst 
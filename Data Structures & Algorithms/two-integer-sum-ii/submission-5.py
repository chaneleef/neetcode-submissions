class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = 1
        result = []
        for i in range(len(numbers)):
            for j in range(i + 1, len(numbers)):
                x = numbers[i] + numbers[j]
                if x == target:
                    result = [i + 1, j + 1]
                    return result
            
        return result
            
            


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # input -> list, int -> k  
        # output list
         
        seen = {}
        result = []
        # iterate through list 
        for n in nums:
            # add the number as a key and count as value
            if n not in seen:
                seen[n] = 1
            else:
                seen[n] += 1 
            # if count matches k then add to list 

        # iterates over k 
        for i in range(k):
            m = 0 
            # finds max and removes it to find the next max 
            for s, v in seen.items():
                if v > m:
                    m = v
                    x = s
            result.append(x)
            seen.pop(x)
        return result
                
                
                
            

        return result


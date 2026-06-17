class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # input: list of strings 
        # output: list of lists of strings 

        seen = {}
        

        for s in strs:
            x = "".join(sorted(s))
            if x not in seen: 
                seen[x] = [s]
            else:
                seen[x].append(s)

        return list(seen.values())

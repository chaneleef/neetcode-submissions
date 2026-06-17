class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # input: list of strings 
        # output: list of lists of strings 

        seen = {}
        

        for s in strs:
            if "".join(sorted(s)) not in seen: 
                seen["".join(sorted(s))] = [s]
            else:
                seen["".join(sorted(s))].append(s)

        return list(seen.values())

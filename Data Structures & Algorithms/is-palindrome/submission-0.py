class Solution:
    def isPalindrome(self, s: str) -> bool:
        import re
        l = 0 
        
        
        cleaned_text = re.sub(r'[^A-Za-z0-9]', '', s)
        cleaned_text = cleaned_text.lower()
        r = len(cleaned_text)-1 

        while l < r:
            if cleaned_text[l] == cleaned_text[r]:   
                l += 1
                r -= 1
            else:
                return False 
        return True 
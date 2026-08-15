class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        pal= ''
        for ch in s:
            if ch.isalnum():
                pal += ch.lower()

        return pal == pal[::-1]

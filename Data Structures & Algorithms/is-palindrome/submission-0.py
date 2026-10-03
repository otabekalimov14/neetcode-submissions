class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = ""
        for c in s:
            if c.isalnum():
                clean += c
        if clean[::-1].lower() == clean.lower():
            return True
        else:
            return False
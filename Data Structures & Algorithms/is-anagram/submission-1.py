class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        w1 ={}
        w2 = {}
        for c in s:
            w1[c] = w1.get(c, 0) + 1
        for x in t:
            w2[x] = w2.get(x, 0) + 1
        
        if w1 == w2:
            return True
        else:
            return False
        
        
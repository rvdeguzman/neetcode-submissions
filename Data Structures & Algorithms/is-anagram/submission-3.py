class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        i = list(s) 
        j = list(t)
        i.sort()
        j.sort()
        if i != j:
            return False
        return True
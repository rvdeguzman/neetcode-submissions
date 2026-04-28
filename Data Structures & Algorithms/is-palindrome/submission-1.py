class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1 = ''.join(c for c in s if c.isalnum()).lower()
        print(s1)
        i = 0
        j = len(s1) - 1
        print(j)
        while i <= j:
            if (s1[i] != s1[j]):
                return False
            i += 1
            j -= 1
        return True
        
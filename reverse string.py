from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s[:] = s[::-1]
        print(s)


lst = list('hello12345')

a = Solution()
print(a.reverseString(lst))
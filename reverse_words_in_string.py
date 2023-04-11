from typing import List

class Solution:
    def reverseWords(self, s: str) -> str:
        """
        Do not return anything, modify s in-place instead.
        """
        splited = s.split(' ')
        a = ' '.join([el[::-1] for el in splited])
        return a

lst = "Let's take LeetCode contest"

a = Solution()
print(a.reverseWords(lst))
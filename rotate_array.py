from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(k):
            popped = nums.pop(-1)
            nums.insert(0, popped)
            print(nums)

lst = ['-','-','-','-','-','-','-','-',0]

a = Solution()
a.rotate(lst, 100)
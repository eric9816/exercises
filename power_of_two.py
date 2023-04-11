class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n and not (n & n - 1)
        # if n < 2:
        #     return True
        # return True if (n ** 0.5).is_integer() else False

obj = Solution()
print(obj.isPowerOfTwo(8))
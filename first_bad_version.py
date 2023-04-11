
class Solution:

    @staticmethod
    def isBadVersion(version: int) -> bool:
        return True if version >= 1702766719 else False

    # def firstBadVersion(self, n: int):
    #
    #     low_idx = 0
    #     high_idx = n
    #
    #     while low_idx < high_idx:
    #         mid_idx = round((low_idx + high_idx) / 2)
    #         if self.isBadVersion(mid_idx):
    #             high_idx = mid_idx
    #         else:
    #             low_idx = mid_idx + 1
    #
    #     return low_idx

    def firstBadVersion(self, n: int) -> int:
        low = 1
        high = n - 1
        while (low <= high):
            mid = low + (high - low) // 2
            if self.isBadVersion(mid):
                high = mid - 1
            else:
                low = mid + 1
        return low


            # if self.isBadVersion(guess):
            #     if not self.isBadVersion(before_guess):
            #         return before_guess
            #     elif guess > target:
            #         high_idx = mid_idx - 1
            # elif guess < target:
            #     low_idx = mid_idx + 1
        # return -1


a = Solution()
print(a.firstBadVersion(2126753390))

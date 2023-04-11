class Solution:
    def searchInsert(self, nums, target: int) -> int:

        low_idx = 0
        high_idx = len(nums) - 1

        while low_idx <= high_idx:
            mid_idx = round((low_idx + high_idx) / 2)
            guess = nums[mid_idx]

            if guess == target:
                return mid_idx
            elif guess > target:
                high_idx = mid_idx - 1
            elif guess < target:
                low_idx = mid_idx + 1


lst = sorted([-1,0,3,5,9,12])

a = Solution()
print(a.searchInsert(lst, 6))
def isBadVersion(version: int) -> bool:
    return True if version >= 5 else False

def find(n):
    left = 0
    right = n - 1
    while left <= right:
        mid = (left + right) // 2
        if isBadVersion(mid):
            right = mid - 1
        else:
            left = mid + 1

    return left

print(find(3))


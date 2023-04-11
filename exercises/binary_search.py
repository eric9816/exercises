
def binary_search(lst, target):
    left = 0
    right = len(lst) - 1
    while left <= right:
        mid_idx = (left + right) // 2
        if lst[mid_idx] == target:
            return mid_idx
        elif lst[mid_idx] > target:
            right = mid_idx - 1
        else:
            left = mid_idx + 1


lst = sorted([1,2,3,4,5,6,7,8,9])
print(binary_search(lst, 7))
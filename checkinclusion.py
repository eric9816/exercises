class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if s1 in s2:
            return True
        elif s1[::-1] in s2:
            return True
        else:
            s1_sorted = ''.join(sorted(s1))
            s2_sorted = ''.join(sorted(s2))
            if s1_sorted in s2_sorted:
                return True
            return False





obj = Solution()
print(obj.checkInclusion("ab", "eidboaoo"))

a = [5,0,2,3,-5,6,9]

def quicksort(lst):
    if len(lst) < 2:
        return lst
    else:
        pivot = lst[0]
        left = [i for i in lst[1:] if i <= pivot]
        right = [i for i in lst[1:] if i > pivot]
        return quicksort(left) + [pivot] + quicksort(right)

print(quicksort(a))


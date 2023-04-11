def twoSum(numbers, target: int):
    arr = numbers
    left, right = 0, len(arr) - 1

    while left < right:
        curr_sum = arr[left] + arr[right]
        if curr_sum == target:
            return [left + 1, right + 1]
        elif curr_sum < target:
            left += 1
        else:
            right -= 1

#print(twoSum([2,7,11,15,6,67,8], 17))


def scobes(scobes):
    stack = []
    for idx, scobe in enumerate(scobes):
        if scobe in '{[(':
            stack.append(scobe)
        else:
            if not stack:
                return 'Ошибка'

            top = stack.pop()

            if top == '{' and scobe == '}':
                continue
            if top == '[' and scobe == ']':
                continue
            if top == '(' and scobe == ')':
                continue

    if stack:
        return 'Ошибка'
    return 'Success'

print(scobes('[(())]'))



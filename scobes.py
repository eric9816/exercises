
# good_scobes = '{{}()}'
# bad_scobes = '{)()'

good_scobes = '[[]()]'
bad_scobes = '[)()'
scobes = '([](){([[]])})'
scobes = '(()'
def check_scobes(scobes):
    stack = []
    for idx, scobe in enumerate(scobes):
        if scobe in '{[(':
            stack.append(scobe)
        else:
            # Тут можем сразу завершить, если есть закрывающаяся, но нет открывающейся
            if not stack:
                return idx
            top = stack.pop()
            if (top == '[' and scobe == ']'):
                continue
            if (top == '(' and scobe == ')'):
                continue
            if (top == '{' and scobe == '}'):
                continue
            return idx
    return 'Success'


print(check_scobes(scobes))


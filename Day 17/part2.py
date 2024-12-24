goal = list(reversed([2, 4, 1, 5, 7, 5, 1, 6, 0, 3, 4, 2, 5, 5, 3, 0]))

def backtrack(A, i):
    if i == len(goal):
        return A
    
    A <<= 3
    for k in range(8):
        A += k
        if (A ^ 5 ^ 6 ^ (A >> ((A % 8) ^ 5))) % 8 == goal[i]:
            try: return backtrack(A, i + 1)
            except BaseException: pass
        A -= k
    A >>= 3

    raise BaseException

print(backtrack(0, 0))
def bin3_to_int(string):
    c = 0
    bits = reversed([string[x:x+3] for x in range(0, len(string), 3)])

    for i, bit in enumerate(bits):
        c += int(bit, 2) * (8 ** i)
    return c

goal = [1, 7, 2, 6, 4, 6, 2, 5, 3, 0, 7, 1, 6, 6, 0, 3] # (prog ^ 3 since 5^6 = 3)
base_8 = [format(i, '03b') for i in range(8)]

# We build A 3 bits at a time starting from the most significant since they reprensent the code's last digit
A = (["0"] * 9) + ["0" for _ in range(len(goal) * 3)]

# Rlly need to build A from the 3 leftmost digits and then bitshift 3 <<
def backtrack(A, i):
    if i < 0:
        print("Found")
        return A
    
    bit_goal = base_8[goal[i]]
    print(''.join(A))
    for bit in base_8: # 3 leftmost bits of A (excluding shift buffer)
        a = bin3_to_int(bit)
        A_index = 9 + (len(goal) - i - 1) * 3
        A_index_shift = a ^ 5
        bit_output = base_8[(a ^ (bin3_to_int(''.join(A[A_index - A_index_shift - 3 : A_index])))) % 8]
        if bit_output == bit_goal:
            end = backtrack(A[:9 + A_index] + [x for x in bit_goal] + A[9 + A_index + 3:], i - 1)
            if end != None:
                return end
            
    return None

print(backtrack(A, len(goal) - 1))

case1 = [2, 3, 1, 1, 4]
case2 = [2, 3, 0, 1, 4]





def jump_helper(index, lst, mem):
    end = (len(lst)-1)
    if index == end:
        return 0

    if mem[index] != -1:
        return mem[index]

    min_jumps = float("inf")

    for i in range(lst[index], 0, -1):
        if index + i <= end:
            min_jumps = min(min_jumps, 1 + jump(lst, index + i, mem))
    mem[index] = min_jumps
    return mem[index]

def jump(lst):
    memo = [-1 for x in range(len(lst))]
    jump_helper(0, lst, memo)
    return memo[0]





jump(case1)
jump(case2)

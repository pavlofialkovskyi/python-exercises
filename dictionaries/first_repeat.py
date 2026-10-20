def first_repeat(nums):
    d = {}
    rep = -1
    for n in nums:
        if n in d:
            rep = n
            break
        d[n] = 1
    return rep



print(first_repeat([2, 5, 1, 2, 3, 5]))   # 2
print(first_repeat([1, 2, 3]))            # -1
print(first_repeat([7, 7]))               # 7
print(first_repeat([]))                   # -1
print(first_repeat([5, 1, 5, 1]))         # 5
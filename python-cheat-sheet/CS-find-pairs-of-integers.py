


# def find_pairs(l, x):
#     pairs = []   
#     for (i, el_1) in enumerate(l):
#         for (j, el_2) in enumerate(l[i+1:]):
#             if el_1 + el_2 == x:
#                 pairs.append((el_1,el_2))
#     return pairs

def find_pairs(l, x):
    memo = {}
    pairs = []
    for i in l:
        if i not in memo:
            if x > i:
                memo[i] = x - i
            if x < i:
                memo[i] = i - x
    for i in memo:
        if memo[i] in l and i + memo[i] == x:
            return (i, memo[i])



list = [2,5,8,98,63,5,67,8]
print(find_pairs(list, 13))
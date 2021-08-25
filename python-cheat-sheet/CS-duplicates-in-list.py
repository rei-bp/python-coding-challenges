

intlist = [3, 4, 5, 6, 7, 8, 3, 9]


# def find_duplicates(list):
#     duplicates, seen = set(), set()
#     for i in list:
#         if i in seen:
#             duplicates.add(i)
#         seen.add(i)
#     return list(duplicates)



#with dictionary
def find_duplicates(list):
    memo = {}
    duplicates = []
    for i in list:
        if i not in memo:
            memo[i] = 1
        else:
            duplicates.append(i)
    return duplicates
            

        

print(find_duplicates(intlist))
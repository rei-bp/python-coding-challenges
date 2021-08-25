def get_missing_number(list):
    return set(range(1, list[len(list)-2]))-set(list)

l = list(range(1,100))
l.remove(50)
print(get_missing_number(l))
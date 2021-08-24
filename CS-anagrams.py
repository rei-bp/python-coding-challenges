str1 = 'elvis'
str2 = 'lives'



# def is_anagram(s1, s2):
#     print(set(s1), set(s2))
#     return set(s1) == set(s2)


#more accurate way with duplicate letters
def is_anagram(s1, s2):
    memo1 = {}
    memo2 = {}
    if len(s1) != len(s2):
        return False
    else:
        for i in s1:
            if i not in memo1:
                memo1[i] = 1
            else:
                memo1[i] += 1
        for i in s2:
            if i not in memo2:
                memo2[i] = 1
            else:
                memo1[i] += 1
    return True if memo1 == memo2 else False
            
            


print(is_anagram(str1, str2))
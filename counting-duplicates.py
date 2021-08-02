def duplicate_count(text):
    # Your code goes here
    memo = {}
    count = 0
    str = text.lower()
    for i in str:
        print(str)
        if i not in memo:
            memo[i] = 1
        elif memo[i] > 1:
            continue
        else:
            memo[i] += 1
    for i in memo:
        if memo[i] > 1:
            count += 1
    return count
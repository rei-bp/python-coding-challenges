def spin_words(sentence):
    # Your code goes here
    arr = sentence.split()
    str = []
    for i in arr:
        if len(i) < 5:
            str.append(i)
            print(str)
        elif len(i) >= 5:
            new = i[::-1]
            str.append(new)
    return ' '.join(str)
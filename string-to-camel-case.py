#covert string to comel case 

def to_camel_case(text):
    #your code here
    import re
    if text == '':
        return ''
    else:
        arr = re.split('-|_', text)
        newArr = []
        if text[0].islower():
            newArr.append(arr[0])
            for i in range(1, len(arr)):
                cap = (arr[i])[0].upper()
                rest = (arr[i])[1:]
                new = f'{cap}{rest}'
                newArr.append(new)
        else:
            for i in arr:
                cap = i[0].upper()
                rest = i[1:]
                new = f'{cap}{rest}'
                newArr.append(new)
        return ''.join(newArr)
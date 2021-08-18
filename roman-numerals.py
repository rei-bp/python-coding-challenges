def solution(n):
    import math
    # put roman nums in dictionary to iterate
    roman = {
        'M': 1000,
        'CM': 900,
        'D': 500,
        'CD': 400,
        'C': 100,
        'XC': 90,
        'L': 50,
        'XL': 40,
        'X': 10,
        'IX': 9,
        'V': 5,
        'IV': 4,
        'I': 1
    }
    str = ''
    
    # iterate and find how many roman num are in n beginning with the largest roman num
    for i in roman:
        # find how many times each roman num is in n
        x = math.floor( n / roman[i])
        
        # reduce n to move on the next highest roman num
        n -= x * roman[i]
        
        # add the roman num to string by the amount of times the roman num is in n
        str += i*x
   
    return str
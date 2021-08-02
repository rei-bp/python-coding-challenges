def count_bits(n):
    binary = bin(n)[2:]
    blist = list(map(int, binary))
    return sum(blist)
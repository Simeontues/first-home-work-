def digits(n):
    l = 0

    while(n > 0):
        n = n // 10
        l += 1
    return l
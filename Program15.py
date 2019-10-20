def is_abundant(n):
    s = sum([fctr for fctr in range(1, n + 1) if n / fctr == 0])
    return s
print(is_abundant(12))

def power1(a, b):
    result = 1
    while b :
        if b % 2: result *= a
        a *= a
        b //= 2
        
    return result

print(power1(3,11))
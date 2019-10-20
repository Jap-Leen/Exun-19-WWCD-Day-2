# Binary to Decimal conversion
# Complexity: H

def function n: 
    temp = n
    value = 0
    c = 1 
    while (temp): 
        r = temp % 10  
        value += r * c 
        c *= 2 
        temp /= 10
    return value 



def isPowerOfThree(n):
    while True:
        if n == 1:
            return True
        elif n < 1:
            return False
        n /= 3
    
print(isPowerOfThree(27))
def sumDigit(x):
    sum =x%10
    return sumDigits(x//10,sum)
        
def sumDigits(x,sum):
    sum = sum + x%10
    if x < 10:
        print (sum)
    else:
        sumDigits(x//10, sum)

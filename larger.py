def largediv(x, y):
    if x > y:
        small = y
    else:
        small = x
    for i in range(1, small+1):
        if((x % i == 0) and (y % i == 0)):
            large = i
            
    return large

number1,number2=map(int,(input().split()))
print(largerdiv(number1, number2))

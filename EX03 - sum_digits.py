n = int(input("Enter an integer number: "))
sum = 0

while n != 0:
    rest = n % 10
    n = (n-rest)//10
    sum = sum + rest
print(sum)
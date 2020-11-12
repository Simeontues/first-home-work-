num = int(input("Enter a number: "))
a = num
b = 0
while(num > 0):
    c = num % 10
    b = b * 10 + c
    num = num // 10
if(a == b):
    print(a, "-> True")
else:
    print(a, "-> False")
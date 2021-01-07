from dig import digits
def disarium(x, n):
    s = 0

    while(n > 0):
        r = n % 10
        s = s + (r ** x)
        x -= 1
        n = n // 10
    return s

n = int(input("Enter a number: "))
x = digits(n)
m = disarium(x, n)

if(m == n):
    print("Disarium")
else:
    print("Not Disarium")
def a(n):
    for d in n:
        if int(d) % 2:
            return False
    return True


c = []
for n in range(2000, 5000):
    if a(str(n)):
        c.append(n)

print(f"{', '.join(map(str, c))}")
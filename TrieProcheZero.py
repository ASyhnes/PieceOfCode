import random
l = [random.randint(-10,10) for i in range(5)]
m = l[0]
for x in l:
    if abs(x) < abs(m):
        m = x

print(l)
print(m)

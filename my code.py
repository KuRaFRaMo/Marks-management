k = int(input())
b = {}
for i in range(k):
    key = str(input())

    # to input a list to dictionary value i declaare a list
    m = []
    for j in range(3):
        n = int(input())
        m.append(n)
    # list element added to value

    value = list(m)
    b[key] = value

a = str(input())
summ = 0
for l in b[a]:
    summ = summ+l
avg = summ/3
print(avg)

file = open("liczby.txt")
data=[]
for f in file:
    data.append(f.strip())

ile = 0
for i in data:
    if int(i) % 2 == 0:
        ile += 1

b = 0
for j in data:
    x = int(j, 2)
    if x > b:
        b = x
print(ile,bin(b)[2:], b)
ile2 = 0
ile1 = 0
for d in data:
    if len(d) == 9:
        ile1 += 1
        ile2 += int(d, 2)
print(ile1, bin(ile2)[2:])
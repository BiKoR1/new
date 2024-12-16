file = open("pary.txt")
file2 = open("wyniki.txt", "w")
data = []

for f in file:
    f = f.strip().split()
    f[0] = int(f[0])
    data.append(f)

def isPrime(n):
    if n < 2:
        return False
    for i in range(2,n):
        if n % i == 0:
            return True
    return False

a = []

for d in data:
    num = d[0]
    if isPrime(num):
        a.append(num)

print("zad 1", file = file2)
print(len(a), "%", sep = '', file = file2)
print(a[-1], file = file2)

numm, dzz = 0, []
for d in data:
    num = d[0]
    dz = []
    for i in range(1, num + 1):
        if num % i == 0:
            dz.append(i)
    if len(dz) > len(dzz):
        dzz = dz
        numm = num

print("zad 2", file = file2)
print(numm, len(dzz), *dzz, file = file2)

c = ''
for d in data:
    word = d[1]
    if word == word[::-1]:
        if len(word) == len(c):
            c = word
print("zad 3", file = file2)
print(c, len(c), file = file2)

mediana, srednia = [], 0
for d in data:
    num = d[0]
    srednia += num
    mediana.append(num)
mediana = sorted(mediana)
mediana = (mediana[49] + mediana[50])
srednia /= 100 
print(mediana, srednia)





file2.close()











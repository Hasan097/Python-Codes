a = [60,35,81,98,14,47]
n = len(a)
count = []
s = []
for i in range(n):
    count.append(0)
    s.append(0)

for i in range(n):
    for j in range(i + 1, n):
        if a[i] < a[j]:
            count[j] = count[j] + 1
        else:
             count[i] = count[i] + 1

for i in range(n):
    s[count[i]] = a[i]

print(s)


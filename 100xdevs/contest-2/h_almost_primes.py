n = int(input())

div_count = [0] * (n + 1)
for i in range(1, n + 1):
    for j in range(i, n + 1, i):
        div_count[j] += 1

print(*(x for x in range(1, n + 1) if div_count[x] <= 4))

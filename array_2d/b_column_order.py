# B. Column Order - print all matrix elements column by column, space-separated
import sys

data = sys.stdin.read().split()
p = 0
n = int(data[p]); p += 1
m = int(data[p]); p += 1

matrix = []
for _ in range(n):
    row = data[p:p + m]
    p += m
    matrix.append(row)

out = []
for j in range(m):          # each column, left to right
    for i in range(n):      # each row within the column, top to bottom
        out.append(matrix[i][j])

print(' '.join(out))

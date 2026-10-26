# A. Row Order - print all matrix elements row by row, space-separated
import sys

data = sys.stdin.read().split()
p = 0
n = int(data[p]); p += 1
m = int(data[p]); p += 1

# tokens already arrive in row order, so collecting n*m of them
# preserves the row-by-row order we need to print
nums = data[p:p + n * m]

print(' '.join(nums))

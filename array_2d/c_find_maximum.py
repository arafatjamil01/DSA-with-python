import sys

data = sys.stdin.buffer.read().split()
p = 0
n = int(data[p]); p += 1
m = int(data[p]); p += 1
nums = list(map(int, data[p:p + n * m]))

print(max(nums))

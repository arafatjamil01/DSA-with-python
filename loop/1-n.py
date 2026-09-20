# n = int(input())

# for i in range(n):
#     print(i+1)

import sys

n = int(sys.stdin.readline());
for i in range(1, n + 1):
    sys.stdout.write(str(i) + '\n')
## Using loops only
# n,m = list(map(int, input().split()))

# for i in range(n):
#     for j in range(m):
#         print('*', end='')

#     print()

# This is better, pythonic, and takes less memory
n, m = list(map(int, input().split()))

for _ in range(n):
    print('*' * m)
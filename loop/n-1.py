n = int(input())
for i in range(n, 0, -1):
    print(f"{i}", end=" ")

# Faster version
# n = int(input())
# print(" ".join(map(str, range(n, 0, -1))))

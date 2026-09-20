# two given integers, print every integer in between
# l,r = list(map(int, input().split()))
# print(*range(l,r+1))

l, r = map(int, input().split())

for i in range(l, r + 1):
    print(i, end=' ')

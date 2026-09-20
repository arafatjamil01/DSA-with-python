# https://codeforces.com/group/4vcXCPx8NY/contest/667712/problem/E
# x is a factor of 18 (i.e., 18modx=0), or x is a multiple of 45 (i.e., xmod45=0).
n = int(input())

nums = list(map(int, input().split()))
count = 0

for x in nums:
    if(x != 0 and 18 % x == 0) or ( x % 45 == 0):
        count += 1

print(count)
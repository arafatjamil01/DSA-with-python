import sys
data = sys.stdin.read().split()
t = int(data[0])
p = 1
out = []

for _ in range(t):
    n = int(data[p]); p += 1
    nums = list(map(int, data[p:p+n])); p += n
    x = int(data[p]); p += 1

    cnt = {}          # value -> how many times it appears at indices < j
    ans = 0
    for j in range(n):
        for k in range(j + 1, n):
            ans += cnt.get(x - nums[j] - nums[k], 0)
        cnt[nums[j]] = cnt.get(nums[j], 0) + 1

    out.append(str(ans))

print("\n".join(out))

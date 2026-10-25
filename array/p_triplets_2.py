import sys

data = sys.stdin.read().split()

t = int(data[0])
p = 1

for _ in range(t):
    n = int(data[p]);p+=1
    nums = list(map(int, data[p:p+n]));p+=n
    x = int(data[p]);p+=1

    nums.sort()
    ans = 0
    for i in range(n):
        lo, hi = i+1, n-1
        while lo < hi:
            s = nums[i] + nums[lo] + nums[hi]
            if s < x:
                lo += 1
            elif s > x:
                hi -= 1
            else:
                if nums[lo] == nums[hi]:
                    m = hi - lo + 1
                    ans += m*(m-1)//2
                    break
                c1 = 1
                while nums[lo+1] == nums[lo]:
                    lo += 1;c1 += 1
                c2 = 1
                while nums[hi-1] == nums[hi]:
                    hi -= 1;c2 += 1
                ans += c1*c2
                lo += 1;hi -= 1
    print(ans)

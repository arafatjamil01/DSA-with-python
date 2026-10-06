import sys
data = sys.stdin.read().split()
n = int(data[0])
nums = data[1:1+n]
k = n//2-1
l = k+1
res = []
while(k>=0):
    res.append(nums[k])
    res.append(nums[l])
    k -=1
    l+=1

print((" ").join(res))
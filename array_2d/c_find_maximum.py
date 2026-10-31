import sys

data = sys.stdin.read().split()
p = 0
n = int(data[p]);p+=1
m = int(data[p]);p+=1
nums = data[p:p+n*m]

print(max(nums))
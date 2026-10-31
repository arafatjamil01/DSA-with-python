import sys

data = sys.stdin.read().split()
p = 0
n = int(data[p]);p+=1
m = int(data[p]);p+=1
x = int(data[p]);p+=1
nums = list(map(int,data[p:p+n*m]))

if x in nums:
    print('true')
else:
    print('false')
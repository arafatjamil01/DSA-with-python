# n = int(input())
# times = list(map(int, input().split()))
# # output is item postion + 1, or i+1

# mt = times[0]
# i = 1
# z = 1
# while(i<n):
#     if(mt >= times[i]):
#         mt = times[i]
#         z = i
#     i +=1
# print(z+1)

import sys


data = sys.stdin.read().split()
n = int(data[0])
nums = [int(x) for x in data[1:n+1]]
print(nums)


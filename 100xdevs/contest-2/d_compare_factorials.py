# import sys
# nums = [int(x) for x in sys.stdin.read().split()]
# afac, bfac = 1,1

# if(nums[0] != 0 and nums[0] != 1):
#     for i in range(1, nums[0]+1):
#         afac *= i

# if(nums[1] !=0 and nums[1] != 1):
#     for j in range(1, nums[1]+1):
#         bfac *=j

        
# if afac == bfac:
#     print('Yes')
# else:
#     print('No')

# The trick is to compare if those two are same, 
# rather tahn calculating actual factorial

import sys

a, b = map(int, sys.stdin.read().split())

if a == b or (a in (0, 1) and b in (0, 1)):
    print('Yes')
else:
    print('No')
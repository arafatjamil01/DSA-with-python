# # Old solution (wrong on test 5): only compared first and last elements,
# # so arrays like "2 1 2" incorrectly printed YES.
# import sys
# data = [int(x) for x in sys.stdin.read().split()]
# n = data[0]
# nums = data[1:1+n]
# if nums[0] == nums[n-1]:
#     print('YES')
# else:
#     print('NO')

import sys

data = sys.stdin.read().split()
n = int(data[0])
nums = data[1:1 + n]

# print('YES' if all(x == nums[0] for x in nums) else 'NO')
# is_beautiful = True
# for i in range(n):
#     if(nums[0] == nums[i]):
#         continue
#     else:
#         is_beautiful = False
#         break

# print('YES' if is_beautiful else 'NO')
import sys

data = sys.stdin.read().split()
n = int(data[0])
nums = data[1:1 + n]

# print('YES' if all(x == nums[0] for x in nums) else 'NO')
for i in range(n):
    if nums[i] != nums[0]:
        print('NO')
        break
else:
    print('YES')

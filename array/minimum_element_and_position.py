n = int(input())
nums = list(map(int, input().split()))
minimum = min(nums)
position = nums.index(minimum) + 1
print(minimum, position)

# alternative 
# n = int(input())
# nums = list(map(int, input().split()))

# minimum = nums[0]
# position = 0

# for i in range(1, n):
#     if nums[i] < minimum:
#         minimum = nums[i]
#         position = i

# print(minimum, position + 1)
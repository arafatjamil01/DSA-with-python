n = input()
nums = list(map(int, input().split()))
max_num = max(nums)
max_pos = nums.index(max_num)+1
print(max_num, max_pos)
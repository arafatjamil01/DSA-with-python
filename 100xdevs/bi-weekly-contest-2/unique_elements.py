# Need to optimzie
_ = int(input())
nums = list(map(int, input().split()))
unique_list = []

for i in nums:
    if(nums.count(i) == 1):
        unique_list.append(i)
    
str_nums = map(str, unique_list)
unique_list = " ".join(str_nums)
print(unique_list)
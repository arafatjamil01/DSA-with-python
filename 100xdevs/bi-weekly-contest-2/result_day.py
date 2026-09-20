_ = int(input())
nums = list(map(int, input().split()))
pass_mark = int(input())

pass_count = 0
fail_count = 0

for i in nums:
    if(i>= pass_mark):
        pass_count +=1
    else:
        fail_count +=1
    

print('Pass: ', pass_count)
print('Fail: ', fail_count)
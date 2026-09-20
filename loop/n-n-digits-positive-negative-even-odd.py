n = input()
nums = list(map(int, input().split()))
pos = 0
neg = 0
even = 0
odd = 0


for i in nums:
    if(i < 0):
        neg +=1
    elif( i>0 ):
        pos +=1
    
    if(i % 2 == 0):
        even+=1
    else:
        odd+=1

print(pos, neg, even, odd, sep='\n')
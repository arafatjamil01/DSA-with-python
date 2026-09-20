# Need to optimzie
n = int(input())
times = list(map(int, input().split()))
res = 0

for i in range(n):
    temp = times[i]
    if(i!=n-1):
        if(times[i] > times[i+1]):
            temp = times[i+1]
            res = i
        elif(times[i] == times[i+1]):
            res +=1

print(res+1)
        
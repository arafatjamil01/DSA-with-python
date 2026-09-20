a,b = map(int, input().split())
x = 0
y = 0

if(a > b):
    x = b
    y = a
elif(a < b):
    x = a
    y = b
elif(a == b):
    x = a
    y = b

# Min = X
# Max = Y

print("Min = ", x)
print("Max = ", y)
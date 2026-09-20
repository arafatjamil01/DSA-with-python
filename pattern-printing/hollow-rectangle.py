# in hollow, the first and last one should work
# n, m = list(map(int, input().split()))

# for i in range(n):
#     if( i == 0 or i == n-1):
#         print('*' * m)
#     else:
#         print('*' + ' ' * (m-2) + '*')
        

# nested loop process, takes more time, less efficient.        
n, m = list(map(int, input().split()))

for i in range(n):
    for j in range(m):
        if(i == 0 or i == n-1 or j == 0 or j == m-1):
            print('*', end="")
        else:
            print(' ', end="")
    print()
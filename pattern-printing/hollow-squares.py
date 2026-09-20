# in hollow, the first and last one should work
# n = int(input())

# for i in range(n):
#             # If it's the first or last row, print a full line of stars
#             if i == 0 or i == n - 1:
#                 print('*' * n)
#             else:
#                 print('*' + ' ' * (n - 2) + '*')
                
# Nested loop process
# in hollow, the first and last one should work
n = int(input())

for i in range(n):
    for j in range(n):
        if(i == 0 or i == n-1 or j == 0 or j == n-1):
            print('*', end="")
        else:
            print(' ', end="")
    print()
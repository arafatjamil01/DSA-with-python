# n = int(input())

# for i in range(1, 2 * n):
#     # Same spacing logic you already used
#     space_before = ' ' * abs(n - i)
    
#     # Calculate how many stars would have been in this row
#     if i <= n:
#         count = i
#     else:
#         count = 2 * n - i
    
#     # Logic for hollow stars
#     if count == 1:
#         # Top and bottom tips
#         print(space_before + '*')
#     else:
#         # Internal spaces = (count - 2) stars + the spaces between them
#         # Formula for internal gap: 2 * (count - 1) - 1
#         inner_spaces = ' ' * (2 * (count - 1) - 1)
#         print(space_before + '*' + inner_spaces + '*')

# better, two loops solutions
n = int(input())

for i in range(1,n+1):
    leading_space = ' '*(n-i);
    if(i==1):
        print(leading_space + '*')
    else:
        print(leading_space + '*' + ' ' * (2*i -3) + '*' )
    
for i in range(n-1, 0, -1):
    leading_space = ' '*(n-i);
    if(i==1):
        print(leading_space + '*')
    else:
        print(leading_space + '*' + ' ' * (2*i -3) + '*' )
    
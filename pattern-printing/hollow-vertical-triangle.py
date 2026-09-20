# More Efficient
n = int(input())

for i in range(1, 2 * n):
    # Calculate stars: i if in the first half, (2n - i) if in the second half
    if i <= n:
        stars = i
    else:
        stars = 2 * n - i
    
    # Print hollow pattern: only stars at edges
    if stars == 1:
        print('*')
    else:
        print('*' + ' ' * (2 * stars - 2) + '*')


# n = int(input())

# for i in range(1, 2 * n):
#     # Calculate how many stars would be in this row if it were solid
#     count = n - abs(n - i)
    
#     if count == 1:
#         print('*')
#     else:
#         # Calculate spaces to maintain the same width as the solid triangle
#         spaces = ' ' * (2 * count - 2)
#         print(f'*{spaces}*')
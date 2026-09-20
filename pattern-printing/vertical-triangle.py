# n = int(input())

# Two loops solutions
# for i in range(n):
#     print('* ' * (i+1))

# for i in range(n-1):
#     print('* ' * (n-1-i))


# Single loop solution, more efficient
n = int(input())

for i in range(1, 2 * n):
    # Calculate stars: i if in the first half, (2n - i) if in the second half
    if i <= n:
        stars = i
    else:
        stars = 2 * n - i
    
    # Print the star followed by a space, repeated 'stars' times, then stripped of trailing space
    print('* ' * stars)
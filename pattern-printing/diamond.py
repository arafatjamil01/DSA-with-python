n = int(input())

for i in range(1, 2*n):
    space_before = ' ' * abs(n-i)

    if(i<=n):
        stars = ' '.join(['*'] * i)
    else:
        stars = ' '.join(['*'] * (2*n - i))

    print(space_before + stars)
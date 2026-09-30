n,m = list(map(int, input().split()))

for i in range(1, n+1):
    if(i == 1 or i == n or m == 1):
        print('^' * m);
    else:
        print('^' + ' ' * (m-2) + '^')
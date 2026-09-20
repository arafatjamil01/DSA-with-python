t = input()
for _ in range(t):
    n = int(input())
    odds = list(range(1,n+1,2))
    evens = list(range(2, n+1,2))
    print(odds+evens.reverse())
    
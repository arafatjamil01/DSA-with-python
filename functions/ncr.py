def fact(n):
    factorial = 1
    if n == 0:
        return factorial
    
    for i in range(1,n+1):
        factorial *= i
    
    return factorial

n, r = map(int, input().split())
print(int(fact(n) / (fact(r) * fact(n-r))))
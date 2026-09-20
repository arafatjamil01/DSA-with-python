# cook your dish here
def print_factors(n):
    for i in range( n+1, 0, -1):
        if(n % i == 0):
            print(i, end=" ")

n = int(input())
print_factors(n)
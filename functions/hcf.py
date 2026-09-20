# HCF -> Highest common factor
# GCD -> Greatest common divisor
# Both are same

def findHCF(a,b):
    hcf = 1
    for i in range(1, min(a,b) + 1):
        if a % i == 0 and b % i == 0:
           hcf = i
    return hcf     


a,b = map(int, input().split())
print(findHCF(a,b))
# import math
#
# n = int(input())
# # Factor of n is special, if ends up with 2 or 7 in the end
# factors = []
# for i in range(1,n+1):
#     if n % i == 0:
#         factors.append(i)
#
# spec_fact = []
# for j in factors:
#
#     if j % 10 == 2 or j % 10 == 7:
#         spec_fact.append(str(j))
#
# if(len(spec_fact) > 0):
#     print((" ").join(spec_fact))
# else:
#     print(-1)

import math

n = int(input())

factors = []
for i in range(1, math.isqrt(n) + 1):
    if n % i == 0:
        factors.append(i)
        if i != n // i:
            factors.append(n // i)

factors.sort()
special = [str(d) for d in factors if d % 10 in (2, 7)]

print(" ".join(special) if special else -1)

# You are given an array of integers and an integer X
# .

# Find how many times X
#  appears in the array.

# Input
# First line contains two integers N
#  and X
#  (1≤N≤105,−109≤X≤109)
# .
# Second line contains N
#  integers A1,A2,…,AN
#  (−109≤Ai≤109)
# .
# Output
# Print a single integer — the number of times X
#  appears in the array.

# Input
# 6 3
# 1 5 2 3 7 3

# Output
# 2

# n,x = input().split()
# arr = input().split()
# count = 0

# for i in arr:
#    if i == x:
#        count = count + 1

# print(count)

n,x = input().split()
arr = input().split()


print(arr.count(x))
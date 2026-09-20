# If a number exists in an array, num is the number below

# Read N and X from the first line
n, x = input().split()

# Read the array elements from the second line as a list of strings
arr = input().split()

# Python's 'in' operator performs a fast linear search
if x in arr:
    print("YES")
else:
    print("NO")

# Array sorted
# Read the number of elements
n = int(input())

# Read the array elements and convert them to integers
arr = list(map(int, input().split()))

# Check if every element is less than or equal to the next one
# The all() function stops checking (short-circuits) as soon as it finds a False
# is_sorted = all(arr[i] <= arr[i+1] for i in range(n - 1))

is_sorted = all(arr[i] <= arr[i+1] for i in range(n-1))

# Print the result according to the problem statement
if is_sorted:
    print("YES")
else:
    print("NO")
# n = int(input())
# zc = 0

# # Special case for the number 0
# if n == 0:
#     zc = 1
# else:
#     while n > 0:
#         # Check if the LAST digit is 0
#         if n % 10 == 0:
#             zc += 1
#         # Remove the last digit
#         n //= 10

# print(zc)

# Pythonic shortcut
print(input().count('0'))
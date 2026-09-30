# You are given an integer N
# Your task is to print the second last digit of N
n = int(input())
print((n//10 % 10)) # n//10 is for getting integer
#this works because, n % 10 gives the last digit, as result, and n / 10 gives the result, other than the last digit
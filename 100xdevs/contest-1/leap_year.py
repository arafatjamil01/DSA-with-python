# To check whether a year is a leap year, follow these rules:

# First check if the year is divisible by 100, If it is, then it must also be divisible by 400 to be a leap year.
# If the year is not divisible by 100, then it is a leap year if it is divisible by 4, 

#  You are given a year Y, if leap year, print "Yes" otherwise "No"

n = int(input());

if(n % 100 == 0 and n % 400 == 0) or ( n % 100 != 0 and n % 4 == 0):
    print('Yes')
else:
    print('No')
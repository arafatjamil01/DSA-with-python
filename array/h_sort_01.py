num_of_array = int(input())
for _ in range(num_of_array):
    num_of_digits = input()
    arr = input().split()
    
    zeros = arr.count('0')
    ones = arr.count('1')
    print('0 ' * zeros + '1 ' * ones)


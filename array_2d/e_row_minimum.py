import sys

data = sys.stdin.read().split()
p = 0
n = int(data[p]);p+=1
m = int(data[p]);p+=1
nums = list(map(int, data[p:p+n*m]))

# dont' need all these, since when nums start, in every 'row' or nth num, find the minimum and add it in a row. 
matrix = []
for _ in range(n):
    row = data[p:p+m]
    p+=m
    matrix.append(row)

min_nums = []
for _ in range(m):


# print(min_nums)
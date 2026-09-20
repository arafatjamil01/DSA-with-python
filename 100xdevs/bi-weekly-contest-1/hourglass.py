# n = int(input())

# for i in range(2*n +1):

#     prev_space = ''
#     dot_count = 0
#     if(i<n):
#         prev_space = ' ' * i
#         dot_count = n-i
       
#     elif(i>n):
#         prev_space = ' ' * (2*n - i)
#         dot_count = i - n
    
#     dots = ' '.join(['.'] * dot_count)
#     if(i!=n and i != n+1):
#         print(prev_space + dots)
        
# alternative solution
n = int(input())

for i in range(n - 1, -n, -1):
    dot_count = abs(i) + 1
    spaces = " " * (n - dot_count)
    
    # join() only puts spaces BETWEEN strings in the list
    dots = " ".join(["."] * dot_count)
    
    print(spaces + dots)
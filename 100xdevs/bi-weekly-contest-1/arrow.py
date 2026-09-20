n = int(input())
inner_spaces = 1
 
for i in range(1, 2*n):
    # print(i)
    leading_space = 0
    
           
    if(i==1 or i == 2*n-1):
        arrows = '>'
    else:
        arrows = '>' + ' ' * (inner_spaces -2) + '>'
 
 
    if(i<n):
        leading_space = i-1
        inner_spaces +=2
    else:
        leading_space = 2*n - i-1
        inner_spaces -=2
    
    print(' ' * leading_space + arrows)
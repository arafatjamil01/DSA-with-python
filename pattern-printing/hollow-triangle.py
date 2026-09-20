n = int(input())
for i in range(1, n + 1):
    # Calculate leading spaces
    leading_spaces = ' ' * (n - i)

    # Construct the star pattern for the row
    # Using ' '.join(['*'] * i) is memory efficient
    row_stars = '';
    if(i==n or i == 1):
        row_stars = ' '.join(['*'] * i);
    else:
        # 2i-3 converts 1, 2, 3,4 into -1 1 3 5 7...
        row_stars += ((2*i - 3) * ' ').join(['*'] * 2)
    
    
    # making a string of triangles, and printing at last
    print(leading_spaces + row_stars)
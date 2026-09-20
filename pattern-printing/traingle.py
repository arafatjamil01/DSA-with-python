n = int(input())

for i in range(1, n + 1):
    # Calculate leading spaces
    leading_spaces = ' ' * (n - i)
    
    # Construct the star pattern for the row
    # Using ' '.join(['*'] * i) is memory efficient

    row_stars = ' '.join(['*'] * i)
    
    # making a string of triangles, and printing at last
    print(leading_spaces + row_stars)
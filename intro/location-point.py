# Taking input from the user
x,y = map(int, input().split())
# 1. Check for Origin
if x == 0 and y == 0:
    print("Origin")

# 2. Check for Axes
elif x != 0 and y == 0:
    print("X axis")
elif x == 0 and y != 0:
    print("Y axis")

# 3. Check Quadrants
elif x > 0 and y > 0:
    print("1st Quadrant")
elif x < 0 and y > 0:
    print("2nd Quadrant")
elif x < 0 and y < 0:
    print("3rd Quadrant")
elif x > 0 and y < 0:
    print("4th Quadrant")


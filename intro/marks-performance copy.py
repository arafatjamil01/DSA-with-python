# Taking input from the user
marks = int(input())

# Grading logic
if marks > 90:
    print("Excellent")
elif marks > 80:
    # We don't need to check "and marks <= 90" because 
    # if it was > 90, the first 'if' would have caught it.
    print("Good")
elif marks > 70:
    print("Fair")
elif marks > 60:
    print("Meets Expectations")
else:
    print("Below Par")
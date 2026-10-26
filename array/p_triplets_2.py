# 2 pointer solution
import sys

data = sys.stdin.read().split()

test_case_count = int(data[0])
p = 1

for _ in range(test_case_count):
    array_size = int(data[p])
    p += 1
    numbers = list(map(int, data[p:p + array_size]))
    p += array_size
    x = int(data[p])
    p += 1

    numbers.sort()
    triplet_count = 0
    for i in range(array_size):
        # fix numbers[i] as the 1st element, search the 2nd+3rd in numbers[i+1..array_size-1]
        left, right = i + 1, array_size - 1
        while left < right:
            current_sum = numbers[i] + numbers[left] + numbers[right]
            if current_sum < x:
                left += 1            # sum too small -> pick a bigger middle value
            elif current_sum > x:
                right -= 1           # sum too big -> pick a smaller last value
            else:
                # current_sum == x: count ALL valid index pairs in left..right (duplicates count!)
                if numbers[left] == numbers[right]:
                    # whole left..right stretch is one repeated value:
                    # any 2 of these equal_count elements complete the triplet -> C(equal_count, 2)
                    equal_count = right - left + 1
                    triplet_count += equal_count * (equal_count - 1) // 2
                    break
                # else: count the run of equal values at left ...
                left_run_length = 1
                while numbers[left + 1] == numbers[left]:
                    left += 1
                    left_run_length += 1
                # ... and the run of equal values at right
                right_run_length = 1
                while numbers[right - 1] == numbers[right]:
                    right -= 1
                    right_run_length += 1
                triplet_count += left_run_length * right_run_length  # each left value pairs with each right value
                left += 1            # jump past both runs, keep searching
                right -= 1
    print(triplet_count)

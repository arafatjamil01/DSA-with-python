# t = int(input())
# for _ in range(t):
    n = int(input())
    odds = list(range(1,n+1,2))
    evens = list(range(2, n+1,2))
    evens.reverse()
    print(*odds+evens)

# t = int(input())
# for _ in range(t):
#     n = int(input())
#     print(*range(1, n + 1, 2), *range(n - n % 2, 1, -2))

# cook your dish here
def solve():
    # Read the number of test cases
    t = int(input())
    
    # Process each test case
    for _ in range(t):
        # Read n for the current test case
        n = int(input())
        
        # 1. Generate odd numbers in increasing order (1, 3, 5...)
        # We start at 1, go up to n+1 (exclusive), and step by 2
        odds = [str(x) for x in range(1, n + 1, 2)]
        
        # 2. Generate even numbers in decreasing order
        # If n is even, we start from n. If n is odd, we start from n - 1.
        # We step by -2 down to 1 (exclusive, so it stops at 2)
        start_even = n if n % 2 == 0 else n - 1
        evens = [str(x) for x in range(start_even, 1, -2)]
        
        # Combine the lists and print them space-separated
        print(" ".join(odds + evens))

if __name__ == '__main__':
    solve()
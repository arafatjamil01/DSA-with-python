def solve():
    # Easy approach - just use Python's `in` and `remove` on the list.
    # For each number in arr1, if it's still in arr2, keep it and remove ONE
    # copy from arr2 so it can't be matched twice.
    # (O(N * M), but N, M <= 1000 so it's fast enough here.)
    import sys

    # Read ALL numbers at once instead of line by line.
    # When N or M is 0, the judge may skip that line completely, so input()
    # would read the wrong line and crash. Reading tokens avoids that.
    data = iter(sys.stdin.read().split())

    t = int(next(data))
    for _ in range(t):
        n = int(next(data))
        arr1 = [next(data) for _ in range(n)]
        m = int(next(data))
        arr2 = [next(data) for _ in range(m)]

        result = []
        for x in arr1:
            if x in arr2:
                result.append(x)
                arr2.remove(x)  # removes only the first occurrence

        print(" ".join(result))
        
if __name__ == "__main__":
    solve()

# second block
# data = sys.stdin.read().split()
# idx=0
# t = int(data[idx]);idx+=1
# for _ in range(t):
#     n = int(data[idx]);idx+=1
#     arr1 = data[idx: idx +n];idx+=n
#     m = int(data[idx]); idx+=1
#     arr2 = data[idx:idx+m]; idx+=m
    
#     sol = []
#     # Intersection check
#     for x in arr1:
#         if x in arr2:
#             sol.append(x)
#             arr2.remove(x)
#     print((" ").join(sol))
    
    
import sys

# Previous solution (failed on test 10):
# - when N = 0 it printed nothing and didn't read X, so later tests read the wrong lines
# - the O(N^2) double loop is too slow in Python for t = 100, N = 1000
#
# def solution():
#     t = int(input())
#     if t!=0:
#         for _ in range(t):
#             n = int(input())
#             if n!=0:
#                 nums = list(map(int, input().split()))
#                 x = int(input())
#                 # first item + other items of array sum = x
#                 count = 0
#                 for i in range(n):
#                     a = nums[i]
#
#                     for j in range(i+1,n):
#                         if a + nums[j] == x:
#                             count +=1
#                 print(count)


def solution():
    data = sys.stdin.read().split()
    idx = 0
    t = int(data[idx]); idx += 1
    out = []
    for _ in range(t):
        n = int(data[idx]); idx += 1
        nums = data[idx:idx + n]; idx += n
        x = int(data[idx]); idx += 1

        # for each number, count how many earlier numbers complete the pair
        seen = {}
        count = 0
        for s in nums:
            a = int(s)
            count += seen.get(x - a, 0)
            seen[a] = seen.get(a, 0) + 1
        out.append(str(count))
    print("\n".join(out))


if __name__ == "__main__":
    solution()

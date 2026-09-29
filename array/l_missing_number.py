# def solve():
#     t = int(input())
#
#     for _ in range(t):
#         n = int(input())
#         nums = list(map(int, input().split()))
#
#         unique = 0
#         for x in nums:
#             unique ^= x
#
#         print(unique)
#
# if __name__ == "__main__":
#     solve()

# from collections import Counter
#
# def solve():
#     t = int(input())
#
#     for _ in range(t):
#         n = int(input())
#         nums = list(map(int, input().split()))
#
#         counts = Counter(nums)
#         for num, freq in counts.items():
#             if freq == 1:
#                 print(num)
#                 break
#
# if __name__ == "__main__":
#     solve()

def solve():
    t = int(input())

    for _ in range(t):
        n = int(input())
        nums = list(map(int, input().split()))
        nums.sort()

        unique = nums[-1]
        for i in range(0, n - 1, 2):
            if(nums[i] != nums[i+1]):
                unique = nums[i]
                break

        print(unique)

if __name__ == "__main__":
    solve()

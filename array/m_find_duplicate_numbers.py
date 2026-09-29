# https://codeforces.com/group/4vcXCPx8NY/contest/669913/problem/M
# 0 to n-2


def solve():
    t = int(input())

    for _ in range(t):
        n = int(input())
        if(n != 0):
            nums = list(map(int, input().split()))
            nums.sort()
            for i in range(n - 1):
                if(nums[i] == nums[i+1]):
                    print(nums[i])
                    break

if __name__ == "__main__":
    solve()
def solve():
    t = int(input())

    for _ in range(t):
        n = int(input())
        if(n !=0):
            nums = input().split()
            for i in range(1,n,2):
                nums[i],nums[i-1] = nums[i-1], nums[i]
            print((" ").join(nums))
        else:
            print()

if __name__ == "__main__":
    solve()

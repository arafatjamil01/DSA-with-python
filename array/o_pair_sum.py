import sys 

def solution():
    data = sys.stdin.read().split()
    idx = 0
    t = int(data[idx]); idx += 1
    out = []
    for _ in range(t):
        n = int(data[idx]); idx += 1
        nums = data[idx:idx + n]; idx += n
        x = int(data[idx]); idx += 1

        # # hashmap for each number, count how many earlier numbers complete the pair
        # seen = {}
        # count = 0
        # for s in nums:
        #     a = int(s)
        #     count += seen.get(x - a, 0)
        #     seen[a] = seen.get(a, 0) + 1

        # sort + two pointers
        arr = sorted(int(v) for v in nums)
        left, right = 0, n - 1
        count = 0
        while left < right:
            s = arr[left] + arr[right]
            if s < x:
                left += 1
            elif s > x:
                right -= 1
            else:
                if arr[left] == arr[right]:
                    m = right - left + 1
                    count += m * (m - 1) // 2
                    break
                cl = 1
                while arr[left + 1] == arr[left]:
                    cl += 1
                    left += 1
                cr = 1
                while arr[right - 1] == arr[right]:
                    cr += 1
                    right -= 1
                count += cl * cr
                left += 1
                right -= 1
        out.append(str(count))
    print("\n".join(out))


if __name__ == "__main__":
    solution()

import sys


def main():
    data = sys.stdin.buffer.read().split()
    n, m = int(data[0]), int(data[1])
    # The maximum over the whole matrix = max of all n*m values
    print(max(map(int, data[2:2 + n * m])))


if __name__ == "__main__":
    main()

_ = input()
my_list = list(map(int,input().split()))
my_list.sort(reverse=True)
print(" ".join(str(num) for num in my_list))
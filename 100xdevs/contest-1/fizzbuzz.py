n = int(input())

for i in range(1, n+1):
    if(i % 5 == 0 and i % 3 == 0):
        print('FizzBuzz')
    elif(i%5==0):
        print("Buzz")
    elif(i%3 == 0):
        print('Fizz')
    else:
        print(i)

# better version below.
# n = int(input())

# for i in range(1, n + 1):
#     if i % 15 == 0: # Instead of doing two different modulo, they have combined 3*5=15, which is LCM(3,5)=15 and used only one modulo
#         print("FizzBuzz")
#     elif i % 3 == 0:
#         print("Fizz")
#     elif i % 5 == 0:
#         print("Buzz")
#     else:
#         print(i)

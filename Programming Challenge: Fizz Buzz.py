for num in range(1, 51):
    if num % 15 == 0:
        print("FizzBizz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Bizz")
    else:
        print(num)
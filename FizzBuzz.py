for x in range(1, 101):
    if x % 15 == 0:
        print("FizzBuzz")
    elif x % 5 == 0:
        print("buzz")
    elif x % 3 == 0:
        print("fizz")
    else:
        print(x)

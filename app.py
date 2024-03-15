def fizz_buzz():
    print("\t\t\t\tWELCOME TO FIZZYLOGIC")
    print("\t\t\t   Let's play a FizzBuzz ;0 ")
    while True:
        n = int(input("\nEnter a Number to start or 0 to Exit "))
        if n == 0:
            print("Exiting the game. Goodbye!")
            break
        elif n % 3 == 0 and n % 5 == 0:
            print("FizzBuzz")
        elif n % 3 == 0:
            print("Fizz")
        elif n % 5 == 0:
            print("Buzz")
        else:
            print(n)


fizz_buzz()


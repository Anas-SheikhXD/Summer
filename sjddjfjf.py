def countdown(n):
    if n == 0:                  # base case — stops recursion
        print("Liftoff!")
        return
    print(n)
    countdown(n - 1)             # function calls itself

countdown(3)
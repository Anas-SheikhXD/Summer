def broken(n):
    print(n)
    broken(n + 1)    # no base case! never stops!

broken(1)
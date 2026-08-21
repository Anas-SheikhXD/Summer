def a():
    print("a starts")
    b()
    print("a ends")

def b():
    print("b starts")
    c()
    print("b ends")

def c():
    print("c runs")

a()
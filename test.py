def divide(a, b):
    try:
        c = a/b
        print(c)
    except:
        print("ZeroDivisionError: division by zero is not possible")

divide(10, 0)
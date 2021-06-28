# fill in this function
def fib():
    a=1
    b=1
    while True:
        yield a
        a,b=b,a+b

# testing code
import types
if type(fib()) == types.GeneratorType:
    print("Good, The fib function is a generator.")

    counter = 0
    for n in fib():
        print(n)
        counter += 1
        if counter == 10:
            break
# your code goes here
def multiplier_of(num):
    def multiply_with_5(n):
        print(num*n)
    return multiply_with_5

multiplywith5 = multiplier_of(5)
multiplywith5(9)
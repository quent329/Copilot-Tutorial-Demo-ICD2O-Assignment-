a = 65
b = 4
#if a is even, print out "potato", if b is odd, print out "tomato", otherwise, make a new variable c = b + a and print c
if a % 2 == 0:
    print("potato")
elif b % 2 != 0:
    print("tomato")
else:
    c = b + a
    print(c)

#make a function that calculates the factorial of any number and print it out depending on what number was inputted
n = 3
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(n))
    
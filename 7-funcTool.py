## Functional Tools

## partial application of functions (currying)

def exp(base, power):
    return base ** power

## 2 ^ power
def two_to_the(power):
    return exp(2, power)


from functools import partial
two_to_the = partial(exp, 2)
print two_to_the(3)

square_of = partial(exp, power=2)
print square_of(3)
 

def double(x):
return 2 * x
xs = [1, 2, 3, 4]
twice_xs = [double(x) for x in xs]
twice_xs = map(double, xs)
list_doubler = partial(map, double)
twice_xs = list_doubler(xs)

def multiply(x, y):
    return x * y

products = map(multiply, [1, 2], [4, 5])

def is_even(x):
    return x % 2 == 0

x_evens = [ x for x in xs if is_even(x)]

x_evens = filter(is_even, xs)
list_evener = partial(filter, is_even)
x_evens = list_evener(xs)


x_product = reduce(multiply, xs)
list_product = partial(reduce, multiply)
x_product = list_product(xs)

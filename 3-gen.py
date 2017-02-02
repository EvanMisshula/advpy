## A problem with lists is that they can easily grow very big. range(1000000)
## creates an actual list of 1 million elements. If you only need to deal
## with them one at a time, this can be a huge source of inefficiency
## (or of running out of memory). If you potentially only need the first
## few values, then calculating them all is a waste.
## A generator is something that you can iterate over (for us, usually
## using for) but whose values are produced only as needed (lazily).

def lazy_range(n):
"""a lazy version of range"""
   i = 0
   while i < n:
       yield i
       i += 1

for i in lazy_range(10):
    do_something_with(i)
#lazy

## The flip side of laziness is that you can only iterate through a gen‐
## erator once. If you need to iterate through something multiple
## times, you’ll need to either recreate the generator each time or use a
## list.

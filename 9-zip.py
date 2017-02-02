## Zip

to a single list of tuples of list1 = ['a', 'b', 'c']
list2 = [1, 2, 3]
my_zipList = zip(list1, list2)
print my_zipList

## unpack
pairs = [('a',1), ('b',2), ('c',3)]
letters, numbers = zip(*pairs)
print letters
print numbers

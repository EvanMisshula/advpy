## List comprehension


even_numbers = [x for x in range(5) if x % 2 == 0]
squares = [x * x for x in range(5)]
even_squares = [x * x for x in even_numbers]

print even_numbers
print squares 
print even_squares


## works for dicts and sets

square_dict = { x : x * x for x in range(5) }
square_set = { x * x for x in [1, -1] }

print square_dict
print square_set
 
## mult loops

pairs = [(x, y)
         for x in range(10)
         for y in range(10)]

print pairs

## later loops can use results of earlier ones

increasing_pairs = [(x, y)
                    for x in range(10)
                    for y in range(x + 1, 10)]

print increasing_pairs




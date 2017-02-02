## randomness

import random
four_uniform_randoms = [random.random() for _ in range(4)]
print four_uniform_randoms


## pseudo-randomness

random.seed(10)
print random.random()
random.seed(10)
print random.random()

#range
print random.randrange(10)
print random.randrange(3, 6) 

#shuffle
up_to_ten = range(10)
random.shuffle(up_to_ten)
print up_to_ten

#choice
my_best_friend = random.choice(["Alice", "Bob", "Charlie"])
 
# without replacement
lottery_numbers = range(60)
winning_numbers = random.sample(lottery_numbers, 6)
print winning_numbers

# with replacement
four_with_replacement = [random.choice(range(10))
for _ in range(4)]
print four_with_replacement

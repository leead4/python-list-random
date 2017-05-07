# Using the random module and the range method, generate a 
# list of 20 random numbers between 0 and 49.


# import random
# random_numbers = [...insert awesome code here...]
# print(random_numbers)

# With the resulting list, use a list comprehension to 
# build a new list that contains each number squared. For example, 
# if the original list is [2, 5], the final list will be [4, 25].
import random

random_list = []
for i in range(20):
	random_list.append(random.randint(0,49))
	
print("random", random_list)

random_squared = [a*a for a in random_list]
print("squared", random_squared)




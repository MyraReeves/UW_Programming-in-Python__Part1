# Comprehensions - Iterate thru a list using a For loop with "nested"/"backwards" syntax

#############
# Example 1 #
#############

# Using the List method with range method to create a list from zero to 9:
normal_list = list(range(10))
print(normal_list)                                          # [0,1,2,3,4,5,6,7,8,9]

# Using a For loop to count from 0 to 9 on separate lines (ie. vertically) in the console:
for x in range(10):
    print(x)                                                # (See console for result)

# Comprehension will take the syntax of that For loop but will map the output into being a list
comprehension_list = [x for x in range(10)]                 
print(comprehension_list)                                   # [0,1,2,3,4,5,6,7,8,9]


#############
# Example 2 #
#############

# Using a For loop to count from 1 to 10 vertically in the console: 
for x in range(10):
    print(x + 1)                                            # (See console for result)

# Creating a function that will count upward starting at 1:
def add_one(x):
    return x + 1

# Using that function with the range method inside a map construct to create a list from 1 to 10:
mapped_list = list(map(add_one, range(10)))
print(mapped_list)                                          # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Comprehension produces the same output:
compr_version = [add_one(x) for x in range(10)]
print(compr_version)                                        # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Comprehension can ALSO produce the same output without needing to use the function!  It can just use the expression!
compre_version = [x + 1 for x in range(10)]
print(compre_version)                                       # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


#############
# Example 3 #
#############

# Creating a function that filters numbers to produce only odd numbers:
def filter_odds(x):
    return x % 2

# Using that function in a For loop to vertically print in the console odd numbers only from 1 thru 9:
for x in range(10):
    if filter_odds(x):
        print(x)

# Using the List method and filter method with that function to create a list of those numbers:
odd_number_list = list(filter(filter_odds, range(10)))
print(odd_number_list)                                               # [1, 3, 5, 7, 9]

# Comprehension creates those same odd numbers inside a list:
odd_number_comprehension = [x for x in range(10) if filter_odds(x)]
print(odd_number_comprehension)                                      # [1, 3, 5, 7, 9]

# Again, Comprehension can produce the same output without needing to use the function!  It can just use the expression!
odd_number_compre = [x for x in range(10) if x % 2]
print(odd_number_compre)                                             # [1, 3, 5, 7, 9]


#############
# Example 4 #
#############

# Using the sum method on a list that filters out only the odd numbers 1 thru 9
the_sum = sum(list(filter(filter_odds, range(10))))
print(the_sum)                                                      # 25

# Using the sum method on a Comprehension
sum_of_comprehension = sum([x for x in range(10) if x % 2])
print(sum_of_comprehension)                                         # 25






# Note the similarity in syntax with SQL's "SELECT ... WHERE"!
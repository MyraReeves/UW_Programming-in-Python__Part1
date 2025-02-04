# Slicing Activity

# Write some functions that take a sequence as an argument, and return a copy of that sequence:
# with the first and last items exchanged.
# with every other item removed.
# with the first 4 and the last 4 items removed, and then every other item in the remaining sequence.
# with the elements reversed (just with slicing).
# with the last third, then first third, then the middle third in the new order.
# Example:   (1,2,3,4,5,6) should return: (5,6,1,2,3,4) (start with a length that's a multiple of three, but make sure it doesn't crash for other lengths)

# NOTE: These should work with any sequence- but you can use strings to test, if you like.
# Hint:  Your functions should work with all sequences. That means that you cannot use list methods, like .append, because that won't work with strings and tuples. But all sequences support concatenation with the + operator.
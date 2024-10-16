#################
#   Problem 5   #
#################

#  But what about the answers?
#  How can we record the answer to every question without making any changes to
#  the program other than adding a new question (or removing an existing question) from the tuple ?

# Possible solution = Responses could be pushed into the end of the tuple.
# Since tuples are immutable, the tuple could be converted into a list using the list() method,
# the new item pushed into the end of the list,
# and then the list converted back into a tuple using the tuple() method.

# If a variable is created beforehand to store the length of the tuple/list
# using the len() method before a response is added,
# then the index of each response would be 1 + that previous length value,
# and the response value could be displayed in the console using that.

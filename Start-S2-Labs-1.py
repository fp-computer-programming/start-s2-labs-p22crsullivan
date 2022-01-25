# Author: CRS 01/18/22
# Create a list
words = ["dog", "cat", "fish"]
# Define function split
def split(lst):
# Make a string variable
    var = ""
# Create a for loop to add words to each other
    for word in lst:
        if word != lst[len(lst) - 1]:
            var += word + " "
        else:
            var += word + " "
# Print the result
        print(var)
split(words)
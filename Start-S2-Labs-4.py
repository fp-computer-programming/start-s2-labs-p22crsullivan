# Define the function double_every_other
def double_every_other(l):
# Multiply each number by 2 and return it
    return [x * 2 if i % 2 else x for i, x in enumerate(l)]
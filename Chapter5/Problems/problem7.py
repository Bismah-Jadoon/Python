#  can u change the values inside a list which is contained in set s:
s = {8, 7, 12, "Harry", [1, 2]}

print(s)
# Answer:
# No, you cannot have a list inside a set in Python.
# Why?
# Sets in Python only allow immutable (unchangeable) elements because they rely on hash values for fast lookups. However, lists are mutable (their values can be changed), so they cannot be added to a set.
# What happens if you try?
# If you run:
# s = {8, 7, 12, "Harry", [1, 2]}

# You'll get:
# TypeError: unhashable type: 'list'
# How to Fix?
# If you need a collection of immutable elements, use a tuple instead of a list:

# s = {8, 7, 12, "Harry", (1, 2)}
# Now, s is valid because a tuple is immutable and hashable.

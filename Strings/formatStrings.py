# String Format

# We can't combine strings and numbers like this:
# age = 23
# txt = "My name is Francisco, I am " + age
# print(txt)

# But we can combine strings and numbers by using the format() method!

# The format() method takes the passed arguments, formats them,
# and places them in the string where the placeholders {} are:

# age = 23
# txt = "My name is Francisco, I am {}"
# print(txt.format(age))

# quantity = 3
# itemno = 567
# price = 49.95
# myorder = "I want {} pieces of item {} for {} dollars."
# print(myorder.format(quantity, itemno, price))


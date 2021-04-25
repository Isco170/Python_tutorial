# Python - Access List Items

# List items are indexed and you can access them by referring to the index number

myList = ["Apple", "Banana", "Cherry"]
# print(myList[1])

# Negative Indexing => means start from the end
# (-1 refers to the last item, -2 refers to the second last item etc).

# print(myList[-1])

# Range of Indexes => specify a range of indexes by specifying where to start and where to end the range.

myList = ["Apple", "Banana", "Cherry", "Orange", "Kiwi", "Melon", "Mango"]

# print(myList[2:5])

# The search will start at index 2 (included) and end at index 5 (not included)

# Check if Item Exists
# To determine if a specified item is present in a list use the "in" keyword:

if "Apple" in myList:
    print("Yes, 'Apple' is in the fruits list")
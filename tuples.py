# creating and munipulating lists and tuples
fruits = ["apples", "bananas", "pineapples"]
fruits.append("oranges")
print(fruits)

dimensions=["1456", "1980", "1222", "0000"]
dimensions.remove("0000")  #one can not work with item index here
dimensions_tuple = tuple(dimensions)
print(dimensions_tuple) 
print(dimensions_tuple[1]) 
# dimensions.insert(0, "2340")
# len(dimensions)
# dimensions.pop(1)
print(dimensions)
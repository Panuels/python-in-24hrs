# store key value pairs, working sets

phone_book = {"Alice": "123-456", "Bob":"789-101"}
print(phone_book["Alice"])

unique_numbers = {1,2,3,2,5,6,5,1} #set example
print(unique_numbers)

# Sample dictionary with numbers as values
data = {
    "item1": 10,
    "item2": 20,
    "item3": 30
}

# Editing a specific value
data["item1"] = 15  # Update value of item1

# Or if you want to add a number to each item
for key in data:
    data[key] += 5  # Increment each value by 5

print(data)

# empty dictionary
# dict1 = {}
# dict2 = dict()

# dict1_values = {
#     'key1': 'value1',
#     'key2': 'value2',
# }
# dict2_values = dict(key1='valu1', key2='value2')
# print(dict2_values)

# key can be immutable data type
dict = {1: 'value', (2, 3): 'tuple key'}
# print(dict[(2,3)])

# use .get() method
my_value = dict.get(1)

# my_value = dict['my_key']
my_value = dict.get('my_key')

# YOU DO - create a student dictionary with keys name and favorite_integer and print it.

favorite_animal = 'dog'


# if 'course' in student:
#     print(f"{student['name']} is enrolled in {student['course']}")
# else:
#     print(f"{student['name']} is not enrolled in a course")

student = {
    'name': 'Maria',
    'favorite_integer': 5,
    favorite_animal: 'llama'
}

# setting items
student['name'] = 'Mariana'

# add items
student['age'] = 25

# delete an item
del student['dog']

# see the number of items
len(student)

# items() show all items in dictionary
student.items()

# use items() in a for-in loop
# for key, val in student.items():
    # print(f"{key} is {val}")

# print(student.values())

where_my_things_are = {
    'coffee cup': 'on the desk',
    'hairbrush': 'at home',
    'denis': 'I dont know... outside?'
}

for thing, location in where_my_things_are.items():
    pass
    # print(f"{thing} is kept {location}")

# LISTS
list1 = []
list2 = list()

colors = ['red', 'green', 'blue']
dic = {
    'a': 'red',
    'b': 'green',
    'c': 'blue'
}
colors2 = list(dic.keys())

# replacing items
colors[-1] = 'brown'

# adding an item
colors.append('purple')

# add multiple items
colors.extend(['orange', 'black'])

# insert an item
colors.insert(1, 'yellow')

# print(colors)
# remove an item
banana = colors.pop(2)

# print(banana)

# remove specific item
colors.remove('orange')

# empty the entire list
# colors.clear()

# iterate over our list
# for color in colors:
#     print(color)

# for idx, color in enumerate(colors):
#     print(idx, color)


# TUPLE

colors = ('red', 'green', 'blue')

hello_tuple = 'Hello',

# can use index() method find specific values
blue_idx = colors.index('blue')
# print(blue_idx)

# iterate using enumrate
# for idx, color in enumerate(colors):
#     print(idx, color)

# for color in colors:
#     print(color)


# unpacking
r, banana, b = colors
print(r, banana, b)
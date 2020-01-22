"""
User Database Query
James
Julie
Steph
"""

users = ['James', 'Julie', 'Steph']

print(users)

users.insert(1, 'Anthony')

print(users)

users.append('Tom')

print(users)

print([users[2]])

users[4] = 'Gibson'

print(users)

#removing something from a list

users = ['Kristine', 'Tiffany', 'Jordan', 'Leann']

print(users)

users.remove('Jordan') # used when you know the item

print(users)

popped_user = users.pop() # used when you want to use the last item on the list and use it for something

print(popped_user)
print(users)

del users[0] # uesed when you want to delete item and you know the index

print(users)

# nested lists

users = ['Kristine', 'Tiffany', 'Jordan', 'Leann']

ids = [1, 2, 3, 4]

mixed_list = [42, 10.3, 'Altuve', users]

print(mixed_list)

user_list = mixed_list.pop()

print(user_list)
print(mixed_list)

nested_lists = [[123], [234], [345]]

# len() and index

tags = ['python', 'development', 'tutorials', 'code']

number_of_tags = len(tags)
last_item = tags[-1]
index_of_last_item = tags.index(last_item)

print(number_of_tags)
print(last_item)
print(index_of_last_item)

# join()   https://www.google.com/search?q=python+development+tutorial

uri = 'https://www.google.com/search?q='
tags = ['python', 'development', 'tutorial']
formatted_tags = '+'.join(tags)
query_uri = f'{uri}{formatted_tags}'

print(query_uri)

# ranges and slice
tags = [
  'python',
  'development',
  'tutorials',
  'code',
  'programming',
  'computer science'
]

tag_range = tags[1:-1:2]
tag_range = tags[::-1]

print(tag_range)

tags.sort(reverse=True)

print(tags)

# slice objects when you need to store it in a var and recall it multiple times later
tags = [
  'python',
  'development',
  'tutorials',
  'code',
  'programming',
]

print(tags[1:4:2]) #slice option 1

slice_obj = slice(1, 4, 2) #slice option 2 when you are wanting to store in var and recall later

print(slice_obj.start) # when you have a sliced list and want to know how it was sliced
print(slice_obj.stop)
print(slice_obj.step)

print(tags[slice_obj])

# add to a list

tags = ['python', 'development', 'tutorials', 'code']

# Nope
tags[-1] = 'Programming' # replaces -1 index value

# In Place
tags.extend('Programming') # separates programming into separate strings for each letter
tags.extend(['Programming']) # works but when you print this it comes back none

# New List
new_tags = tags + ['Programming'] # is usually the way to do this if you want to keep the original list intact

print(new_tags)

print(tags)
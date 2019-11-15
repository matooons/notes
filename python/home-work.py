# bob = 'ABCD'
# bob = bob.replace('ABCD', 'DBCA')
# print(bob)

# list = [1,2,3,4]
# sum = 0
# for num in list:
#     sum = sum + num
# print (sum)

# bab = 'restart'
# bab = 'resta'+'$'+'t'
# print(bab)

# import random
# r = lambda: random.randint(0,255)
# print('#%02X%02X%02X' % (r(),r(),r()))


#



# from functools import reduce

# """
# manual_exponent(2, 3)
# #>8

# manual_exponent(10, 2)
# #> 100

# def manual_exponent(num, exp)
   
# """


# def manual_exponent(num, exp):
#     counter = exp - 1
#     total = num 

#     while counter > 0:
#         total *= num
#         counter -= 1

#     return total

    
# def manual_exponent(num, exp):
#          computed = [num] * exp
#          return (reduce(lamba total, element: total * element, computed_list))


# print(manual_exponent(2, 3))
# print(manual_exponent(10, 2))





#





# """
# User Database Query
# Kristine
# Tiffany
# Jordan
# """

# users = ['Kristine', 'Tiffany', 'Jordan']

# print(users)

# users.insert(1, 'Anthony')

# print(users)

# users.append('Ian')

# print(users)

# print([users[2]])

# users[4] = 'Brayden'

# print(users)




#




# users = ['Kristine', 'Tiffany', 'Jordan', 'Leann']

# print(users)

# users.remove('Jordan')

# print(users)

# popped_user = users.pop()

# print(popped_user)
# print(users)

# del users[0]

# print(users)





#




# users = ['Kristine', 'Tiffany', 'Jordan', 'Leann']

# ids = [1, 2, 3, 4]

# mixed_list = [42, 10.3, 'Altuve', users]

# print(mixed_list)

# user_list = mixed_list.pop()

# print(user_list)
# print(mixed_list)

# nested_lists = [[123], [234], [345]]




#





# tags = ['python', 'development', 'tutorials', 'code']

# print(tags)

# tags.sort()

# print(tags)

# tags.sort(reverse=True)

# print(tags)

# totals = [234, 1, 543, 2345]

# totals.sort(reverse=True)

# print(totals)





#





# # https://www.google.com/search?q=python+development+tutorial

# uri = 'https://www.google.com/search?q='
# tags = ['python', 'development', 'tutorial']
# formatted_tags = '+'.join(tags)
# query_uri = f'{uri}{formatted_tags}'

# print(query_uri)






#





# # https://www.google.com/search?q=python+development+tutorial

# uri = 'https://www.google.com/search?q='
# tags = ['python', 'development', 'tutorial']
# formatted_tags = '+'.join(tags)
# query_uri = f'{uri}{formatted_tags}'

# print(query_uri)




#





# tags = ['python', 'development', 'tutorials', 'code']

# tag_range = tags[2:]
# tag_range = tags[0:2]
# tag_range = tags[:2]
# tag_range = tags[0:-1]

# print(tag_range)



#







# sale_prices = [
#   100,
#   83,
#   220,
#   40,
#   100,
#   400,
#   10,
#   1,
#   3
# ]

# sorted_list = sorted(sale_prices, reverse=True)

# print(sorted_list)
# print(sale_prices)




#




# import math

# """
# Tools:
# - math library
# - sorted function
# - list slicing
# - computations
# """

# sale_prices = [
#   100,
#   83,
#   220,
#   40,
#   100,
#   400,
#   10,
#   1,
#   3
# ]

# sorted_list = sorted(sale_prices)
# num_of_sales = len(sorted_list)
# half_slice = math.floor(num_of_sales/2)
# first_sales_items = sorted_list[:half_slice]
# last_sales_items = sorted_list[-(half_slice):]
# median = sorted_list[half_slice:(half_slice + 1)]

# print(sorted_list)
# print(num_of_sales)
# print(first_sales_items)
# print(last_sales_items)
# print(median)



#


# import math

# """
# Tools:
# - math library
# - sorted function
# - list slicing
# - computations
# """

# sale_prices = [
#   100,
#   83,
#   220,
#   40,
#   100,
#   400,
#   10,
#   1,
#   3
  
# ]

# sorted_list = sorted(sale_prices)
# num_of_sales = len(sorted_list)
# half_slice = math.floor(num_of_sales/2)
# first_sales_items = sorted_list[:half_slice]
# last_sales_items = sorted_list[-(half_slice):]
# median = sorted_list[half_slice:(half_slice + 1)]

# print(median)


# sorted_list = sorted(sale_prices)
# num_of_sales = len(sorted_list)
# half_slice = math.ceil(num_of_sales/2 - 1)
# first_sales_items = sorted_list[:half_slice]
# last_sales_items = sorted_list[-(half_slice):]
# median = sorted_list[half_slice:(half_slice + 1)]


# print(median)

# print(sorted_list)



#



# tags = [
#   'python',
#   'development',
#   'tutorials',
#   'code',
#   'programming',
# ]

# print(tags[1:4:2])

# slice_obj = slice(1, 4, 2)

# print(slice_obj.start)
# print(slice_obj.stop)
# print(slice_obj.step)

# print(tags[slice_obj])




#



# tags = ['python', 'development', 'tutorials', 'code']

# # Nope
# tags[-1] = 'Programming'

# # In Place
# tags.extend('Programming')
# tags.extend(['Programming'])

# # New List
# new_tags = tags + ['Programming']

# print(new_tags)

# print(tags)



#



# teams = {
#   "astros": ["Altuve", "Correa", "Bregman"],
#   "angels": ["Trout", "Pujols"],
#   "yankees": ["Judge", "Stanton"],
# }

# astros = teams['astros']
# print(astros)
# print(teams['angels'])
# print(teams['yankees'])



#


# teams = {
#   "astros": ["Altuve", "Correa", "Bregman"],
#   "angels": ["Trout", "Pujols"],
#   "yankees": ["Judge", "Stanton"],
# }

# teams['red sox'] = ['Price', 'Betts']

# print(teams)


#


# teams = {
#   "astros": ["Altuve", "Correa", "Bregman"],
#   "angels": ["Trout", "Pujols"],
#   "yankees": ["Judge", "Stanton"],
# }

# teams['red sox'] = ['Price', 'Betts']
# bob = sorted(teams)
# print(bob)


#



# teams = {
#   "astros": ["Altuve", "Correa", "Bregman"],
#   "angels": ["Trout", "Pujols"],
#   "yankees": ["Judge", "Stanton"],
#   "red sox": ['Price', 'Betts'],
# }

# featured_team = teams.get('red sox', 'No featured team')

# print(featured_team)



#


# players = {
#   "ss" : "Correa",
#   "2b" : "Altuve",
#   "3b" : "Bregman",
#   "DH" : "Gattis",
#   "OF" : "Springer",
# }

# player_names = list(players.copy().values())

# teams = {
#   "astros" : ["Altuve", "Correa", "Bregman"],
#   "angels":  ["Trout", "Pujols"],
#   "yankees": ["Judge", "Stanton"],
#   "red sox": ["Price", "Betts"],
# }

# team_groupings = teams.items()

# """
# [
#   ('astros', ['Altuve', 'Correa', 'Bregman']),
#   ('angels', ['Trout', 'Pujols']),
#   ('yankees', ['Judge', 'Stanton']),
#   ('red sox', ['Price', 'Betts'])
# ]
# """

# print(list(team_groupings)[1][1][0])


#



# teams = {
#   "astros" : ["Altuve", "Correa", "Bregman"],
#   "angels":  ["Trout", "Pujols"],
#   "yankees": ["Judge", "Stanton"],
#   "red sox": ["Price", "Betts"],
# }

# del teams['angels']
# removed_team = teams.pop('mets', 'Team not found')


# print(teams)
# print(removed_team)



#


# teams = [
#   {
#     'astros': {
#       '2B': 'Altuve',
#       'SS': 'Correa',
#       '3B': 'Bregman',
#     }
#   },
#   {
#     'angels': {
#       'OF': 'Trout',
#       'DH': 'Pujols',
#     }
#   }
# ]

# # print(teams[0])

# angels = teams[1].get('angels', 'Team not found')

# print(list(angels.values())[1])



#


# """
# g $$$$$$$$$$$$$$$$$$$$
# f $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# t $$$$$$$$$$
# o $$$$$$$$$$$$
# """

# sales = {
#   'google': 20,
#   'facebook': 42,
#   'twitter': 10,
#   'offline': 12,
# }

# print('g ' + sales['google'] * '$')
# print('f ' + sales['facebook'] * '$')
# print('t ' + sales['twitter'] * '$')
# print('o ' + sales['offline'] * '$')




#



# # List: []
# # Dictionary: {}
# # Tuple: ()

# # Tuple: immutable 
# # List: mutable

# post = ('Python Basics', 'Intro guide to python', 'Some cool python content')

# # Tuple unpacking
# title, sub_heading, content = post

# # Equivalent to Tuple unpacking
# # title = post[0]
# # sub_heading = post[1]
# # content = post[2]

# print(title)
# print(sub_heading)
# print(content)



#



# post = ('Python Basics', 'Intro guide to python', 'Some cool python content')

# print(id(post))
# print(id(post))

# post += ('published',)

# print(id(post))

# title, sub_heading, content, status = post

# print(title)
# print(sub_heading)
# print(content)
# print(status)


#


# post = ('Pyrthon Basics', 'Intro to Python', 'something cool')

# tags = ['python', 'coding', 'tutorial']

# post += (tags,)

# print(post[-1][1])



# def number():

#     numbers = []

#     num = 1

#     while num <= 20:
#         numbers.append(num)
#         num += 1 

#         for numdr in numbers:
#             if number is [3, 9, 14]:
#                 del numbers[numbers.]



#                                                                          hello  name




# def name(first_name, last_name):

#     tim = "hello " + first_name + " your fother Mr." + last_name + " is missing"

#     print(tim)

# name('matthew', 'lebaron')

# """
# [
#     [0, 1, 2, 3, 4],
#     [1, 2, 3, 4, 5],
#     [2, 3, 4, 5, 6],
#     [3, 4, 5, 6, 7],
#     [4, 5, 6, 7, 8],
# ]
# """

# def manual_incrementing_matrix(n):
#     matrix = [ [ None for y in range(n) ] for x in range(n) ]

#     counter = 0

#     for idx, el in enumerate(matrix):
#         for nested_idx, nested_el in enumerate(el):
#             matrix[idx][nested_idx] = counter + nested_idx

#         counter += 1

#     return matrix

# print(manual_incrementing_matrix(5))









# sentence = 'The quick brown fox jumped'
# sentence -> variable
# 'The quick brown fox jumped' -> string
# = -> assignment

# sentence = 'The quick brown fox jumped'
# sentence_two = sentence.upper()

# print(sentence)
# print(sentence_two)

# sentence = 'the quick brown fox jumped'.capitalize()
# print(sentence)

# sentence = 'the quick brown fox jumped'.title()
# print(sentence)

# sentence = 'the Quick Brown fOx jumped'
# print(sentence.lower())



#




# priority_index = {
#     (1, 'premier'): [1, 34, 12],
#     (1, 'mvp'): [84, 22, 24],
#     (2, 'standard'): [53, 42, 24],
# }

# print(list(priority_index.keys()))



#                                                                                                                      how to zip code


# position = ['sb', '3b', 'ss', 'dh']
# players = ['altuve', 'bob', 'sam', 'tim']

# scoreboard = zip(position, players)

# print(list(scoreboard))




#                                                                                                                        what the in function




# tags = {
#     'python',
#     'coding',
#     'tutorials',
#     'coding'
# }


# print(tags)


# query_one = 'python' in tags
# query_two = 'ruby' in tags

# print(query_one)
# print(query_two)





#                                                                                                     merging python sets


# tags_one = {
#     'python',
#     'coding',
#     'tutorials',
#     'coding'
# }

# tags_two = {
#     'ruby',
#     'coding',
#     'tutorials',
#     'development'
# }


# #merged tags

# # merged_tags = tags_one | tags_two
# # print(merged_tags)

# #tags in tags_one but not in tags_two
# exclusive_to_tag_one = tags_one - tags_two
# print(exclusive_to_tag_one)

# # tags found in both one and two

# universal_tags = tags_one & tags_two 


#                                                                         loops in python                                 for in loops                 and               while loops   



# players = ['altuve', 'bregman', 'correa', 'gattis']

# for player in players:
#     print(player)


# players = {
#     '2b': 'altuve',
#     '3b': 'bregman',
#     'ss': 'correa',
#     'dh': 'gattis'
# }

# for position, player in players.items():
#     print('Position', position)
#     print('Player Name', player)



#                                                                                                 looping ranges in python                           Range  (1, 10)



# for num in range(1, 11, 2):
#     print(num)

# for bob in range(1, 11):
#     print(bob)


  #                                                                                                how to break in python loops 


# usernames = [
#     'jo',
#     'ty',
#     'th',
#     'ce',
#     'sa'
# ]

# # for username in usernames:
# #     if username == 'ce':
# #         print(f'sorry, {username}, you are not allowed')
# #         continue
# #     else:
# #         print(f'{username} is allowed')


# for username in usernames:
#     if username == 'ce':
#         print(f'{username} was found at index {usernames.index(username)}')
#         break
#     print(username)


#                                                                                                     While loops in python (Overview)


# nums = list(range(1, 100))

# while len(nums) > 0:
#     print(nums.pop())


# def guessing_game():
#     while True:
#         print('what is your guess?')
#         guess = input()

#         if guess == '42':
#             print('you corectly guessed it!')
#             return False
#         else:
#             print(f'no, {guess} is not the answer, pleas try again\n')


# guessing_game()



#                                                                                                               how comdine flaten list with loops




# legacy_customers = ['alice', 'bob']
# new_customers = ['tiffany', 'kristine']

# raw_db = [legacy_customers, new_customers]

# print(raw_db)


# for legacy_customer in legacy_customers:
#     new_customers.append(legacy_customer)


# print(new_customers)


#                                                                                     mesing around


# def penis(length):
#     penis = [
#     "8" 
#     ]

#     boner = "="

#     counter = 0

#     while counter <= length:
#         penis.append(boner)
#         counter += 1

#     penis.append("D")

#     penis_string = "".join(penis)

#     print(penis_string)

# penis(int(input(f"How long is yo dick?\n")))




#                                                                                      list compryhention in python



# num_list = range(1, 11)
# # cubed_nums = []

# # for num in num_list:
# #     cubed_nums.apend(num ** 3)


# # cubed_nums = [num ** 3 for num in num_list]


# # even_numbers = []

# # for num in num_list:
# #     if num % 2 == 0:
# #         even_numbers.append(num)


# even_numbers = [num for num in num_list if num % 2 == ]

# print(list(num_list))


# # print(cubed_nums)
# print(even_numbers)




#                                                                                   bild html heading genarator in python                        how to make un h1 tag

#   heading_generator(title, heading_generator)
#   heading_generator('greeting', '1')
#   <h1>greating</h1>

#   heading_generator('hi there', '3')
#   <h3>hi there</h3>

# def heading_generator(title, heading_type):
#     return f'<h{heading_type}>{title}</h{heading_type}>'
      
# print(heading_generator('greeting', '1'))

# print(heading_generator('hi there', '3'))
     


 #                                                                                                      section introduction

# def heading_generator(title):

#     return(title)


# print(heading_generator('rafael'))



#                                                                                                                          age restrictions


# age = 25 

# if age < 25:
#     print(f"I'm sorry, you need to be at least 25 years old")
# elif age > 100:
#        print(f"I'm sorry,you are to old to rent a car")
# else:
#   print(f"you're good to go, {age} fits in the range to rent a car.")


#                                                                                             full list of python conditionals                                                                                                 



# # role = 'admin'

# # auth = 'can access' if role == 'admin' else 'connect access'

# # print(auth)

# role = 'admin'

# if role == 'admin':
#     auth = 'can access'
# else:
#     auth = 'cannot access'

# print(auth)

# username = 'jonsnow'

# if username != 'jonsnow':
#     print('welcome')
# else:
#     print('you shall not pass!')


# age = 55'

# if age < 10:
#     print('welcome')
# else:
#     print('you shall not pass!')


# user_list = ['kris', 'tiff']
# second_list = ['kris', 'tiff']

# if user_list == second_list:
#     print('they match')



#                                                                                How to Check if a Value is Included in a Python String or List



# sentence = 'The quick brown fox jumped over the lazy Dog'
# word = 'dog'

# if word.lower() in sentence.lower():
#   print('The word is in the sentence')
# else:
#   print('The word is not in the sentence')


# nums = [1, 2, 3, 4]

# if 3 in nums:
#   print('The number was found')
# else:
#   print('The number was not found')



#                                                                                        How to Build Compound Conditionals in Python       sighn in   email or name and password


# username = 'jonsnow'
# email = 'jon@snow.com'
# password = 'thenorth'

# if username == 'jonsnow' and password == 'thenorth':
#   print('Access permitted')
# else:
#   print('Not allowed')


# if (username == 'jonsnow' or email == 'jon@snow.com') and password == 'thenorth':
#   print('Access permitted')
# else:
#   print('Not allowed')


# if username == 'jonsnow' or password == 'thenorth':
#   print('Access permitted')
# else:
#   print('Not allowed')


# logged_in = True
# standard_user = False

# if logged_in and not standard_user:
#   print('You can access the admin dashboard')
# else:
#   print('You can only access the standard dashboard')



#                                                                                 basic syntax for creating python functions



# def full_name(first, last):
#     print(f'{first} {last}')


# full_name('matthew', 'lebaron')


# def auth(email, password):
#     if email == 'me@home.com' and password =='secret':
#         print('yes')
#     else:
#         print('not yes')
        

# auth('me@home.com', 'secret')

# def hundred(max):
#     for num in rangr(1, max):
#         print(num)


# hundred(max) 




# def full_name(first, last):
#     print(f'{first} {last}')


# full_name('matthew', 'lebaron')




#                                                                                                 what does it maen to return a value from a python function?





# def full_name(first, last):
#   return f'{first} {last}'


# kristine = full_name('Kristine', 'Hudgens')

# def greeting(name):
#   print(f'Hi {name}!')


# greeting(kristine)





#                                                                                                                      How to Nest Functions in Parent Functions in Python




   


# def greeting(first, last):
#   def full_name():
#     return f'{first} {last}'

#   print(f'Hi {full_name()}!')


# greeting('Kristine', 'Hudgens')




#                                                                                                               guide to default arguments in python functios





# def greeting(name = 'Guest'):
#   print(f'Hi {name}!')

# greeting()
# greeting('Kristine')

#                                         Nope

# def some_function(collection = []):
#   collection.append(1)
#   print(id(collection))
#   return collection

# #                                      other part of program

# print(some_function())
# print(some_function())




#                                                                                              how to utilize named function arguments in python



# def full_name(first, last):
#   print(f'{first} {last}')


# full_name('Kristine', 'Hudgens')
# full_name(first = 'Kristine', last = 'Hudgens')
# full_name(last = 'Hudgens', first = 'Kristine')





#                                                                                        guide to funtion argument unpacking in python




# def greeting(*args):
#   print('Hi ' + ' '.join(args))


# greeting('Kristine', 'M', 'Hudgens')
# greeting('Tiffany', 'Hudgens')


# def greeting(*names):
#   print('Hi ' + ' '.join(names))


# greeting('Kristine', 'M', 'Hudgens')
# greeting('Tiffany', 'Hudgens')


# def greeting(time_of_day, *args):
#   print(f"Hi {' '.join(args)}, I hope that you're having a good {time_of_day}")


# greeting('Afternoon', 'Kristine', 'M', 'Hudgens')
# greeting('Morning', 'Tiffany', 'Hudgens')





#                                                                                            Overview of Keyword Arguments in Python Functions




# def greeting(**kwargs):
#   print(kwargs)


# greeting()
# greeting(first = 'Kristine', last = 'Hudgens')






# def greeting(**kwargs):
#   if kwargs:
#     print(f"Hi {kwargs['first']} {kwargs['last']}, have a great day!")
#   else:
#     print('Hi Guest!')


# greeting()
# greeting(first = 'Kristine', last = 'Hudgens')




#                                                                                                  How to Combine All Argument Types in a Single Python Function



# def greeting(time_of_day, *args, **kwargs):
#   print(f"Hi {' '.join(args)}, I hope that you're having a good {time_of_day}.")

#   if kwargs:
#     print('Your tasks for the day are:')
#     for key, val in kwargs.items():
#       print(f'{key} -> {val}')


# greeting('Morning',
#          'Kristine', 'Hudgens',
#          first = 'Empty dishwasher',
#          second = 'Take pupper out',
#          third = 'math homework')




#                                                                                                  Guide to Python Lambdas



# full_name = lambda first, last: f'{first} {last}'


# def greeting(name):
#     print(f'hi there {name}')


# greeting(full_name('kris', 'hug'))



#                                                                                                                   remove the first and last eliment from a python list                                                                             


# # remove_first_and_last(list_to_clean)

# # html = ['<h1>', 'content', '</h1']

# # remove_first_and_last(html)
# # => ['some content']

# # html = ['<h1>', 'content', 'more', '</h1']

# remove_first_and_last(html_2)
# => ['content', 'more']


# # def remove_first_and_last(clean):

# # one, *two, three = [1, 2, 3, 4, 5]



# def remove_first_and_last(clean):
#   _, *content, _ = clean
#   return content

# html = ['<h1>', 'content', 'more', '</h1>']

# print(remove_first_and_last(html_2))



#                                                                                          How to Create a Custom Module and Import It In the Python Repl





























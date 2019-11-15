#content = """
#Nullam id dolor id nibh ultricies vehicula ut id elit. Nullam quis risus eget urna mollis ornare vel eu leo.

#Vestibulum id ligula porta felis euismod semper. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Cras justo odio, dapibus ac facilisis in.

#Integer posuere erat a ante venenatis dapibus posuere velit aliquet.
#"""

#print(repr(content))

#long_string = '\nNullam id dolor id nibh ultricies vehicula ut id elit. Nullam quis risus eget urna mollis ornare vel eu leo.\n\nVestibulum id ligula porta felis euismod semper. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Cras justo odio, dapibus ac facilisis in.\n\nInteger posuere erat a ante venenatis dapibus posuere velit aliquet.\n'

#print(long_string)



#



#sentence  = 'the quick brown fox jumped'
#sentence -> variable
#'the quick brown fox jumped' -> string

#=-> assignment
#sentence_two = sentence.upper()

#sentence = 'the quick brown fox jumped'.capitalize()
#print(sentence)

#sentence = 'the quick brown fox jumped'.title()
#print(sentence)

#sentence = 'the quick bRown Fox juMped'.lower()
#print(sentence)

# T => 0
# h => 1
# e => 2
# ' '=>3

#starter_sentance = 'The quick brown fox jumped'
 
#new_sentence = 'thy'+' quick brown fox jumped'
#print(new_sentence)

#new_sentence = 'thy'+ starter_sentance[3:]
#print(new_sentence)


#                                                                                      How to Use Python's format method to Implement Index Based String Interpolation


#name = 'Kristine'
#age = 12
#product = 'Python eLearning course'
#from_account = 'Jordan'

#greeting = "Product Purchase: {2} - Hi {0}, you are listed as {1} years old. - {3}".format(name, age, product, 'Jordan')

#greeting = f"Product Purchase: {product} - Hi {name}, you are listed as {age} years old. - {from_account}"

#print(greeting)

 #                                                                                    Finding a Substring in Python with: Find, Index, and In         


#sentence = 'The quick brown fox jumped over the lazy dog.'

#query = sentence.find('oops')
#query_two = sentence.index('oops')

#print(query)
#print(query_two)

#query = 'oops' in sentence

#print(query)


#                                                                             Using a Negative Index with a Python String


#sentence = 'my old dog.'

#sentence = sentence.replace('old', 'old lazy')

#print(sentence[-9:])


#


#url = 'https://google.com'

#url = url.rstrip('.com')
#url = url.lstrip('https://')
#url = url.capitalize()
#print(url)


#



#heading = "Python: An Introduction, and Python: Advanced"

#header, _, subheader = heading.partition(': ')

#print(header)
#print(subheader)

#first, second, third = heading.partition(': ')

#print(first)
#print(second)
#p#rint(third)



# 




#heading = "Python: An Introduction, and python: Advanced"

#header, _, subheader = heading.partition(': ')

#print(header)
#print(subheader)

#tags ='pythn,coding,programing,development'

#list_of_tags = tags.split(',')

#print(list_of_tags)


#list_of_tags = tags.split()

#print(list_of_tags)

#heading = "python: An Introduction"

#heading_list = heading.split(': ')

#print(heading_list)



#



#api_data = '5'
#greeting = 'Hithere' #no  space. if space False

#print(api_data.isalpha())
#print(greeting.isalpha())

#print(api_data.isnumeric())
#print(greeting.isnumeric())



#



# product_id = 420
# sale_price = 14.99
# tip_percentage = 1/5
# new_product = 150


# print(product_id)
# print(sale_price)
# print(tip_percentage)


# print(sale_price + new_product)
# print(product_id + new_product)




#






# print('Addition')
# print(100 + 42)

# print('Subtraction')
# print(100 - 42)

# print('Division')
# print(100 / 42)
# print(100 / 38)

# print('Floor Division')
# print(100 // 42)
# print(100 // 38)

# print('Multiplication')
# print(100 * 42)

# print('Modulus')
# print(100 % 42)

# print('Exponents')
# print(100 ** 42)


# calculation = 8 + 2 * 5 - (9 + 2) ** 2

# print(calculation)




# total = 100

# total = total + 10
# total += 10
# total -= 10
# total *= 2
# total /= 10
# total //= 10
# total **= 2
# total %= 2

# product_two = 120
# product_three = 10

# total += product_two
# total += product_three

# print(total)





#




# product_cost = 88.80
# commission_rate = 0.08
# qty = 450

# print(int(product_cost))
# print(float(qty))
# print(Decimal(product_cost))
# print(complex(commission_rate))
#A lambda function in Python is a simple, anonymous function that is defined without a name

# lambda argument(s): expression
# A lambda function can have multiple arguments but only 
# one expression, and is usually contained within one line of code

add_two = lambda x: x + 2
print(add_two(5))

square = lambda x: x * x
print(square(5))

len_str = lambda s: len(s)
print(len_str("Hello, world!"))

even = lambda n: n % 2 == 0
print(even(4))

sort_asc = lambda l: sorted(l)
print(sort_asc([1, 5, 3, 2, 4]))

even_numbers = lambda l: [x for x in l if x % 2 == 0]
print(even_numbers([1, 2, 3, 4, 5]))


#Lambda functions are typically used in the following scenarios:
#1 When we want to write a quick function with one line
#2 When we want to combine with other built-in functions such as map(), filter(), and apply() to filter for data

# import pandas as pd
 
# df = pd.DataFrame({
#    'name': ['Amy', 'Jackie', 'Sue'],
#    'grades': [90, 84, 76]
# })
 
# # use the lambda function to multiply bump up the values in the grades column by 1.2!
# df['grades'] = df['grades'].apply(lambda x: x * 1.2)

# print(df)
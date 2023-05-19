# print("Let's multiply numbers! \n")
# number_1=int(input("Please enter the first number: "))
# number_2=int(input("Please enter the second number: "))

# def multiple(x,y):
#     try: 
#         result = x * y
#         print(result)
#     except:
#         print("One of the inputs is not a number.")
#     finally:
#         print("See you again!")

    
# multiple(number_1,number_2) 


print("Let's multiply numbers! \n")

while True:
    number_1 = input("Please enter the first number: ")
    if number_1.isdigit():
        number_1=int(number_1)
        break
    print("Please enter a valid number.")

print(number_1)
print(type(number_1))
while True:
    number_2 = input("Please enter the second number: ")
    if number_2.isdigit():
        number_2=int(number_2)
        break
    print("Please enter a valid number.")
print(number_2)
print(type(number_2))

print(number_1*number_2)

def multiple(x, y):
    try:
        result = x * y
        print(result)
    except:
        print("One of the inputs is not a number.")
    finally:
        print("See you again!")

multiple(number_1, number_2)
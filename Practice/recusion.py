def factorial(num):
   if num == 1:
       return 1
   else:
       return num * factorial(num-1) #this will go on and on
   
print(factorial(3))

#The above function factorial is a recursive function because it calls 
# itself within the function. A recursive function contains 
# two parts: recursive step and base case.

def factorial(num):
   call_stack = []
   if num == 1:
       print('base case reached! Num is 1.')
       return 1
   else:
       call_stack.append({'input': num})
       print('call stack: ', call_stack)
       return num * factorial(num-1)
 
factorial(5)
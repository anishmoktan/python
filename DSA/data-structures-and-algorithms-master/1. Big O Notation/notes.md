#Big O Notation

Complexity Analysis
One problem can have multiple solutions but they all may not be equal in terms of time and memory usage.

How to define good code?
Run Fast
Require Less Memory
Readable Gives Correct Output

Readable
Scalable: Time and Space dependent 

Time Complexity: 
Amount of time it takes to run an algorithm.
Algorithm runs fast, better time complexity. 

Space Complexity: 
Amount of extra space out algorithm requires. 
Algorithm takes less space, better space complexity

Big O Notation: performance parameter that helps us determine the rating of our code base, in terms of time and space complexity.

Definition:

Big O notation is used in Computer Science to describe the performance or complexity of an algorithm. Big O is used to describe the excution time required or the space used (e.g. in memory of on disk) by an algorithm.

To measure the efficiency of an algorithm, we nee dto consider two things:
Time Complexity: How much time does it take to run completely?
Space Complexity: How much extra space does it require in the process?

### 7. Why we need Big O Notation?
Speed of program running is different in separate devices and hardware
We cannot rate the code on the time it takes to run

Why we need Big O?
We require BIG O to give a performance to our program for time and space
We cannot depend on our system clock time as well as hardware for each program

It doesn't depend on time, as it depends on how many steps we are performing
The main focus is to calculate the amount of work we do or the number of comparisons we perform

### 8. Big O(n) Complexity

An algorithm with a Big O(n) time complexity is said to be **linear**. This means that the running time of the algorithm is directly proportional to the size of the input. For example, if an algorithm takes 1 second to sort a list of 10 items, it will take 2 seconds to sort a list of 20 items, and so on.


E.x. 

```
def print_numbers(n):
    for i in range(n):
        print(i)
```

As n increases, the output of number increases linearly:
n=5 will output 5 outputs
n=6 will output 6 outputs

Solution A = 10 Operations
Solution B = 5 Operations ---> Better code as it has less operations

https://www.bigocheatsheet.com/

Liner Big(n) Example:

```
student_list1 = ['tim', 'drake', 'ashish', 'shubham']

student_list2 = ['andrew', 'harshit', 'lary', 'shubham', 'chris']

def checkStudent(student_list2):
    for student in student_list2:
        if student == 'chris':
            print('Available')

checkStudent(student_list2) 
```

#### Big O(1) Complexity
An algorithm with a Big O(1) time complexity is said to be **constant**. This means that the running time of the algorithm is independent of the size of the input. For example, if an algorithm takes 1 millisecond to sort a list of 10 items, it will also take 1 millisecond to sort a list of 100 items, and so on.


```
student_list = ['andrew', 'akshat', 'chris', 'harshit', 'lary', 'shubham', 'tim', 'drake', 'ashish']

def displayStudent(student_list):
    print(student_list[0]) #O(1)
    print(student_list[1]) #O(1)

displayStudent(student_list) #O(2)
```

We don't use big O(2), we say big O(1) which signals constant

### 9. Counting Operations
 
```
students = ['andrew', 'akshat', 'chris', 'harshit', 'lary', 'tim', 'drake', 'ashish', 'shubham'] #O(1)

def rondomFunction(students):
    first = students[0] #O(1)
    total = 0 #O(1) 
    new_list = [] #O(1)

    for student in students:
        total += 1 #O(n)
        new_list.append(student) #O(n)
    
    print(new_list) #O(1)   
    return total #O(1)

print(rondomFunction(students)) # O(6 +2n) => O(n)
```

### 11. Simplifying Big O - Part 1

**Rule 1** - Focus on Scalability 
**Rule 2** - Considering Worst Case Scenario
**Rule 3** - Remove all possible constants
**Rule 4** - Consider different variable for different inputs
**Rule 5** - Remove all non-dominants

### 12. Big O(n^2) Complexity

An algorithm with a Big O(n^2) time complexity is said to be quadratic. This means that the running time of the algorithm is proportional to the square of the size of the input. For example, if an algorithm takes 1 second to sort a list of 10 items, it will take 4 seconds to sort a list of 20 items, and so on.

Some examples of algorithms with different Big O time complexities:

Bubble sort: O(n^2)
Selection sort: O(n^2)
Insertion sort: O(n^2)
Big O time complexity of an algorithm can vary greatly so it is important to choose the most efficient algorithm for a given task, as this can have a significant impact on the performance of a program.

Additional details about Big O(n^2) time complexity:

Algorithms with Big O(n^2) time complexity are often called "quadratic time" algorithms.
Algorithms with Big O(n^2) time complexity are often less efficient than algorithms with other time complexities.
Algorithms with Big O(n^2) time complexity should be avoided when possible.

Example
```
num_list = [1, 2, 3, 4, 5, 6, 7]
def rondomFunction(num_list):
    total = 0

    for num1 in num_list:
        for num2 in num_list:
            print(num1, num2)
            total += 1
    
    return total

print(rondomFunction(num_list))
```
This will run 49 times (7*7) so it is n^2

### 15. Space Complexity

Space Complexity of an algorithm represents the amount of extra memory space needed by the algorithm in its life cycle

We usually have 2 type of space requirement:
1. To store our input data
2. Extra space that we need to execute our program

How much additional memory do we need to allocate in order to run our code?

```
def all_cubes(items):
    result = []

    for item in items:
        result.append(pow(item,3)) #O(n)

    print(result)

items = [2,3,4,5,6,7]
all_cubes(items)
```
This example has space complexity of O(n), as the numbers in items list increase, there will be a linear increase in the result array.
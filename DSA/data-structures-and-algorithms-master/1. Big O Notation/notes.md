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

7. Why we need Big O Notation?
Speed of program running is different in separate devices and hardware
We cannot rate the code on the time it takes to run

Why we need Big O?
We require BIG O to give a performance to our program for time and space
We cannot depend on our system clock time as well as hardware for each program

It doesn't depend on time, as it depends on how many steps we are performing
The main focus is to calculate the amount of work we do or the number of comparisons we perform

8. Big O(n) Complexity

E.x. 
Solution A = 10 Operations
Solution B = 5 Operations ---> Better code as it has less operations

https://www.bigocheatsheet.com/

Liner Big(n) Example:

student_list1 = ['tim', 'drake', 'ashish', 'shubham']

student_list2 = ['andrew', 'harshit', 'lary', 'shubham', 'chris']

def checkStudent(student_list2):
    for student in student_list2:
        if student == 'chris':
            print('Available')

checkStudent(student_list2) 


#file=open("/Users/anishtamang/Personal_Projects/Python/Google_Courses/Using_Python_to_Interact_with_OS/Week_2/hello.txt")

# print(file.read())

# file.close()

with open("/Users/anishtamang/Personal_Projects/Python/Google_Courses/Using_Python_to_Interact_with_OS/Week_2/hello.txt") as file:
    print(file.read())
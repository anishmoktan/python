score = int(input("What did you score on your exam?"))
print(type(score))

def letter_grade_conversion(score):
    if score >= 90:
        print("Your grade is an A")
        letter_grade = "A"
    elif score >= 85:
        print("Your grade is a B")
        letter_grade = "B"
    elif score >= 75:
        print("Your grade is a C")
        letter_grade = "C"
    else:
        print("You failed!")
        letter_grade = "F"

    return letter_grade

print(letter_grade_conversion(score))
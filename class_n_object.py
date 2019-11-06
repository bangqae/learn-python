# Classes & Objects, Learn Python - Full Course for Beginners [Tutorial]
# Classes & Object for define complex data type, example = phone, student
# Class is defining what student is
# Object is an actual student
from student import Student  # File name and Class name

student1 = Student("Jim", "Business", 3.1)  # This parameter goes to class function
student2 = Student("Dante", "Blacksmith", 2.5)

print(student2.gpa)  # Calling attribute from class

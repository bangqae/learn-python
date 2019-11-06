# Reading Files, Learn Python - Full Course for Beginners [Tutorial]
# r = read, w = write (rewrite), a = append (add), r+ = r & w
employee_file = open("employees.txt", "r")  # open function
for employee in employee_file.readlines():
    print(employee)


# ------------------------------------------
# print(employee_file.readlines()[0])
# print(employee_file.read())
# print(employee_file.readline())
# print(employee_file.readable())

employee_file.close()  # always close after open it

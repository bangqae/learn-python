# Writing to Files, Learn Python - Full Course for Beginners [Tutorial]
employee_file = open("index.html", "w")  # if file don't exist, it creates a new one

employee_file.write("<p>This is html</p>")

# -----------------------------------------
# employee_file = open("employees.txt", "a")

# employee_file.write("\nKenn - Customer Service")

employee_file.close()

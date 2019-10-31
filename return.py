# Return, Learn Python - Full Course for Beginners [Tutorial]
def cube(num):  # Cube function
    return num*num*num  # Using return


value = input("Pangkat 3 dari : ")  # Input value
result = cube(int(value))  # Using cube function
print("Adalah : " + str(result))  # Int can't be print along with str

# If Statements, Learn Python - Full Course for Beginners [Tutorial]
is_male = True
is_tall = 1  # 0 is false, any else number is true, even minus

if is_male and is_tall:
    print("You are a tall male")
elif is_male and not is_tall:
    print("You are a short male")
elif not is_male and is_tall:
    print("You are a tall female")
elif not is_male and not is_tall:
    print("You are a short female")
else:
    print("Err")

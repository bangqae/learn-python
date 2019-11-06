import random

feet_in_mile = 5280  # 5 tomato
meters_in_kilometer = 1000
turtles = ["Leonardo", "Michelangelo", "Raphael", "Donatello"]


def get_file_ext(filename):  # Get file extension
    return filename[filename.index(".") + 1:]


def roll_dice(num):  # Random number
    return random.randint(1, num)
# Always add 2 enter before write function

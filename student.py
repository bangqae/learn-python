class Student:  # Class name
    def __init__(self, name, major, gpa):  # Parameter
        self.name = name  # Pass the parameter to an actual attribute
        self.major = major
        self.gpa = gpa
        # self.in_on_probation = is_on_probation

    def on_honor_roll(self):
        if self.gpa >= 3.5:
            return True
        else:
            return False

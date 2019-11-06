from Chef import Chef


class ChineseChef(Chef):  # Inherit Chef class to ChineseChef class

    def make_special_dish(self):  # Changes this method
        print("The chef makes orange chicken")

    def make_fried_rice(self):
        print("The chef makes fried rice")

# So ChineseChef have all Chef method
# But still able to changes method if he wants to

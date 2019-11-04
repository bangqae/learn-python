# Translator, Learn Python - Full Course for Beginners [Tutorial]
def translate(phrase):  # Function to change vowels to "g"
    translation = ""  # Variable for store the return value
    for letter in phrase:  # For every index in phrase do...
        if letter.lower() in "aiueo":  # If it's vowels do...
            if letter.isupper():  # Check if it's uppercase
                translation = translation + "G"  # "" + "G"
            else:
                translation = translation + "g"  # "" + "g"
        else:
            translation = translation + letter  # "" + other non vowels letter
    return translation  # Return value


print(translate(input("Enter a phrase : ")))  # Input value store in phrase

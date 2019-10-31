# Guessing Game, Learn Python - Full Course for Beginners [Tutorial]
secret_word = "giraffe"  # Word to guess
guess = ""  # Input
# guess_count = 0
guess_limit = 3  # Chance to try
out_of_guesses = False  # As long as this false, you can win

while guess != secret_word and not out_of_guesses:
    if guess_limit > 0:
        guess = input("Enter guess: ")
        if guess != secret_word:
            guess_limit -= 1
            print("Wrong!")
            if guess_limit > 0:
                print(str(guess_limit) + " more try!")
    else:
        out_of_guesses = True

if not out_of_guesses:  # if out_of_guesses == false
    print("You win!")
else:
    print("You lose!")

# in this game we have a secret word and we want the user to guess this word
# there is a limit of number of guesses

secret_word = "Mohammed"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_word and not out_of_guesses:
    if guess_count < guess_limit:
        guess = input("enter guess: ")
        guess_count+=1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("you lose out of guesses")
else:
    print("you win")


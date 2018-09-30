print("Welcome to the 'It's Six' guessing game!"  #start with the rules of the game
      "\nThe rules:"
      "\n   1)Pick a number from 1-10 for the other player to guess."
      "\n   2)Let the other player make up to 3 different guesses to get your number."
      "\nPayouts:"
      "\n   If the Guesser doesn't get the Picker's number: "
      "\n       The Guesser owes the Picker $3 if the Picker's number is even, or $4 if the number is odd."
      "\n   If the Guesser gets the Picker's number:"
      "\n       The Picker owes the Guesser $10 if it was the first guess, $8 if it was the second guess,"
      "\n       and neither is owed anything for this round if it was the third guess."
      "\nLets begin!")


def get_pick_number(x, y):  #
    pick_number = 0
    while pick_number < x or pick_number > y:  # have the player pick a number from min to max
        try:
            pick_number = int(input("Pick a number from 1 to 10 {inclusive) for the other player to guess."))
            if pick_number < x or pick_number > y:
                print("That wasn't a valid pick.")
        except ValueError:
            print("That wasn't a valid pick.")

    return pick_number


def get_guess_number(x, y, instance):
    guess_number = 0
    while guess_number < x or guess_number > y:  # have player two make a guess
        try:
            guess_number = int(input(f"Guess a number from 1 to 10 ({instance} guess)."))
            if guess_number < x or guess_number > y:
                print("That wasn't a valid guess.")
        except ValueError:
            print("That wasn't a valid guess.")

    return guess_number


def compare_numbers(pick, guess):  # see if the guess is correct
    if pick == guess:
        print("You guessed it!")
        return True
    else:
        print("Nope!")
        return False


number_of_guesses = 0
was_it_guessed = False
player_one_num = get_pick_number(1, 10)
instance = ["First", "Second", "Third"]
while was_it_guessed is False and number_of_guesses < 3:
    player_two_guess = get_guess_number(1, 10, instance[number_of_guesses])
    was_it_guessed = compare_numbers(player_one_num, player_two_guess)
    number_of_guesses += 1
    if number_of_guesses == 3 or was_it_guessed is True:
        print("Round complete.")
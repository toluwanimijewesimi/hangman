def choose_a_word():
    """Selects a random word for the game"""
    from random import choice
    with open('hangman_words.txt') as file:
        words = file.readlines()
        selected_word = choice(words)
        selected_word = (selected_word.strip()).upper()

    return selected_word

def print_board(wrong_guesses):
    """Prints the board of the game after each turn"""
    if len(wrong_guesses) == 0:
        print(f"\n  +---+     Wrong Guesses:")
        print(f"  |   |     Score: {score}")
        print("  |")
        print("  |")
        print("  |")
        print("  |")
        print("=========")
        print_display_word()
    elif len(wrong_guesses) == 1:
        print(f"\n  +---+     Wrong Guesses: {wrong_guesses[0]}")
        print(f"  |   |     Score: {score}")
        print("  |   O")
        print("  |")
        print("  |")
        print("  |")
        print("=========")
        print_display_word()
    elif len(wrong_guesses) == 2:
        print(f"\n  +---+     Wrong Guesses: {wrong_guesses[0]}, {wrong_guesses[1]}")
        print(f"  |   |     Score: {score}")
        print("  |   O")
        print("  |   |")
        print("  |")
        print("  |")
        print("=========")
        print_display_word()
    elif len(wrong_guesses) == 3:
        print(f"\n  +---+     Wrong Guesses: {wrong_guesses[0]}, {wrong_guesses[1]}, {wrong_guesses[2]}")
        print(f"  |   |     Score: {score}")
        print("  |   O")
        print("  |   |\\")
        print("  |")
        print("  |")
        print("=========")
        print_display_word()
    elif len(wrong_guesses) == 4:
        print(f"\n  +---+     Wrong Guesses:{wrong_guesses[0]}, {wrong_guesses[1]}, {wrong_guesses[2]}, {wrong_guesses[3]}")
        print(f"  |   |     Score: {score}")
        print("  |   O")
        print("  |  /|\\")
        print("  |")
        print("  |")
        print("=========")
        print_display_word()
    elif len(wrong_guesses) == 5:
        print(f"\n  +---+     Wrong Guesses: {wrong_guesses[0]}, {wrong_guesses[1]}, {wrong_guesses[2]}, {wrong_guesses[3]}, {wrong_guesses[4]}")
        print(f"  |   |     Score: {score}")
        print("  |   O")
        print("  |  /|\\")
        print("  |  /")
        print("  |")
        print("=========")
        print_display_word()
    elif len(wrong_guesses) == 6:
        print(f"\n  +---+     Wrong Guesses: {wrong_guesses[0]}, {wrong_guesses[1]}, {wrong_guesses[2]}, {wrong_guesses[3]}, {wrong_guesses[4]}, {wrong_guesses[5]}")
        print(f"  |   |     Score:{score}")
        print("  |   O")
        print("  |  /|\\")
        print("  |  / \\")
        print("  |")
        print("=========")
        print_display_word()

def guess_a_letter(selected_word):
    """Allows user to guess a letter and checks if letter is in the word"""
    letter = input("Guess a letter: ")
    letter = letter.upper()
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M']
    letters += ['N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    if letter in letters:
        if letter not in wrong_guesses:
            if letter not in correct_letters:
                if letter in selected_word:
                    if letter == game_word['one']:
                        displayed_word['one'] = letter
                        correct_letters.append(letter)
                    if letter == game_word['two']:
                        displayed_word['two'] = letter
                        correct_letters.append(letter)
                    if letter == game_word['three']:
                        displayed_word['three'] = letter
                        correct_letters.append(letter)
                    if letter == game_word['four']:
                        displayed_word['four'] = letter
                        correct_letters.append(letter)
                    if letter == game_word['five']:
                        displayed_word['five'] = letter
                        correct_letters.append(letter)
                    if letter == game_word['six']:
                        displayed_word['six'] = letter
                        correct_letters.append(letter)
                else:
                    wrong_guesses.append(letter)
            else:
                print("\nYou already guessed this letter")
        else:
            print("\nYou already guesses this letter")        
    else:
        print("\nYou must enter a letter")

def check_if_won():
    """Check if the word was guessed"""
    if displayed_word['one'] == game_word['one']:
        if displayed_word['two'] == game_word['two']:
            if displayed_word['three'] == game_word['three']:
                if displayed_word['four'] == game_word['four']:
                    if displayed_word['five'] == game_word['five']:
                        if displayed_word['six'] == game_word['six']:
                            return True

def print_display_word():
    """Display the word on the board"""
    display_word = f"{displayed_word['one']} {displayed_word['two']} "
    display_word += f"{displayed_word['three']} {displayed_word['four']} " 
    display_word += f"{displayed_word['five']} {displayed_word['six']}"
    print(display_word)

def update_score():
    """Upadate the score when the player earns and looses points"""
    made_score = 100
    lost_points = len(wrong_guesses) * 10
    gained_points = len(correct_letters) * 10 
    made_score -= lost_points
    made_score += gained_points
    return made_score

def top_five_scores(score):
    """Make a list of the top five scores"""
    import json

    try:
        with open('top_five_scores.json') as file:
            top_scores = json.load(file)
    except FileNotFoundError:
        with open('top_five_scores.json', 'w') as file:
            top_scores = []
            top_scores.append(score)
            if score == 6:
                del top_scores[-1]

            json.dump(top_scores, file)
    else:
        with open('top_five_scores.json', 'w') as file:
            top_scores.append(score)
            top_scores.sort(reverse=True)
            if len(top_scores) == 6:
                del top_scores[-1]

            json.dump(top_scores, file)

    if score in top_scores:
        return True

def update_high_scores():
    """Updates the high scores"""
    with open('high_scores.txt', 'a') as file:
        name = input('Enter your intials: ')
        if len(name) == 2:
            name = f"{name.upper()} "
        if len(name) == 3:
            name = name.upper()
        high_scores = f"{score}          {name}       {word}\n"

        file.write(high_scores)

def print_high_scores():
    """Print board of high scores"""
    import json

    with open('top_five_scores.json') as file:
        top_scores = json.load(file)

        with open('high_scores.txt') as file:
            high_scores = file.readlines()
            sorted_high_scores = sorted(high_scores, reverse=True)
            
        if len(top_scores) == 1:        
            print('-------------------------------------')
            print('            HIGH SCORES            ')
            print('-------------------------------------')
            print('    Score        Name        Word\n')
            print(f' 1.  {sorted_high_scores[0]}')
        elif len(top_scores) == 2:        
            print('-------------------------------------')
            print('            HIGH SCORES            ')
            print('-------------------------------------')
            print('    Score        Name        Word\n')
            print(f' 1.  {sorted_high_scores[0]}')
            print(f' 2.  {sorted_high_scores[1]}')
        elif len(top_scores) == 3:        
            print('-------------------------------------')
            print('            HIGH SCORES            ')
            print('-------------------------------------')
            print('    Score        Name        Word\n')
            print(f' 1.  {sorted_high_scores[0]}')
            print(f' 2.  {sorted_high_scores[1]}')
            print(f' 3.  {sorted_high_scores[2]}')
        elif len(top_scores) == 4:        
            print('-------------------------------------')
            print('            HIGH SCORES            ')
            print('-------------------------------------')
            print('    Score        Name        Word\n')
            print(f' 1.  {sorted_high_scores[0]}')
            print(f' 2.  {sorted_high_scores[1]}')
            print(f' 3.  {sorted_high_scores[2]}')
            print(f' 4.  {sorted_high_scores[3]}')
        elif len(top_scores) == 5:        
            print('-------------------------------------')
            print('            HIGH SCORES            ')
            print('-------------------------------------')
            print('    Score        Name        Word\n')
            print(f' 1.  {sorted_high_scores[0]}')
            print(f' 2.  {sorted_high_scores[1]}')
            print(f' 3.  {sorted_high_scores[2]}')
            print(f' 4.  {sorted_high_scores[3]}')
            print(f' 5.  {sorted_high_scores[4]}')                          

#Main Game
while True:
    print("\nWelcome to Hangman!")
    print("Enter 1 to play")
    print("Enter 2 to view the high scores")
    print("Enter 'quit' to quit")
    choice = input()
    #Plays the game then gives option to play again or quit
    if choice == '1':
        word = choose_a_word()
        #Seperates the word into letters in a dictionary so the leters the
        #User entars can be compared to it
        game_word = {
        'one': word[0],
        'two': word[1],
        'three': word[2],
        'four': word[3],
        'five': word[4],
        'six': word[5]
        }
        #Displays blanks on the board that will be filled in with the letters
        #The user enters
        displayed_word = {
        'one': '_',
        'two': '_',
        'three': '_',
        'four': '_',
        'five': '_',
        'six': '_'
        }
        wrong_guesses = []
        correct_letters = []
        #Loop runs game unitl player wins or runs out of attempts
        while check_if_won() != True:
            score = update_score()
            print_board(wrong_guesses)
            guess_a_letter(word)
            if check_if_won() == True:
                score = update_score()
                print_board(wrong_guesses)
                print("You guessed the word correctly")
                if top_five_scores(score) == True:
                    print('You made a high score')
                    update_high_scores()
                    print_high_scores()
            elif check_if_won() != True:
                if len(wrong_guesses) == 6:
                    score = update_score()
                    print_board(wrong_guesses)
                    print(f"You Lost\nThe word was {word}")
                    break
        play = input('Do you want to keep playing? (yes/no): ').lower()
        if play != 'yes':
            break
    #Show leaderboard then give options to play game or quit
    elif choice == '2':
        try:
            print_high_scores()
        except FileNotFoundError:
            print("\nThere are no highscores yet")
        play = input('Do you want to keep playing? (yes/no): ').lower()
        if play != 'yes':
            break
    #Quit out of game
    elif choice == 'quit':
        break
    else:
        print('\nChoose one of the given options')

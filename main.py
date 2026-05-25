import random
from words import word_list
from stages import stages


score = 0


def choose_word():
    return random.choice(word_list)


def display_word(word, guessed_letters):
    display = ""

    for char in word:
        if char in guessed_letters:
            display += char + " "
        else:
            display += "_ "

    return display


def play_game():
    global score

    random_word = choose_word()
    lives = 6
    guessed_letters = []
    game_over = False

    print("\n🎮 Welcome to Hangman!")

    while not game_over:

        letter = input("\nGuess a letter: ").lower()

        # Prevent duplicate guesses
        if letter in guessed_letters:
            print("⚠️ You already guessed that letter!")
            continue

        guessed_letters.append(letter)

        # Wrong guess
        if letter not in random_word:
            lives -= 1
            print(f"❌ Wrong guess! Lives left: {lives}")

        # Display word
        display = display_word(random_word, guessed_letters)

        print("\n" + display)
        print(stages[lives])

        # Win condition
        if "_" not in display:
            print("🏆 You Win!")
            score += 10
            print(f"⭐ Score: {score}")
            game_over = True

        # Lose condition
        if lives == 0:
            print("💀 You Lost!")
            print(f"The word was: {random_word}")
            print(f"⭐ Score: {score}")
            game_over = True


# Replay loop
while True:

    play_game()

    replay = input("\nDo you want to play again? (yes/no): ").lower()

    if replay != "yes":
        print(f"\nFinal Score: {score}")
        print("👋 Thanks for playing!")
        break
import random

word_list = ["giraffe", "baboon", "camel", "bulldog", "elephant", "lizard"]

word = random.choice(word_list)

display = []
previous_guesses = []
for i in word:
    display += "_"
print(display)
counter = 1
show = len(word)+3
game = True
while game:
    print(f"You got {show} guess left")
    guess = input("Guess a letter: ").lower()
    previous_guesses.append(guess)

    for position in range(len(word)):
        letter = word[position]
        if letter == guess:
            display[position] = letter
        else:
            display = display
    print(display)

    print(f"\nPrevious choices are {previous_guesses}")
    counter += 1
    show -= 1
    if "_" not in display:
        print("You win")

        game = False
    elif counter > len(word)+3:
        print("You lose")
        print(f"Correct answer was {word}")
        game = False

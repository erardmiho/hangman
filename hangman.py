# hangman game
import random
print('Welcome to Hangman!')
word_list = ['python', 'java', 'javascript', 'ruby', 'swift']
chosen_word = random.choice(word_list)
end_of_game = 0
guessing_word = ['_'] * len(chosen_word)
game_stage = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''',
'''
  +---+
  |   |
  O   |
      |
      |
      |
=========''',
'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''',
'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''',
'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''',
'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''',
'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
check_word = '_' * len(chosen_word)

print(f'The word is: {" ".join(guessing_word)}')
print(game_stage[0])
while end_of_game <= len(game_stage):
    #giving words
    guess = input('Guess a letter: ').lower()
    #starting the game
    for i in range(len(chosen_word)):
        if guess == chosen_word[i]:
            guessing_word[i] = guess
    if guess in chosen_word:
        print(f'Good job! {guess} is in the word.')
        # replace guess with numbers
        for i in range(len(chosen_word)):
            if guess == chosen_word[i]:
                check_word = check_word[:i] + guess + check_word[i+1:]
                print(check_word)
        if check_word == chosen_word:
            print(f'Congratulations! You guessed the word {chosen_word} correctly!')
            break            
    else:
        end_of_game += 1
        if end_of_game < len(game_stage):
            print(f'{game_stage[end_of_game]}')
            print(f'Sorry, {guess} is not in the word.')
        else:
            break
else:
    print(game_stage[end_of_game])
    print(f'Game over! The word was {chosen_word}.')

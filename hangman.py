#Instruction
'''
1. Generate a random word from the list of words.
2. Ask the user to guess a letter.
3. Check if the letter is in the word.
4. If the letter is in the word, reveal the letter in the word, the game continues. 
5. If the letter is not in the word, reveal a part of the hangman.
6. If the user guesses all the letters in the word, congratulate the user and ask if they want to play again.
7. If the user guesses the wrong letter 7 times, the game is over and the user loses.
'''

#1. Generate a random word from the list of words.
import random
words = ['apple', 'banana', 'orange', 'pear', 'grape', 'pineapple', 'watermelon', 'kiwi', 'peach', 'plum']
word = random.choice(words).lower()
# Store all the guessed letters in a list
guessed_letters = []
stored_letters = []
wrong_letters = []
HANGMAN_PICS = ['''
   +---+
       |
       |
       |
      ===''', '''
   +---+
   O   |
       |
       |
      ===''', '''
   +---+
   O   |
   |   |
       |
      ===''', '''
   +---+
   O   |
  /|   |
       |
      ===''', '''
   +---+
    O   |
   /|\  |
        |
       ===''', '''
   +---+
   O   |
  /|\  |
  /    |
      ===''', '''
   +---+
   O   |
  /|\  |
  / \  |
      ===''', '''
   💀 You Loose! 💀''']

for i in range(len(word)): #len(word) is the length of the random word
    #print the underscores for each letter in the word
    print('_', end=' ') #end=' ' prevents the print statement from going to a new line
    stored_letters.append('_') # store underscores for each letter in the word to a variable
print() #print a new line after the word

# Check which random word is being used by computer
#print(f'Testing purposes, the answer is: {word}')

# Allow user to guess 7 times
count = 0

def display_guessed_letters(word, guessed_letter):
    for w in range(len(word)): # iterate [0,1,2...]
        if guessed_letter == word[w]: # check if the guessed letter matches the word
            print(f'The letter {guessed_letter} is in the word.')
            #print(f'the index of the letter is {w}')
            #print(f'checking values for stored_letters variable:{stored_letters}')
            #need to store matched letter in the correct index
            stored_letters[w] = guessed_letter #replace the underscore with the matched letter
            #print the updated stored_letters variable
            print(f'updated stored_letters variable:{stored_letters}')
            # if the guessed letter is not in the word, reveal a part of the hangman  

#2. Check if the letter is in the word.
while count < 7 and stored_letters != list(word): # while count is less than 7 and the word is not completely guessed
    
    #Show very first hangman picture
    if count == 0:
        print(HANGMAN_PICS[0])
        
    #3. Ask the user to guess a letter.
    guessed_letter=input('Enter a letter to guess:\n ').lower()
    
    # Check user's input against the word and reveal the letter or part of the hangman
    # Make sure the user enters a single character
    if guessed_letter not in stored_letters:
        if len(guessed_letter)==1 and guessed_letter.isalpha(): # check if the input is a single character and is alphabetic
            # modified by Kenny
            if guessed_letter in word: # check if the guessed letter is in the word
                display_guessed_letters(word, guessed_letter)
            else:
                
                wrong_letters.append(guessed_letter) # add the wrong letter to the list of wrong letters
                count += 1
                print(f'You have used {count} out of 7 guesses.')
                print(f'{HANGMAN_PICS[count]}')
                print(f'The wrong letters are: {wrong_letters}')
                # increment to track number of guesses
        else:
            print("Please enter a single string character to continue.")
    else:
        print('You have already guessed this letter. Please enter a different one.')
# if run out of guesses and the word is not completely guessed, the game is over
if count == 7 and stored_letters != list(word):
    print(f'Sorry, you have used up all your guesses. The word was {word}.')
else:        
    print(f'Congratulations! You guessed the word {word}!')
    

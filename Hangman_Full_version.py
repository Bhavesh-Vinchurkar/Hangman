import random

#Word bank of animals
word_list = ('ant baboon badger bat bear beaver camel cat clam cobra cougar '
         'coyote crow deer dog donkey duck eagle ferret fox frog goat '
         'goose hawk lion lizard llama mole monkey moose mouse mule newt '
         'otter owl panda parrot pigeon python rabbit ram rat raven '
         'rhino salmon seal shark sheep skunk sloth snake spider '
         'stork swan tiger toad trout turkey turtle weasel whale wolf '
         'wombat zebra ').split()


#word_list=['bhavesh','abhishek','riddhi']
selected_word=random.choice(word_list)
selected_word_list=[i for i in selected_word]
user_guessed_word=["_" for _ in range(len(selected_word_list))]
print("Here's the riddle - ")
for i in user_guessed_word:
    print(i,end='')
print("\n")
HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
lives=7
while user_guessed_word!=selected_word_list:
    guessed_alphabet=input("Guess a letter : ").lower()
    if guessed_alphabet in selected_word_list:
        if selected_word_list.count(guessed_alphabet)>1:
            x=0
            for i in range(selected_word_list.count(guessed_alphabet)):
                user_guessed_word[selected_word_list.index(guessed_alphabet,x)]=guessed_alphabet
                x=selected_word_list.index(guessed_alphabet)+1
        else:
            user_guessed_word[selected_word_list.index(guessed_alphabet)]=guessed_alphabet
        for letter in user_guessed_word:
            print(letter,end='')
        print('')
    else:
        if lives>1:
            print("Wrong letter. Try again")
        print(HANGMANPICS[-lives])
        for letter in user_guessed_word:
            print(letter,end='')
        print('')
        lives-=1
        print(f"{lives} lives left")

    if lives==0:
        print(f"You lost. The word was {selected_word}")
        print("Try Again")
        break

if user_guessed_word==selected_word_list:
    print("Hurray! You Won")
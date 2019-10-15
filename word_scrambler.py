from random import *
import sys

# needs to input how many questions
# probably should search up the proper standard for how this is done
if(len(sys.argv) != 2):
	print("Usage: python3 word_scrambler.py [NUM_QUESTIONS]")
	sys.exit()

f=open("random_words.txt", "r")
lines = f.readlines()

# checks if a number is already in the array
def check_num(n, array):
	in_array = False
	for i in range(len(array)):
		if(n == array[i]):
			in_array = True
			break
	return in_array

# scrambles a word by creating an array that has random indexes
# from the word that is passed through, this array is then
# used as the order for the scrambled word
# KNOWN ISSUE: words maybe put into the same order
def scramble_word(word):
	scrambled_word = ""

	random_array = []
	count = 0
	while(len(random_array) < len(word)):
		n = randrange(0, len(word))
		if(check_num(n, random_array) == False):
			random_array.append(n)

	for i in random_array:
		scrambled_word = scrambled_word + word[i]

	return scrambled_word


#		THE GAME		#
turns = 0
correct_answers = 0
questions = int(sys.argv[1])

while(turns < questions):
	word = lines[randrange(0, len(lines))].lower()
	word = word[:-1]
	print(f"Your scrambled word is: {scramble_word(word)}")
	guess = input("Guess: ")
	if(guess.lower() != word):
		print(f"Wrong! The word is actually {word}")
	else:
		print("Correct!")
		correct_answers+=1
	turns+=1

print(f"You got {correct_answers}/{questions}.")
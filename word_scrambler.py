from random import *
import sys

if(len(sys.argv) != 2):
	print("Usage: python3 word_scrambler.py [NUM_QUESTIONS]")
	sys.exit()

f=open("random_words.txt", "r")
lines = f.readlines()


def check_num(n, array):
	in_array = False
	for i in range(len(array)):
		if(n == array[i]):
			in_array = True
			break
	return in_array

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

print(f"You got {correct_answers}/{sys.argv[1]}.")
"""
File: boggle.py
Name: Tom Tang
----------------------------------------
TODO:
"""

import time

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it

# Constant
FILE = 'dictionary.txt'
INPUT_ERROR = 'Illegal input'


def main():
	# Variables
	s_set = set()  # A set to collect all letters input and remove duplicates for filtering dictionary
	array = []  # A list of lists, to collect letters input by each row for boggle game

	# Create 4x4 array
	for i in range(4):
		# Ask for user input
		row = input(f'{i+1} row of letters: ')
		lst = row.lower().split()
		# Check if is valid input
		if not valid_input(lst):
			return print(INPUT_ERROR)
		# Update the set and the list
		s_set.update(lst)
		array.append(lst)

	# Import dictionary
	dictionary = read_dictionary(s_set)

	# Find words from the given array
	start = time.time()
	words = find_words(array, dictionary)
	print(f'There are {len(words)} words in total.')
	end = time.time()

	# Print the processing time
	print('----------------------------------')
	print(f'The speed of your boggle algorithm: {end - start} seconds.')


def read_dictionary(s_set):
	with open(FILE, 'r') as f:
		d = f.read().splitlines()

	# Filter dictionary for words start with the letters from given array and are longer than 4 letters (include 4)
	dictionary = [word for word in d if word.startswith(tuple(s_set)) and len(word) >= 4]
	return dictionary


def find_words(array, dictionary):
	"""
	:param array: (list) contains 4 child lists, each child list contains 4 single letter words
	:param dictionary: (list) the imported dictionary for searching words
	:return: (list) a list of matching words
	"""
	word = ''
	words = []
	path = []
	for x in range(4):
		for y in range(4):
			find_words_helper(array, word, words, path, x, y, dictionary)
	return words


def find_words_helper(array, word, words, path, row, col, dictionary):
	"""
	:param array: (list) contains 4 child lists, each child list contains 4 single letter words
	:param word: (string) the word working in progress
	:param words: (list) a list of matching words
	:param path: (list) a list of tuple,
		store the 'row' and 'col' that have been checked through
	:param row: (integer) an index represents the child list from the given array
	:param col: (integer) an index represents the item from the selected child list
	:param dictionary: (list) the imported dictionary for searching words
	:return: (list) a list of matching words
	"""
	for x in range(row-1, row+2):
		for y in range(col-1, col+2):
			# Check if x and y are within the size of array and the location has been checked through
			if 0 <= x < 4 and 0 <= y < 4 and (x, y) not in path:
				# Choose
				word += array[x][y]
				path.append((x, y))
				# Explore
				dict_filtered = has_prefix(word, dictionary)
				# Check if filtered dictionary has any items
				if len(dict_filtered) > 0:
					if len(word) >= 4 and word in dict_filtered and word not in words:
						words.append(word)
						# Print the word if it matches the word in dictionary with at least 4 letters in length
						print(f'Found \"{word}\"')
					# Pass to next recursion to continue finding longer word
					find_words_helper(array, word, words, path, x, y, dict_filtered)
				# Un-choose
				path.pop()
				word = word[:len(word)-1]
	return words


def has_prefix(sub_s, dictionary):
	"""
	:param sub_s: (string) the word working in progress
	:param dictionary: (list) the imported dictionary for searching words
	:return: (list) a filtered dictionary with words start with sub_s
	"""
	return [word for word in dictionary if word[:len(sub_s)] == sub_s]


def valid_input(lst):
	"""
	:param lst: (list) user input
	:return: (boolean) True if is valid input
	"""
	if len(lst) == 0:
		return False
	else:
		for ch in lst:
			if not ch.isalpha() or len(ch) != 1:
				return False
	return True


if __name__ == '__main__':
	main()

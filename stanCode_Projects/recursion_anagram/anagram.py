"""
File: anagram.py
Name: Tom Tang
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

import time                   # This file allows you to calculate the speed of your algorithm

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop

# Global variables
dictionary = []


def main():
    print('Welcome to stanCode \"Anagram Generator\" (or -1 to quit)')
    while True:
        s = input('Find anagrams for: ')  # input in string
        if s == EXIT:  # escape program when input == EXIT
            break
        else:
            read_dictionary(s.lower())  # convert to lowercase to match with loaded dictionary
            anagrams = []  # empty list to store all anagrams
            print('Searching...')

            start = time.time()  # time measure start

            find_anagrams(s.lower(), '', len(s.lower()), anagrams)  # recursion to find all anagrams
            print(f'{len(anagrams)} anagrams: {anagrams}')  # print all collected anagrams

            end = time.time()  # time measure end

            print('----------------------------------')
            print(f'The speed of your anagram algorithm: {end-start} seconds.')


def read_dictionary(s):
    global dictionary
    with open(FILE, 'r') as f:
        d = f.read().splitlines()  # read dictionary and strip newline character

    # shortlist the dictionary with only words start with characters from the given string and with the same length
    dictionary = [word for word in d if word.startswith(tuple(s)) and len(word) == len(s)]


def find_anagrams(s, anagram, end, anagrams):
    """
    :param s: (str) input given for searching anagram
    :param anagram: (str) temp variable, start as empty str. return to 'anagrams' when conditions are met
    :param end: (int) length of the string, used for determining how many recursion need to run through
    :param anagrams: (list) collection of anagrams identified by the recursion
    :return:
        1. print each anagram when it's identified
        2. return 'anagrams' to main function
    """
    global dictionary
    # Base case: when 'end' reduced to 0 and is found in dictionary and is not duplicated
    if end == 0 and anagram in dictionary and anagram not in anagrams:
        print(f'Found: {anagram}')
        print('Searching...')
        anagrams.append(anagram)
    # Recursion
    else:
        for i in range(end):
            # Choose
            anagram += s[i]
            # Explore
            s_temp = s[0:i] + s[i+1:]  # temp str to be thrown into next recursion
            if has_prefix(anagram):  # check any word in dictionary starts with current 'anagram', stop if == False
                find_anagrams(s_temp, anagram, end-1, anagrams)
            # Un-Choose
            anagram = anagram[0:len(anagram)-1]  # revert anagram to where has options


def has_prefix(sub_s):
    """
    :param sub_s: (str) sub set of the given string
    :return: (bool) True if any word in dictionary starts with sub_s else False
    """
    global dictionary
    for word in dictionary:
        #  use string slicing instead of startswith() due to performance concern
        if word[:len(sub_s)] == sub_s:
            return True
    return False


if __name__ == '__main__':
    main()

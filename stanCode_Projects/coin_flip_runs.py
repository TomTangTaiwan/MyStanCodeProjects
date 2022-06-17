"""
File: coin_flip_runs.py
Name: Tom Tang
-----------------------
This program should simulate coin flip(s)
with the number of runs input by users.
A 'run' is defined as consecutive results
on either 'H' or 'T'. For example, 'HHHHHTHTT'
is regarded as a 2-run result.
Your program should stop immediately after your
coin flip results reach the number of runs!
"""
import random
import random as r

COIN = 'HT'


def main():
	"""
	'H' = Head; 'T' = Tail
	1. print 'Let\'s flip a coin!'
	2. input 'Number of runs: ' --> ask for 1 int (= num_run)
	3. The program stop when 'H' or 'T' appear multiple times in a row by 'num-run' of runs
	"""
	print('Let\'s flip a coin!')
	num_runs_goal = int(input('Number of runs: '))
	result = flip_coin(num_runs_goal)
	print(result)


def flip_coin(goal):
	s = ''
	same_side_count = 1
	num_runs_count = 0
	while True:
		s += random.choice(COIN)
		len_s = len(s)
		if len_s == 1:
			pass
		else:
			if s[len_s-1] != s[len_s-2]:
				same_side_count = 1
			else:
				if same_side_count == 1:
					same_side_count += 1
					num_runs_count += 1
				else:
					same_side_count += 1
		if num_runs_count == goal:
			break
	return s


# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #

if __name__ == "__main__":
	main()

"""
File: largest_digit.py
Name: Tom Tang
----------------------------------
This file recursively prints the biggest digit in
5 different integers, 12345, 281, 6, -111, -9453
If your implementation is correct, you should see
5, 8, 6, 1, 9 on Console.
"""


def main():
	print(find_largest_digit(12345))      # 5
	print(find_largest_digit(281))        # 8
	print(find_largest_digit(6))          # 6
	print(find_largest_digit(-111))       # 1
	print(find_largest_digit(-9453))      # 9


def find_largest_digit(n):
	"""
	:param n: given number to find the largest digit
	:return: largest digit of the given number
	"""
	# Boundary condition: Flip the signage for negative number
	if n < 0:
		n = -n
	# Edge case: if n is single digit, return n
	if n % 10 == n:
		return n
	else:
		# 'print' is in main function, need to 'return' the result to main function
		return find_largest_digit_helper(n, -1)


def find_largest_digit_helper(num, largest_digit):
	"""
	:param num: given number to find the largest digit, reduce by 1 digit in each recursion
	:param largest_digit: where stores the largest digit
	:return: largest digit of the given number
	"""
	# Base case
	if num == 0:
		return largest_digit
	# Recursion
	else:
		if num % 10 > largest_digit:
			largest_digit = num % 10
		# since the 'print' is in main function, need to remember 'return' to last recursion
		return find_largest_digit_helper((num - num % 10) // 10, largest_digit)


if __name__ == '__main__':
	main()

"""
File: class_reviews.py
Name: Tom Tang
-------------------------------
At the beginning of this program, the user is asked to input
the class name (either SC001 or SC101).
Attention: your input should be case-insensitive.
If the user input "-1" for class name, your program would show
the maximum, minimum, and average among all the inputs.
"""
QUIT = '-1'


def main():
    """
    1. ask class (SC001 or SC101, case-insensitive)
    2. ask score of the class
        a. record the highest score
        b. record the lowest score
        c. calculate the average score
    3. User key in 'QUIT' to quit the program
    """
    max_001 = 0
    min_001 = 0
    count_001 = 0
    sum_001 = 0
    avg_001 = 0
    max_101 = 0
    min_101 = 0
    count_101 = 0
    sum_101 = 0
    avg_101 = 0
    while True:
        input_class = str(input('Which class? ')).upper()
        if input_class == QUIT and count_001 == 0 and count_101 == 0:
            print('No class scores were entered')
            break
        elif input_class == QUIT:
            print('=============SC001=============')
            if count_001 == 0:
                print('No score for SC001')
            else:
                print('Max (001): ' + str(max_001))
                print('Min (001): ' + str(min_001))
                print('Avg (001): ' + str(avg_001))
            print('=============SC101=============')
            if count_101 == 0:
                print('No score for SC101')
            else:
                print('Max (101): ' + str(max_101))
                print('Min (101): ' + str(min_101))
                print('Avg (101): ' + str(avg_101))
            break
        input_score = int(input('Score: '))
        if input_class == 'SC001':
            count_001 += 1
            sum_001 += input_score
            avg_001 = sum_001/count_001
            if count_001 == 1:
                max_001 = min_001 = input_score
            elif input_score > max_001:
                max_001 = input_score
            elif input_score < min_001:
                min_001 = input_score
        elif input_class == 'SC101':
            count_101 += 1
            sum_101 += input_score
            avg_101 = sum_101/count_101
            if count_101 == 1:
                max_101 = min_101 = input_score
            elif input_score > max_101:
                max_101 = input_score
            elif input_score < min_101:
                min_101 = input_score


# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #

if __name__ == '__main__':
    main()

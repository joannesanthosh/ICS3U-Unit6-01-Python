#!/usr/bin/env python3

# Created by: Joanne Santhosh
# Created on: Dec 2022
# This program uses an array


import random


def main():
    # this function uses an array

    my_numbers = []

    # input
    for loop_counter in range(0, 10):
        random_number = random.randint(0, 100)
        my_numbers.append(random_number)
    print("")

    print("Here are the 10 random numbers:")

    for loop_counter in range(0, 10):
        print("The random number is: {0}".format(my_numbers[loop_counter]))
    # sum (random_numbers) adds all variables in the list
    average = sum(my_numbers) / len(my_numbers)
    print("")
    print("The average is {0}".format(average))

    print("\nDone.")


if __name__ == "__main__":
    main()

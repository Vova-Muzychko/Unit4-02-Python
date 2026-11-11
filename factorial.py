#!/usr/bin/env python3

# Created by: Vova
# Created on: November 11 2026
# This program calculates the factorial of a whole number using a simulated do..while loop.


def main():
    # Input
    user_string = input("Enter a positive whole number: ")

    # Process and Output
    try:
        user_number = int(user_string)

        if user_number < 0:
            print("Invalid input! Please enter a number 0 or greater.")
        elif user_number == 0:
            print("0! = 1")
        else:
            factorial = 1
            counter = user_number

            # Simulating a do..while loop in Python
            while True:
                factorial = factorial * counter
                counter = counter - 1

                # Loop exit condition at the bottom
                if counter <= 0:
                    break

            print(f"{user_number}! = {factorial}")

    except ValueError:
        print("Invalid input! That is not a whole number.")


if __name__ == "__main__":
    main()

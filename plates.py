def main():

    plate = input("Plate: ")

    if is_valid(plate):

        print("Valid")

    else:

        print("Invalid")



def is_valid(s):

    # Rule 1: Length must be between 2 and 6 characters

    if not (2 <= len(s) <= 6):

        return False



    # Rule 2: The first two characters must be letters

    if not (s[0].isalpha() and s[1].isalpha()):

        return False



    # Rule 3: Check if numbers are only at the end and the first number isn't '0'

    number_started = False

    for i, char in enumerate(s):

        if char.isdigit():

            # Check if a number appears after letters and ensures no letter comes after a number

            if not number_started:

                # This is the first number, it can't be '0'

                if char == '0':

                    return False

                number_started = True

        else:

            # If number has started, no more letters should appear after it

            if number_started:

                return False



    # Rule 4: Check for periods, spaces, or punctuation (only letters and digits allowed)

    if not s.isalnum():

        return False



    # If all checks passed, return True

    return True



main()

 
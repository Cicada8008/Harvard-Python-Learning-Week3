# Get input from the user in camel case format

camel_case = input("Enter a variable name in camel case: ")



# Create an empty list to store the snake case result

snake_case = []



# Initialize an index variable to manually keep track of the position

index = 0



# Iterate through each character in the camel case string using a while loop

while index < len(camel_case):

    char = camel_case[index]



    # If the character is uppercase and it's not the first character, convert it

    if char.isupper() and index != 0:

        snake_case.append('_')

        snake_case.append(char.lower())

    else:

        # If the character is lowercase or the first character, just add it as is

        snake_case.append(char.lower())



    # Increment the index manually

    index += 1



# Join the list into a single string and print the snake case result

print("".join(snake_case))

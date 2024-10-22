# Prompt the user for input

text = input("Input: ")



# Define the set of vowels to remove (both uppercase and lowercase)

vowels = "aeiouAEIOU"



# Create an empty string to store the result

result = ""



# Iterate through each character in the input text

for char in text:

    # If the character is not a vowel, add it to the result

    if char not in vowels:

        result += char



# Output the result without vowels

print("Output:", result)

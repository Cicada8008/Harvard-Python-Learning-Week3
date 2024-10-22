# Define the list of food items

food = [

    {"fruit": "Apple", "Calories": "130"},

    {"fruit": "Avocado", "Calories": "50"},
    {"fruit": "Pear", "Calories": "100"},
    {"fruit": "Sweet Cherries", "Calories": "100"},
    {"fruit": "Kiwifruit", "Calories": "90"},
    {"fruit": "Tomato", "Calories": None}

]



# Prompt the user for a fruit

user_input = input("Item: ").strip().title()  # Get user input and strip any extra spaces



# Initialize variable to hold calorie count

calorie_count = None



# Iterate through the list to find the fruit

for item in food:

    if item["fruit"].strip() == user_input:  # Compare input with the fruit key, stripping spaces

        calorie_count = item["Calories"]  # Get the calorie count

        break  # Stop searching once we find the fruit



# Print the calorie count if found

if calorie_count is not None:

    print("Calories:",calorie_count)  # Print calorie count

else:

    print("")  # Handle case where the fruit is not in the list

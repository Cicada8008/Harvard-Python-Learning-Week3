# Initialize the amount due for the Coca-Cola bottle

amount_due = 50



# Inform the user of the initial amount due

print("Amount due:", amount_due)



# Continue prompting the user for coins until the amount due is 0 or less

while amount_due > 0:

    # Prompt the user to insert a coin

    insert_coin = int(input("Insert coin:"))



    # Check if the inserted coin is a valid denomination (25, 10, or 5 cents)

    if insert_coin in [25, 10, 5]:

        # Subtract the inserted coin from the amount due

        amount_due -= insert_coin

    else:

        # Ignore invalid denominations and inform the user

        print("Invalid coin. Please insert 25, 10, or 5 cents.")



    # If the amount due is still positive, inform the user of the remaining amount

    if amount_due > 0:

        print("Amount Due:",amount_due)



# If the user overpays, calculate and display the change
if amount_due == 0:
    print("Change Owed: 0")


if amount_due < 0:

    print("Change Owed:", abs(amount_due))

remarks = {}
# Set a flag to indicate that the polling is active
poll_active = True

while poll_active:
    # Request for the name of the user and their remark
    fullname = input("Enter your full name: ")
    remark = input("What is your country of residence? ")

    # Store the remark in the dictionary
    remarks[fullname] = remark

    # Check if someone is still available to take the poll
    next = input("Is there anyone else available to answer a question? (yes/no) ").lower()
    if next == "no":
        poll_active = False

# Our Poll is complete. Therefore, display the results as follows
print("\n**** Poll Results ****")
for fullname, remark in remarks.items():
    print(f"{fullname}, {remark} is your country of residence.")

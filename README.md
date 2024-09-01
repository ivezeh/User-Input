# Simple Polling Script 🗳️

This project is a basic Python script designed to conduct a simple polling session. The script collects users' full names and their countries of residence, stores the information, and then displays the results once the poll is complete.

## Features
- **Interactive Polling**: Collects the full name and country of residence from users.
- **Dynamic Input**: The polling continues until no additional participants are available.
- **Result Display**: Outputs the collected data in a clean format once polling ends.

## How It Works
1. The script prompts each participant for their full name and country of residence.
2. The responses are stored in a dictionary, with the full name as the key and the country of residence as the value.
3. The poll continues until the user indicates that no more participants are available.
4. Once the poll is complete, the script prints out the results, showing each participant's name and country of residence.

## Example Usage
```python
remarks = {}
# Set a flag to indicate that the polling is active
poll_active = True

while poll_active:
    # Request the user's full name and their country of residence
    fullname = input("Enter your full name: ")
    remark = input("What is your country of residence? ")

    # Store the remark in the dictionary
    remarks[fullname] = remark

    # Check if there's anyone else available to answer the poll
    next = input("Is there anyone else available to answer a question? (yes/no) ").lower()
    if next == "no":
        poll_active = False

# Poll is complete. Display the results as follows
print("\n**** Poll Results ****")
for fullname, remark in remarks.items():
    print(f"{fullname}, {remark} is your country of residence.")

```

# Getting Started
## Prerequisites
- ** Python 3.x: Make sure you have Python 3.x installed on your system.

## Running the Script
1. Clone the repository or download the script.
2. Open a terminal or command prompt and navigate to the directory where the script is located.
3. Run the script using the following command:
``` bash
python3 app.py
```

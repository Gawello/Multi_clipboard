import sys
import clipboard
import json

SAVED_DATA = "clipboard.json"


# Saving clipboard to file, create if file does not exist
def save_items(filepath, data):
    with open(filepath, "w") as f:
        json.dump(data, f)


# Reading file, display error if file does not exist
def load_data(filepath):
    try:
        with open(filepath, "r") as f:
            data = json.load(f)
            return data
    except FileNotFoundError:
        return {}


# Command handling
if len(sys.argv) == 2:
    command = sys.argv[1]
    data = load_data(SAVED_DATA)

    # Adding clipboard to file
    if command == "save":
        key = input("Enter a key: ")
        data[key] = clipboard.paste()
        save_items(SAVED_DATA, data)
    # Search and load data
    elif command == "load":
        key = input("Enter a key: ")
        if key in data:
            clipboard.copy(data[key])
            print("Data copied to clipboard.")
        else:
            print("Key does not exist.")
    # Display all saved data
    elif command == "list":
        print(data)
    else:
        print("Unknown command")
else:
    print("Please pass exactly one command.")

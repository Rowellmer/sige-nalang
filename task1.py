def display_data(data):
    if not data:
        print("No data available.")
    else:
        print("Current data entries:")
        for i, entry in enumerate(data):
            print(f"{i + 1}: {entry}")

def add_single_entry(data):
    entry = input("Enter the data entry to add: ")
    data.append(entry)
    print(f"'{entry}' has been added.")

def add_multiple_entries(data):
    entries = input("Enter multiple data entries separated by commas: ")
    for entry in entries.split(','):
        data.append(entry.strip())
    print("Entries have been added.")

def delete_entry(data):
    display_data(data)
    try:
        index = int(input("Enter the number of the entry to delete: ")) - 1
        if 0 <= index < len(data):
            deleted_entry = data.pop(index)
            print(f"'{deleted_entry}' has been deleted.")
        else:
            print("Invalid entry number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def update_entry(data):
    display_data(data)
    try:
        index = int(input("Enter the number of the entry to update: ")) - 1
        if 0 <= index < len(data):
            new_entry = input("Enter the new data entry: ")
            data[index] = new_entry
            print(f"Entry has been updated to '{new_entry}'.")
        else:
            print("Invalid entry number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def reverse_data(data):
    data.reverse()
    print("Data has been reversed.")

def main():
    data = []
    while True:
        print("\nChoose an action:")
        print("1. Add single data entry")
        print("2. Add multiple data entries")
        print("3. Display data")
        print("4. Delete data")
        print("5. Update data")
        print("6. Reverse data")
        print("7. Exit")
        
        choice = input("Enter your choice (1-7): ")

        if choice == '1':
            add_single_entry(data)
        elif choice == '2':
            add_multiple_entries(data)
        elif choice == '3':
            display_data(data)
        elif choice == '4':
            delete_entry(data)
        elif choice == '5':
            update_entry(data)
        elif choice == '6':
            reverse_data(data)
        elif choice == '7':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")

if __name__ == "__main__":
    main()
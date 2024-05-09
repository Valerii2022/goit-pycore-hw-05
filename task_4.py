def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    try:
        name, phone = args
        contacts[name] = phone
        return "Contact added."
    except ValueError:
        return "Not enough values to unpack"

def change_contact(args, contacts):
    try:
        name, new_phone = args
        if name in contacts:
            contacts[name] = new_phone
            return f"Contact {name} changed."
        else:
            return f"Contact {name} not found"
    except ValueError:
        return "Not enough values to unpack"

def show_phone(args, contacts):
    try:
        name = args[0]
        if name in contacts:
            return f"The phone number for '{name}' is {contacts[name]}."
        else:
            return f"Contact {name} not found"
    except Exception:
        return "Error.Please try again!" 

def show_all(contacts):
    try:
        if len(contacts) == 0:
            return "You have no contacts yet."   
        else:
            return contacts
    except Exception:
        return "Error.Please try again!"

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            print(add_contact(args, contacts))
        
        elif command == "change":
            print(change_contact(args, contacts))
        
        elif command == "phone":
            print(show_phone(args, contacts))
        
        elif command == "all":
            print(show_all(contacts))

        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
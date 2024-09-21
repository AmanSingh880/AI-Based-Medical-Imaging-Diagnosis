def validate_name(name):
    if name.isalpha():
        return True
    else:
        return False
name = input("Enter your name: ")

if validate_name(name):
    print("Name is valid.")
else:
    print("Invalid name. Please enter a valid name.")
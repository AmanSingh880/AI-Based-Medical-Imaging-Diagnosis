# age function 
def validate_age(age):
    age = float(age) 
    if 0 <= age <= 100: 
        return True
    return False
age=input("Enter your age :")
if validate_age(age):
    print("Age is valid ")
else:
    print("invalid age , Please enter the correct age ")
# validate_age(17.5)
# name function
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

# database works 

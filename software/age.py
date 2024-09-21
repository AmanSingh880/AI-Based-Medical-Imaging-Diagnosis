def validate_age(age):
    if age.isdigit():
        age = int(age) #ye is liye add kiya hai kyuki agar koi 17.5 ya ise me age ko add kare to handle ho jaye invalid na de 
        if 0 <= age <= 100: 
            return True
    return False
age=input("Enter your age :")
if validate_age(age):
    print("Age is valid ")
else:
    print("invalid age , Please enter the correct age ")
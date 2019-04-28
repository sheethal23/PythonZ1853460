def main():
    full_name = get_full_name()
    print()
    password = get_password()
    print()
    email = get_email()
    print()
    phone = get_number()
    print()
    first_name = get_first_name(full_name)
    phonenumber = phone_format(phone)
    print("Hi " + first_name + ", thanks for creating an account.")
    print("We'll text your confirmation code to this number: " + phonenumber)
    
def get_full_name():
    while True:
        name = input("Enter full name:       ").strip()
        if " " in name:
            return name
        else:
            print("You must enter your full name.")
    
def get_first_name(full_name):
    index1 = full_name.find(" ")
    first_name = full_name[:index1]
    return first_name


def phone_format(n):
    return format(int(n[:-1]), ",").replace(",", ".") + n[-1]

def get_email():
    while True:
        email = input("Enter email address:      ").strip()
        if "@" and ".com" in email:
            return email
        else:
            print("Please enter a valid email address.")

def get_number():
    while True:
        number = input("Enter phone number:       ")
        if len(number) == 10:
            return number

        elif "(" or ")" or "-" in number:
            print("Please enter a 10-digit phone number.")
        else:
            print("Please enter a 10-digit phone number.")



def get_password():
    while True:
        digit = False
        cap_letter = False
        password = input("Enter password:        ").strip()
        for char in password:
            if char.isdigit():
                digit = True
            elif char.isupper():
                cap_letter = True
        if digit == False or cap_letter == False or len(password) < 8:
            print("Password must be 8 characters or more \n" +
                  "with at least one digit and one uppercase letter.")
        else:
            return password




if __name__ == "__main__":
    main()

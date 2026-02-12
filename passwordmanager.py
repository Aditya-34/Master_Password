import secrets
import string

def generate_master_password(length=12):
    alphabet = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(alphabet) for _ in range(length))

MASTER_PASSWORD = generate_master_password()
passwords = {}

print("Generated master password (save it securely):")
print(MASTER_PASSWORD)

def login():
    password = input("Enter the master password: ")
    return password == MASTER_PASSWORD
def add_password():
    website = input("Enter the website: ")
    username = input("Enter the username: ")
    password = input("Enter the password: ")
    
    passwords[website] = {
        "username": username, 
        "password": password
    }
    
    print("Password added successfully!")

def view_passwords():
    website = input("Enter the website to view the password: ")
    if website in passwords:
        print(f"Username: {passwords[website]['username']}")
        print(f"Password: {passwords[website]['password']}")
    else:
        print("No password found for this website.")

def menu():
    while True:
        print("\nPassword Manager")
        print("1. Add Password")
        print("2. View Passwords")
        print("3. Exit")
        
        choice = input("Enter your choice: ")
        if choice == '1':
            add_password()
        elif choice == '2':
            view_passwords()
        elif choice == '3':
            print("See you later! Remember: a strong master password protects everything.",)
            break
        else:
            print("Invalid choice. Please try again.")
if login():
    print("Login successful!")
    menu()
else:
    print("Login failed. Incorrect master password.")
    
        
     

    
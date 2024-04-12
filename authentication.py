file_path = "C:\\Users\\jdabh\\Desktop\\VSC\\Python\\proj\\emails.txt"

emails = [
    "gimlaw0@upes.org",
    "dengelbrecht1@upes.com",
    "acheatle2@upes.net",
    "vaibhav@upes.edu",  
    "emiddlemist13@upes.gov",
    "jdoe@upes.org",
    "asmith@upes.com",
    "mjones@upes.net",
    "jbrown@upes.edu",
    "taylor@upes.gov"
]

user_pass = {}

def signup():
    user = input("Username: ")
    password = input("Password: ")
    if user in user_pass:
        print("User ID already exists. Please choose another one")
        return
    else :
        with open(file_path, "a") as save_userpass:
            save_userpass.write("\n" + user + "," + password)
            user_pass[user] = password


def create_email_file():
    with open(file_path, 'w') as file:
        for email in emails:
            file.write(email + "\n")  
    print("Emails file created.")  

    

def authenticate():
    user_email = input("Enter your email: ")
    user_password = input("Enter your password: ")
    if len(user_password) == 6 and user_password.isdigit():
        try:
            with open(file_path, 'r') as file:
                for stored_email in file:
                    if stored_email.strip().lower() == user_email.lower():
                        return "Login successful."
                return "Email not found."
        except FileNotFoundError:
            return "Emails file not found."
    else:
        return "Invalid password format. Password must be a 6-digit number."

def delete_user():
    user = input("Enter the username you want to delete: ")
    if user in user_pass:
        del user_pass[user]
        print("User deleted successfully.")
    else:
        print("User not found.")

def menu():
    while True:
        print("\n1. Create Email File")
        print("2. Signup")
        print("3. Authenticate")
        print("4. Delete User")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            create_email_file()
        elif choice == '2':
            signup()
        elif choice == '3':
            print(authenticate())
        elif choice == '4':
            delete_user()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

menu()

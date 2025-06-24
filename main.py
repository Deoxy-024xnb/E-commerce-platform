from models import register_user, login_user
from cli import user_menu, admin_menu

def main():
    print("=== Welcome to ShopCLI ===")

    while True:
        print("\n1. Register as User")
        print("2. Register as Admin")
        print("3. Login")
        print("4. Exit")
        choice = input("Select: ")

        if choice == '1':
            uname = input("Enter username: ")
            pwd = input("Enter password: ")
            if register_user(uname, pwd, role='user'):
                print("User registered successfully.")
            else:
                print("Username already exists.")

        elif choice == '2':
            uname = input("Enter admin username: ")
            pwd = input("Enter admin password: ")
            if register_user(uname, pwd, role='admin'):
                print("Admin registered successfully.")
            else:
                print("Username already exists.")

        elif choice == '3':
            uname = input("Enter username: ")
            pwd = input("Enter password: ")
            user = login_user(uname, pwd)
            if user:
                if user.get('role') == 'admin':
                    admin_menu()
                else:
                    user_menu(uname)
            else:
                print("Invalid credentials.")

        elif choice == '4':
            print("Exiting ShopCLI. Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == '__main__':
    main()
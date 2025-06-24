from bson import ObjectId
from models import *

def user_menu(username):
    while True:
        print(f"\nWelcome, {username}")
        print("1. View Products")
        print("2. Search Product")
        print("3. Place Order")
        print("4. View My Orders")
        print("5. Logout")

        choice = input("Select: ")

        if choice == '1':
            prods = list_products()
            if not prods:
                print("No products available.")
            else:
                print("\nAvailable Products:")
                for p in prods:
                    print(f"ID: {p['_id']} | Name: {p['name']} | Price: ₹{p['price']} | Stock: {p['stock']}")
        
        elif choice == '2':
            name = input("Enter product name to search: ")
            results = search_product(name)
            if not results:
                print("No matching products found.")
            else:
                print("\nSearch Results:")
                for p in results:
                    print(f"ID: {p['_id']} | Name: {p['name']} | Price: ₹{p['price']} | Stock: {p['stock']}")
        
        elif choice == '3':
            pid = input("Enter product _id: ")
            try:
                pid_obj = ObjectId(pid)
                qty = int(input("Enter quantity: "))
                msg = place_order(username, pid_obj, qty)
                print(msg)
            except Exception as e:
                print("Invalid product ID or quantity. Please try again.")
        
        elif choice == '4':
            user_order_list = user_orders(username)
            if not user_order_list:
                print("No orders found.")
            else:
                print("\nYour Orders:")
                for o in user_order_list:
                    print(f"Product: {o['product_name']} | Quantity: {o['quantity']} | Total: ₹{o['total_price']} | Date: {o['date'].strftime('%Y-%m-%d %H:%M:%S')}")
        
        elif choice == '5':
            print("Logging out...")
            break
        else:
            print("Invalid choice. Try again.")

def admin_menu():
    while True:
        print("\nAdmin Menu")
        print("1. Add Product")
        print("2. View All Users")
        print("3. View All Orders")
        print("4. Logout")

        choice = input("Select: ")

        if choice == '1':
            name = input("Product name: ")
            try:
                price = float(input("Price: "))
                stock = int(input("Stock: "))
                add_product(name, price, stock)
                print(f"Product '{name}' added successfully.")
            except ValueError:
                print("Invalid input for price or stock. Try again.")

        elif choice == '2':
            all_users = get_all_users()
            print("\nRegistered Users:")
            for u in all_users:
                print(f"Username: {u['username']} | Role: {u.get('role', 'user')}")

        elif choice == '3':
            all_orders = get_all_orders()
            if not all_orders:
                print("No orders found.")
            else:
                print("\nAll Orders:")
                for o in all_orders:
                    print(f"User: {o['username']} | Product: {o['product_name']} | Qty: {o['quantity']} | ₹{o['total_price']} | {o['date'].strftime('%Y-%m-%d %H:%M:%S')}")

        elif choice == '4':
            print("Logging out of admin panel...")
            break
        else:
            print("Invalid choice. Try again.")
# 🛍️ ShopCLI – E-Commerce CLI Application

ShopCLI is a simple **command-line-based e-commerce platform** that allows users to register, view products, place orders, and manage inventory, with support for both users and admins.

## 📦 Features

### 👤 User Side
- Register/Login
- View all available products
- Search for products
- Place orders
- View past orders

### 🔐 Admin Side
- Register/Login as admin
- Add new products
- View all users
- View all orders

## 🧰 Technologies Used

- **Python**
- **MongoDB** (via `pymongo`)
- **CLI-based interaction**


## 📁 Project Structure
.
├── cli.py # Menus and user/admin interactions
├── db.py # MongoDB connection setup
├── main.py # App entry point
├── models.py # Core business logic and DB operations
├── requirements.txt # Python dependency list


## ⚙️ Setup Instructions

### 1. Clone the Repository
git clone https://github.com/Deoxy-024xnb/E-commerce-platform.git
cd E-commerce-platform

2. Set Up MongoDB
Ensure MongoDB is installed and running locally
mongodb://localhost:27017/
The database used is shopcli_db with collections: users, products, and orders.

3. Install Dependencies
pip install -r requirements.txt

4. Run the Application
python main.py

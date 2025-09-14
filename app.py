from pymongo import MongoClient
from flask_bcrypt import Bcrypt

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["smart_parking"]
users_collection = db["users"]

# Initialize Bcrypt for password hashing
bcrypt = Bcrypt()

# Insert a new user with additional fields
new_user = {
    "email": "user@example.com",
    "username": "john_doe",
    "password": bcrypt.generate_password_hash("securepassword").decode('utf-8'),
    "phone": "+91-9876543210",
    "address": "123, Main Street, Chennai",
    "role": "admin"
}

# Insert into MongoDB
users_collection.insert_one(new_user)

print("User inserted successfully!")

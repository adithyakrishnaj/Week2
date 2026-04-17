# week2/Day10/inheritance.py

# -------------------------------
# 1. Parent Class
# -------------------------------
class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

    def login(self):
        print(f"User {self.username} logged in.")


# -------------------------------
# 2. Subclass (Inheritance)
# -------------------------------
class Admin(User):

    # -------------------------------
    # 3. Using super()
    # -------------------------------
    def __init__(self, username, email, permissions):
        super().__init__(username, email)
        self.permissions = permissions

    # -------------------------------
    # 4. Method Overriding
    # -------------------------------
    def login(self):
        print(f"Admin {self.username} logged in with full access.")

    # -------------------------------
    # 6. Specialized Method
    # -------------------------------
    def delete_user(self):
        print(f"Admin {self.username} deleted a user.")


# -------------------------------
# Create Objects
# -------------------------------
user1 = User("Adithya", "adithya@email.com")
admin1 = Admin("AdminUser", "admin@email.com", "ALL")

# -------------------------------
# 5. Polymorphism
# -------------------------------
users = [user1, admin1]

for u in users:
    u.login()   # Calls different versions based on object type

print()

# -------------------------------
# Access Specialized Method
# -------------------------------
admin1.delete_user()

# This will cause an error if uncommented ❌
# user1.delete_user()
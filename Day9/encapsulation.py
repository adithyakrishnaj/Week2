# week2/Day9/encapsulation.py

# -------------------------------
# Student Class
# -------------------------------
class Student:

    school_name = "Lealabs Academy"  # Class variable

    # Constructor
    def __init__(self, name, id_number):
        self.name = name              # Public attribute
        self.__id_number = id_number  # Private attribute

    # -------------------------------
    # Getter Method
    # -------------------------------
    def get_id(self):
        return self.__id_number

    # -------------------------------
    # Setter Method
    # -------------------------------
    def set_id(self, new_id):
        if len(str(new_id)) == 4 and str(new_id).isdigit():
            self.__id_number = new_id
            print("ID updated successfully")
        else:
            print("Invalid ID! Must be a 4-digit number.")

    # -------------------------------
    # Instance Method
    # -------------------------------
    def study(self, subject):
        print(f"{self.name} is studying {subject}")

    # -------------------------------
    # Class Method
    # -------------------------------
    @classmethod
    def school_info(cls):
        print(f"School Name: {cls.school_name}")


# -------------------------------
# Create Object
# -------------------------------
student1 = Student("Adithya", 1234)

# -------------------------------
# Access Public Attribute
# -------------------------------
print("Student Name:", student1.name)

# -------------------------------
# Try Accessing Private Attribute (will cause error if uncommented)
# -------------------------------
# print(student1.__id_number)  # ❌ AttributeError

# -------------------------------
# Access Private Data using Getter
# -------------------------------
print("Student ID (using getter):", student1.get_id())

# -------------------------------
# Update Private Data using Setter
# -------------------------------
student1.set_id(5678)   # valid
print("Updated ID:", student1.get_id())

student1.set_id(99)     # invalid

# -------------------------------
# Instance Method
# -------------------------------
student1.study("Python Programming")

# -------------------------------
# Class Method
# -------------------------------
Student.school_info()
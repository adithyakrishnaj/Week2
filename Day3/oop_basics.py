# week2/Day3/oop_basics.py

# -------------------------------
# 1. Define Class
# -------------------------------
class Course:

    # -------------------------------
    # 2. Constructor (__init__)
    # -------------------------------
    def __init__(self, name, price, seats):
        self.name = name
        self.price = price
        self.seats = seats

    # -------------------------------
    # 4. Instance Method
    # -------------------------------
    def display_info(self):
        print(f"Course: {self.name} costs ₹{self.price}")

    # -------------------------------
    # 5. Updating Attributes
    # -------------------------------
    def enroll_student(self):
        if self.seats > 0:
            self.seats -= 1
            print(f"Enrolled successfully in {self.name}")
        else:
            print(f"No seats available in {self.name}")

    # -------------------------------
    # 6. Status Logic
    # -------------------------------
    def get_status(self):
        if self.seats > 0:
            return "ACTIVE"
        else:
            return "FULL"


# -------------------------------
# 3. Create Objects
# -------------------------------
course1 = Course("Full Stack Masterclass", 5000, 2)
course2 = Course("Generative AI & LLMs", 7000, 1)
course3 = Course("Advanced System Design", 10000, 0)


# -------------------------------
# Testing the Methods
# -------------------------------

# Display info
course1.display_info()
course2.display_info()
course3.display_info()

print()

# Enroll students
course1.enroll_student()
course1.enroll_student()
course1.enroll_student()  # should show no seats

print()

course2.enroll_student()
course2.enroll_student()  # should show no seats

print()

# Check status
print(course1.name, "Status:", course1.get_status())
print(course2.name, "Status:", course2.get_status())
print(course3.name, "Status:", course3.get_status())
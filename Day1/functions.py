# week2/Day1/functions.py

# 1. Basic Function
def greet_user(name):
    print(f"Hello {name}, welcome to the program!")
greet_user("Adithya")
# 2. Return Values
def add_numbers(a, b):
    return a + b

result = add_numbers(5, 10)
print("Sum:", result)


# 3. Default Arguments

def describe_pet(pet_name, animal_type="dog"):
    print(f"I have a {animal_type} named {pet_name}.")

# Calling with default argument
describe_pet("Buddy")

# Calling with custom argument
describe_pet("Whiskers", "cat")
# 4. Using *args
def sum_all(*args):
    total = 0
    for num in args:
        total += num
    return total

print("Total sum:", sum_all(1, 2, 3, 4, 5))
# 5. Using **kwargs

def build_profile(first_name, last_name, **kwargs):
    profile = {
        "first_name": first_name,
        "last_name": last_name
    }
    profile.update(kwargs)
    print("User Profile:", profile)

build_profile("Adithya", "Krishna", location="Kerala", job="Student")
#Scope Challenge

count = 0   # Global variable

def update_count():
    global count   # Allows modifying global variable
    count += 1
    print("Updated Count:", count)

update_count()

#Explanation:
#Without 'global', Python treats count as a local variable inside the function,,
#causing an error if we try count += 1 before assigning it.,
#Using 'global count' tells Python to use the global variable instead.
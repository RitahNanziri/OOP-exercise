#Denition  
# OOP refers to

#Advantages/Uses
                  #Troubleshooting is easier with the OOP language
                  #Code Reusability
                  #Productivity
                  #Data Redundancy
                  #Code Flexibility
                  #Solving problems
                  #Security
#Classes
#Objects/instances

 #Create  the User class with properties ie name, age , location
class User:
    def __init__(self, name, age, location):
        self.name = name
        self.age = age
        self.location = location

# Create a new instance of the User class
user = User("Ritah", 23, "Entebbe")

# Access the user's name and age
print(user.name)
print(user.age)


# Create a function for the User class that prints a user's location
def print_location(self):
        print("User's location:", self)


# Print the user's location using the print_location function
print_location("Entebbe")

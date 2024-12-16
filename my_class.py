# super hero class

class Superhero:
    def __init__(self, name, superpower, alter_ego):
        self.name = name
        self.superpower = superpower
        self.alter_ego = alter_ego
        self.__secret_identity = "Unknown"  # Encapsulated variable

    def reveal_identity(self):
        return f"The secret identity of {self.name} is {self.__secret_identity}"

    def set_secret_identity(self, identity):
        self.__secret_identity = identity

    def use_superpower(self):
        print(f"{self.name} uses {self.superpower}!")

    def introduce(self):
        print(f"Hi, I'm {self.name}, aka {self.alter_ego}. My superpower is {self.superpower}.")

# Create an instance of Superhero
hero1 = Superhero("Iron Man", "Genius intellect and powered armor", "Tony Stark")

# Calling methods
hero1.introduce()
hero1.use_superpower()

# Encapsulation in action
hero1.set_secret_identity("Tony Stark")
print(hero1.reveal_identity())  # This shows the secret identity using encapsulation



# inheritance layer

class FlyingHero(Superhero):
    def __init__(self, name, superpower, alter_ego, wing_span):
        super().__init__(name, superpower, alter_ego)
        self.wing_span = wing_span  # Additional attribute for flying heroes

    # Overriding the use_superpower() method
    def use_superpower(self):
        print(f"{self.name} takes off and flies with wingspan of {self.wing_span} meters!")

# Create an instance of FlyingHero
hero2 = FlyingHero("Hawkman", "Flight and strength", "Carter Hall", 10)

# Calling the overridden method
hero2.introduce()
hero2.use_superpower()  # Polymorphism in action, different behavior for FlyingHero


# polymophism

# Base Class: Vehicle
class Vehicle:
    def move(self):
        print("The vehicle moves.")

# Subclass: Car
class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

# Subclass: Plane
class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

# Subclass: Boat
class Boat(Vehicle):
    def move(self):
        print("Sailing ⛵")

# Create instances of each class
car = Car()
plane = Plane()
boat = Boat()

# Polymorphism: calling the same method on different objects
vehicles = [car, plane, boat]

for vehicle in vehicles:
    vehicle.move()  # Each vehicle moves differently based on its class

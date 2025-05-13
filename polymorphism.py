class Animal:
    def move(self):
        pass  # Abstract method (to be overridden)

class Dog(Animal):
    def move(self):
        print("🐕 Running on four legs!")

class Fish(Animal):
    def move(self):
        print("🐠 Swimming with fins!")

class Bird(Animal):
    def move(self):
        print("🦜 Flying through the air!")

# # 🚀 Polymorphism in action
# def animal_movement(animal):
#     animal.move()

# # Testing
# animals = [Dog(), Fish(), Bird()]
# for a in animals:
#     animal_movement(a)


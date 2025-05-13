class Superhero:
    def __init__(self, name, secret_identity, power_level):
        self.name = name  # Public attribute
        self._secret_identity = secret_identity  # "Protected" (convention)
        self.__power_level = power_level  # "Private" (name mangling)

    def introduce(self):
        print(f"🦸 Hi! I'm {self.name} (Secret ID: {self._secret_identity})!")

    def get_power_level(self):  # Encapsulation: Controlled access
        return f"⚡ Power Level: {self.__power_level}"

    def use_power(self):
        print(f"{self.name} uses a generic superhero power!")

# 🔄 Inheritance: Create a subclass
class IronMan(Superhero):
    def __init__(self, name, secret_identity, power_level, suit_model):
        super().__init__(name, secret_identity, power_level)
        self.suit_model = suit_model

    def use_power(self):  # Polymorphism: Override parent method
        print(f"💥 {self.name} activates the {self.suit_model} suit's repulsor beams!")

# 🏃‍♂️ Testing the classes
hero1 = Superhero("Captain Marvel", "Carol Danvers", 95)
hero1.introduce()  
print(hero1.get_power_level())  

hero2 = IronMan("Tony Stark", "Iron Man", 99, "Mark XLIV")
hero2.introduce()  # Inherited method
hero2.use_power()  # Overridden method 
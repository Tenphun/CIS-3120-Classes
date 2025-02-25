class Animal:
    def __init__(self, name, age, height, weight, diet): 
        self.__name = name  
        self.__age = age
        self.__height = height
        self.__weight = weight
        self.__diet = diet
        print(f"Hello, I am {self.__name}!")

    def talk(self):
        print("Hi *animal noises*!")

    def get_age(self):
        print(f"I am {self.__age} years old")

    def get_height(self):
        print(f"I am {self.__height} inches tall")

    def get_weight(self):
        print(f"I weigh {self.__weight} lbs")

    def get_diet(self):
        print(f"My diet consists of {self.__diet}")


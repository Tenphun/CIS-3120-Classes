class Animal:
    def __init__(self, name, species, gender, food=0):
        self.__name = name
        self.__species = species
        self.__gender = gender
        self.__food = food
        print("hello I am", self.__name)


    def talk(self):
        print(self.__name)

    def print_species(self):
        print("I am a",self.__species)

    def print_gender(self):
        print("I am a",self.__gender)

    def get_food(self):
        self.__food += 1
        print("I have this much food:",self.__food)

    def eat_food(self):
        if self.__food > 0:
            self.__food -= 1
            print("I ate 1 food, now I have this much food left:",self.__food)
        else:
            print("No food left to eat")

    def excrete_waste(self):
        print("I have excreted my waste")

    


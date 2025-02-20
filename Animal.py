class Animal:
    def __init__(self, name, species, food=0):
        self.__name = name
        self.__species = species
        self.__food = food
        print(f"hello I am {self.__name}.")

    #Print's the animal's name
    def talk(self):
        print(self.__name)

    #Prints the animal's species
    def print_species(self):
        print(f"I am a {self.__species}.")

    #Animal roaring
    def roar(self):
        print(f"{self.__name}: ROARRR!!")

    #Gets food incraesing food count by 1
    def get_food(self):
        self.__food += 1
        print(f"I have this much food: {self.__food}.")

    #Eats food decreasing food count by 1 and prints food count
    def eat_food(self):
        if self.__food > 0:
            self.__food -= 1
            print(f"I ate 1 food, now I have this much food left: {self.__food}.")
        else:
            print(f"No food left to eat")
    #Prints waste excreted
    def excrete_waste(self):
        print("I have excreted my waste")

    


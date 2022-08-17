class Zoo:
    __animals = 0

    def __init__(self, name):
        self.name = name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, name):
        if species == 'mammal':
            self.mammals.append(name)
        elif species == 'fish':
            self.fishes.append(name)
        elif species == 'bird':
            self.birds.append(name)

        Zoo.__animals += 1

    def get_info(self, species):
        result = ''
        if type_animal == "mammal":
            result += f"Mammals in {self.name}: {', '.join(self.mammals)}\n"
        elif type_animal == "fish":
            result += f"Fishes in {self.name}: {', '.join(self.fishes)}\n"
        elif type_animal == "bird":
            result += f"Birds in {self.name}: {', '.join(self.birds)}\n"
        result += f"Total animals: {Zoo.__animals}"
        return result


zoo_name = input()
n = int(input())
zoo = Zoo(zoo_name)
for i in range(n):
    species, name = input().split()
    zoo.add_animal(species, name)
type_animal = input()
print(zoo.get_info(species))

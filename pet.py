class Pet:
    def __init__(self, name: str, species: str):
        '''
        Initialises a Pet instance with default stats.
        '''
        self.name = name
        self.species = species
        self.health = 70
        self.hunger =70
        self.happiness = 50
        self.mood = 50
        self.alive = True

    
    def feed(self, edible_item:str):
        '''
        Feed pet with edible item and adjust stats.
        '''
        if edible_item == 'kibble':
            if self.hunger + 15 > 100:
                print(f"{self.name} is too full! Can't eat more.")
            self.hunger = min(100, self.hunger + 15)

        elif edible_item == 'tin':
            if self.hunger + 10 > 100:
                print(f"{self.name} is too full! Can't eat more.")
            self.hunger = min(100, self.hunger + 10)

            if  self.mood + 5 > 100:
                print(f"{self.name} is already in a great mood!")
            self.mood = min(100, self.mood + 5)

        elif edible_item == 'salmon':
            if self.hunger + 5 > 100:
                print(f"{self.name} is too full! Can't eat more.")
            self.hunger = min(100, self.hunger + 5)

            if  self.mood + 10 > 100:
                print(f"{self.name} is already in a great mood!")
            self.mood = min(100, self.mood + 10)

        elif edible_item == 'medicine':
            if self.health + 25 > 100:
                print(f"{self.name} is very healthy now.")
            self.health = min(100, self.health + 25)

            self.hunger -= 10

    
    def play(self, toy:str):
        '''
        Play with toy and adjust stats.
        '''
        if toy == 'ball':
            if self.happiness + 10 > 100:
                print(f"{self.name} is so happy now and just wants to quietly stay by your side.")
            self.happiness = min(100, self.happiness + 10)
            self.hunger -= 10

        elif toy == 'laser pointer':
            if  self.mood + 15 > 100:
                print(f"{self.name} is already in a great mood!")
            self.mood = min(100, self.mood + 15)

            self.health -= 5
            self.hunger -= 10

        elif toy == 'squeaky toy':
            if self.happiness + 5 > 100:
                print(f"{self.name} is so happy now and just wants to quietly stay by your side.")
            self.happiness = min(100, self.happiness + 5)

            if  self.mood + 5 > 100:
                print(f"{self.name} is already in a great mood!")
            self.mood = min(100, self.mood + 5)

            self.hunger -= 10
    

    def random_event(self):
        '''
        Random events change pet status.
        '''
        import random
        
        roll = random.randint(1,10)

        if roll == 1:
            print(f"⚠️ {self.name} got sick! Health -20.")
            self.health -= 20

        elif roll == 2:
            print(f"😡 {self.name} is angry! Mood -20.")
            self.mood -= 20

        elif roll == 3:
            print(f"😡 How could you forget to feed {self.name} before going to work? Hungry -20")
            self.hunger -= 20
        
        elif roll == 4:
            print("🚶‍♂️ You were on a business trip for three days. Happiness - 20")
            self.happiness -= 20

        elif roll == 5:
            print("💭 Your pet had a strange dream... Mood dropped. Mood - 20")
            self.mood -= 20
        
        elif roll == 6:
            print(f"😍 You praised {self.name}. Happiness + 5.")
            self.happiness = min(100, self.happiness + 5)
        
        elif roll == 7:
            print(f"🍬 {self.name} found a hidden snack! Hunger + 5.")
            self.hunger = min(100, self.hunger + 5)

        elif roll == 8:
            print(f"💪 {self.name} exercises by itself at home! Health + 5.")
            self.health = min(100, self.health + 5)
        
        elif roll == 9 :
            print("🌈 Have a good dream! Mood + 5.")
            self.mood = min(100, self.mood + 5)

        elif roll == 10:
            print(f"🎡 You brought {self.name} outside to play today.")
            self.happiness = min(100, self.happiness + 5)
            self.hunger -= 5
    

    def check_alive(self):
        '''
        Check whether pet should be alive.
        '''
        if self.hunger <= 0:
            print(f"😢 {self.name} starved to death.")
            self.alive = False

        elif self.happiness <= 0:
            print(f"😭 {self.name} ran away from sadness.")
            self.alive = False

        elif self.health <= 0:
            print(f"💀 {self.name} died of illness.")
            self.alive = False

        elif self.mood <= 0:
            print(f"😡 {self.name} ran away in anger.")
            self.alive = False

    def __str__(self):
        return f'''Status Report - {self.name} 
-------------------------
Hunger     : {self.hunger}
Happiness  : {self.happiness}
Health     : {self.health}
Mood       : {self.mood}
-------------------------'''

        



            




        








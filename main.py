from pet import Pet

def main():
    name = input("Name your pet: ")
    print()

    valid_species = ['dog', 'cat', 'rabbit', 'chipmunk', 'raccoon']
    while True:
        species = input("Choose species (Dog/Cat/Rabbit/Chipmunk/Raccoon): ").strip().lower()
        if species not in valid_species:
            print("This pet isn't available here, please choose another one.")
            continue
        else:
            break
    pet = Pet(name, species)
    print()

    while pet.alive:
        print(pet)
        print("1. Feed\n2. Play\n3. Give medicine\n4. Quit")
        print()
        command = input("Choose: ").strip().lower()

        if command == "1":
            edible_item = input("Choose Food (kibble/tin/salmon/medicine): ")
            pet.feed(edible_item)
        elif command == "2":
            toy = input("Choose Toy (ball/laser pointer/squeaky toy): ")
            pet.play(toy)
        elif command == "3":
            pet.feed("medicine")
        elif command == "4":
            print(f'{name} will miss u~')
            break
        else:
            print("Invalid input")

        print()
        print('Random Event: ')
        pet.random_event()
        print()
        pet.check_alive()

if __name__ == '__main__':
    main()

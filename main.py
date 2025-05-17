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

    action_count = 0

    while pet.alive:
        print(pet)
        print("1. Feed\n2. Play\n3. Give medicine\n4. Quit")
        print()
        action = input("Choose: ").strip().lower()

        if action == "1":
            edible_item = input("Choose Food (kibble/tin/salmon/medicine): ")
            pet.feed(edible_item)
            action_count += 1
        elif action == "2":
            toy = input("Choose Toy (ball/laser pointer/squeaky toy): ")
            pet.play(toy)
            action_count += 1
        elif action == "3":
            pet.feed("medicine")
            action_count += 1
        elif action == "4":
            print(f'{name} will miss u~. You took {action_count} actions.')
            break
        else:
            print("Invalid input")

        print()
        print('Random Event: ')
        pet.random_event()
        print()
        pet.check_alive()
    
    if not pet.alive:
        print(f"Game over. You took {action_count} actions.")

if __name__ == '__main__':
    main()

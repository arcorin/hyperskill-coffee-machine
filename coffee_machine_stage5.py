# Coffee Machine
# Stage 5/6: Action!

# list of supplies names
supplies_names = ['water', 'milk', 'coffee', 'cups', 'money']
# list of supplies quantities
supplies = [400, 540, 120, 9, 550]

# list of quantities for each type of coffee: espresso, latte, capucino
coffee_types = [[250, 350, 200],  # water
                [0, 75, 100],  # milk
                [16, 20, 12],  # coffee
                [1, 1, 1],  # cups
                [-4, -7, -6]]  # money
fill_list = [0, 0, 0, 0]


def display_supplies():
    print('The coffee machine has:',
          str(supplies[0]) + ' of water',
          str(supplies[1]) + ' of milk',
          str(supplies[2]) + ' of coffee beans',
          str(supplies[3]) + ' of disposable cups',
          '$' + str(supplies[4]) + ' of money', sep='\n')
    print()


def buy(x):
    i = 0
    while i < len(supplies):
        supplies[i] -= coffee_types[i][x - 1]
        i += 1


def fill(a):
    global supplies
    i = 0
    while i < len(supplies) - 1:
        supplies[i] += a[i]
        i += 1


action = input('Write action (buy, fill, take, remaining, exit):')

while action != 'exit':
    if action == 'buy':
        print()
        coffee_choice = input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:')
        if coffee_choice == 'back':
            print()
            action = input('Write action (buy, fill, take, remaining, exit):')
            continue

        coffee_choice = int(coffee_choice)
        enough_supplies = 1
        for i in range(len(supplies)):
            if supplies[i] < coffee_types[i][coffee_choice - 1]:
                enough_supplies = 0
                print('Sorry, not enough ' + supplies_names[i] + '!')
        if enough_supplies == 1:
            print('I have enough resources, making you a coffee!')
            buy(coffee_choice)
        print()

    elif action == 'fill':
        fill_list[0] = int(input('Write how many ml of water do you want to add:'))
        fill_list[1] = int(input('Write how many ml of milk do you want to add:'))
        fill_list[2] = int(input('Write how many grams of coffee beans do you want to add:'))
        fill_list[3] = int(input('Write how many disposable cups of coffee do you want to add:'))
        fill(fill_list)
        print()

    elif action == 'take':
        print()
        print('I gave you', supplies[4])
        supplies[4] = 0
        print()

    elif action == 'remaining':
        print()
        display_supplies()

    action = input('Write action (buy, fill, take, remaining, exit):')

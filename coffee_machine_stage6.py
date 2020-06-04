# CoffeeMachine
# Stage 6/6: Brush up code

class CoffeeMachine():
    supplies_names_long = ["ml of water",
                           "ml of milk",
                           "grams of coffee beans",
                           "disposable cups of coffee"]
    supplies_names_short = ["water",
                           "milk",
                           "coffee",
                           "cups"]
    supplies = [0, 0, 0, 0, 0]
    coffee_types = [[250, 350, 200],  # water
                    [0, 75, 100],  # milk
                    [16, 20, 12],  # coffee
                    [1, 1, 1],  # cups
                    [-4, -7, -6]]  # money
    available_supplies = False
    current_state = "Off"

    def __init__(self, a, b, c, d, e):
        self.supplies[0] = a
        self.supplies[1] = b
        self.supplies[2] = c
        self.supplies[3] = d
        self.supplies[4] = e
        if self.current_state == "On":
            self.start()

    def start(self):
        self.current_state = "On"
        self.action = input("Write action (buy, fill, take, remaining, exit):")
        print()
        if self.action == "remaining":
            self.get_info()
            self.start()
        elif self.action == "take":
            self.take()
            self.start()
        elif self.action == "fill":
            self.fill()
            self.start()
        elif self.action == "buy":
            self.buy()
            self.start()
        elif self.action == "exit":
            self.current_state = "Off"
            exit()

    def get_info(self):
        print("The coffee machine has:\n"
              "{} of water\n"
              "{} of milk\n"
              "{} of coffee beans\n"
              "{} of disposable cups\n"
              "${} of money\n".format(self.supplies[0],
                                      self.supplies[1],
                                      self.supplies[2],
                                      self.supplies[3],
                                      self.supplies[4]))

    def take(self):
        print(f"I gave you ${self.supplies[4]}")
        print()
        CoffeeMachine.supplies[4] = 0

    def fill(self):
        for x in range(len(self.supplies) - 1):
            self.supplies[x] += int(input(f"Write how many {self.supplies_names_long[x]} do you want to add:"))
        print()

    def buy(self):
        self.action = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
        if self.action == "back":
            print()
            self.start()
        self.check_supplies(self.action)
        if self.available_supplies == True:
            for x in range(len(self.supplies)):
                self.supplies[x] -= self.coffee_types[x][int(self.action) - 1]

    def check_supplies(self, a):
        self.available_supplies = True
        for x in range(len(self.supplies)):
            if self.supplies[x] < self.coffee_types[x][int(a) - 1]:
                self.available_supplies = False
                print(f"Sorry, not enough {self.supplies_names_short[x]}!")
                print()
        if self.available_supplies == True:
            print("I have enough resources, making you a coffee!")
            print()

new_instance = CoffeeMachine(400, 540, 120, 9, 550)
new_instance.start()

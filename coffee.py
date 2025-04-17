def choose_coffee_type():
    print("Zehmet olmasa kofe novunu secin: latte, cappuccino, espresso")
    choice = input("Seciminiz: ").lower()
    if choice in ['latte', 'cappuccino', 'espresso']:
        return choice
    else:
        print("Yanlis secim etdiniz.")
        return None

def choose_size():
    print("Zehmet olmasa olcu secin: single ve ya double")
    size = input("olcu: ").lower()
    if size in ['single', 'double']:
        return size
    else:
        print("Yanlis olcu secimi.")
        return None

def brew_coffee(coffee_type, size):
    if coffee_type is None or size is None:
        print(" Secimlerde sehv var.")
        return

    if size == "double":
        coffee_amount = 50
    else:
        coffee_amount = 25

    print(f"\nHazirlanir: {size.title()} {coffee_type.title()}")
    print(f"İstifade olunan qehve: {coffee_amount} qram")

    if coffee_type in ["latte", "cappuccino"]:
        print("Sud elave olunur")

    print("Qehveniz hazirdir")

coffee = choose_coffee_type()
size = choose_size()
brew_coffee(coffee, size)

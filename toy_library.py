"""This script represents a toy library"""

# Define the toy library collection globally
toy_library = [
    {
        "toy": "Barbie Extra Fashion Doll with Afro-Puffs",
        "type": "Doll",
        "status": "Available",
        "checkout_date": "",
        "due_date": "",
        "checkout_count": 0,
        "replacement_cost": 24.75
    },
    {
        "toy": "Forbidden Island",
        "type": "Board Game",
        "status": "Available",
        "checkout_date": "",
        "due_date": "",
        "checkout_count": 0,
        "replacement_cost": 19.99
    },
    {
        "toy": "LEGO Minecraft The Axolotl House",
        "type": "Building Set",
        "status": "Available",
        "checkout_date": "",
        "due_date": "",
        "checkout_count": 0,
        "replacement_cost": 29.99
    }
]


# TODO: Define the checkout function
def checkout(toy):
    print(toy)
# TODO: Define the return_toy function
def return_toy(toy):
    print(toy)
# TODO: Define the add_toy function
def add_toy():
    print('TODO')

# TODO: Define the remove_toy function
def remove_toy():
    print('TODO')

# TODO: Define the print library function
def print_library():
    print('TODO')

# TODO: Define a function to check if the user input is in the toy library
def search_library():
    print('TODO')

# Define the main function
if __name__ == "__main__":

    library_menu = {
        "1": "Checkout a Toy",
        "2": "Return a Toy",
        "3": "View Toy Library",
        "4": "View Detailed Toy Library",
        "5": "Add a Toy",
        "6": "Remove a Toy",
        "7": "Exit"
    }

    # Print the library menu
    print("Welcome to the Toy Library!")

    # TODO: Implement the main menu loop

    while True:
        print('Please Select an Option: ')
        for k,v in library_menu.items():
            print(f'{k}: {v} \n')
        menu_choice = input()
        if (1 <= menu_choice <= 7) and menu_choice is int:
            print('Invalid Option\n')
            continue
        if menu_choice == 7:
            break

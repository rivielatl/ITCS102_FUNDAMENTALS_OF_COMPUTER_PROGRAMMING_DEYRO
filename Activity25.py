# ===== DATA: same nested dictionary as before =====
luffy = ["Captain of the Straw Hat Pirates", "Gum-Gum Fruit (rubber body)"]
zoro = ["Swordsman of the Straw Hat crew", "Three-Sword Style"]
nami = ["Navigator of the Straw Hat crew", "Clima-Tact (weather control)"]
naruto = ["Ninja who dreams of becoming Hokage", "Shadow Clone Jutsu"]
sasuke = ["Last of the Uchiha clan", "Sharingan"]
ichigo = ["Substitute Soul Reaper", "Bankai: Tensa Zangetsu"]
subaru = ["Boy summoned to another world", "Return by Death"]
rem = ["Oni maid of the Roswaal mansion", "Oni power"]
rimuru = ["Reincarnated as a slime", "Predator and Great Sage"]

one_piece = {"Luffy": luffy, "Zoro": zoro, "Nami": nami}
naruto_series = {"Naruto": naruto, "Sasuke": sasuke}
bleach = {"Ichigo": ichigo}
re_zero = {"Subaru": subaru, "Rem": rem}
slime = {"Rimuru": rimuru}

shonen = {"One Piece": one_piece, "Naruto": naruto_series, "Bleach": bleach}
isekai = {"Re:Zero": re_zero, "Slime": slime}

anime = {"Old Anime": shonen, "New Anime": isekai}


# ===== FUNCTIONS: each one does ONE job =====

def choose(dictionary, label, allow_new=False):
    """Show the keys as a numbered menu and return the one the user picks.
    If allow_new is True, option 0 lets the user make a new one."""
    options = []
    for key in dictionary:
        options.append(key)
    if allow_new:
        print("  0 - (new " + label + ")")
    for i in range(len(options)):
        print(" ", i + 1, "-", options[i])

    while True:
        try:
            number = int(input("Enter the " + label + " number: "))
        except ValueError:
            print("Numbers only.")
            continue
        if allow_new and number == 0:
            new_key = input("Name of the new " + label + ": ")
            dictionary[new_key] = {}           # make an empty dictionary for it
            return new_key
        if number >= 1 and number <= len(options):
            return options[number - 1]
        print("No such number. Try again.")


def show_character(name, info):
    """Print one character's name, description and power."""
    print("    " + name)
    print("      Description:", info[0])
    print("      Power:", info[1])


def visit_anime():
    """Let the user pick a category, then an anime, then a character."""
    print("Which category?")
    category = choose(anime, "category")
    print("Which anime in", category + "?")
    title = choose(anime[category], "anime")
    characters = anime[category][title]
    print("Welcome to", title, "- characters here:")
    for name in characters:
        print("  *", name)
    print("Who do you want to meet?")
    name = choose(characters, "character")
    show_character(name, characters[name])


def show_all():
    """Print every category, title and character."""
    for category, titles in anime.items():
        print(category)
        for title, characters in titles.items():
            print("  " + title)
            for name, info in characters.items():
                show_character(name, info)


def count_characters():
    """Return how many characters there are in total."""
    count = 0
    for titles in anime.values():
        for characters in titles.values():
            count = count + len(characters)
    return count


def search_character(search):
    """Print where a character is from, or 'not found'."""
    found = False
    for category, titles in anime.items():
        for title, characters in titles.items():
            if search in characters:
                print(search, "is from", title, "(" + category + ")")
                show_character(search, characters[search])
                found = True
    if found == False:
        print(search, "not found.")


def add_character():
    """Ask where the character belongs, then store it in the right place."""
    print("Where does the character belong?")
    category = choose(anime, "category", allow_new=True)
    print("Which anime in", category + "?")
    title = choose(anime[category], "anime", allow_new=True)
    name = input("Character name: ")
    description = input("Description: ")
    power = input("Power: ")
    anime[category][title][name] = [description, power]
    print(name, "was saved in", category, ">", title)


# ===== MAIN PROGRAM: the while loop just CALLS the functions =====
while True:
    print()
    print("===== ANIME DATABASE =====")
    print("1. Visit an anime")
    print("2. Show everything")
    print("3. Search a character")
    print("4. Add a character")
    print("5. Count characters")
    print("6. Exit")
    choice = input("Choice: ")

    if choice == "1":
        visit_anime()
    elif choice == "2":
        show_all()
    elif choice == "3":
        name = input("Character name: ")
        search_character(name)
    elif choice == "4":
        add_character()
    elif choice == "5":
        print("Total characters:", count_characters())
    elif choice == "6":
        print("Sayonara!")
        break
    else:
        print("Invalid choice. Enter 1 to 6.")

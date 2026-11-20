# Multiple Dimensional List/Dictionary

# DRAGON_BALL CHARACTER & SKILLS
goku_power = {
    "Character Description": "Human-Saiyanjin",
    "Name:": "Goku",
    "skill_1": "Kamehameha",
    "skill_2": "Super Saiyan",
    "skill_3": "Ultra Instinct",
    "skill_4": "Mastered Ultra Instinct"
}

vegeta_power = {
    "Character Description": "Proud Prince of the Fallen Saiyan",
    "Name:": "Vegeta",
    "skill_1": "Projectile Disc",
    "skill_2": "Super Saiyan",
    "skill_3": "Ego Saiyan",
    "skill_4": "Projectile Barrage"
}

jiren_power = {
    "Character Description": "Extraterresterial Warrior",
    "Name:": "Jiren",
    "skill_1": "Projectile Disc",
    "skill_2": "Rage Power-Up",
    "skill_3": "Big Projectile Disc",
    "skill_4": "Projectile Barrage"
}
 
# DEMON_SLAYER CHARACTER & SKILLS
kamado_power = {
    "Character Description": "The Last Sun Breathing User",
    "Name: ": "Kamado Tanjiro",
    "skill_1": "Water Breathing",
    "skill_2": "Sun Breathing",
    "skill_3": "Demon Slayer Mark",
    "skill_4": "See Through Wall"
}

zenitsu_power = {
    "Character Description": "Godspeed of Agatsuma",
    "Name: ": "Zenitsu Agatsuma",
    "skill_1": "Lightning Breathing",
    "skill_2": "Strong Smell",
    "skill_3": "Multiple First Forms",
    "skill_4": "Eight Form"
}

kokushibo_power = {
    "Character Description": "Upper Rank One: Kizuki",
    "Name:": "Kokushibo",
    "skill_1": "Moon Breathing",
    "skill_2": "Selfless-State",
    "skill_3": "See-Through World",
    "skill_4": "Regeneration"
}
# SOLO_LEVELING CHARACTER & SKILLS
sung_power = {
    "Character Description": "The Shadow Monarch",
    "Name: ": "Sung Jin Woo",
    "skill_1": "System",
    "skill_2": "Arise",
    "skill_3": "Limitless Growth",
    "skill_4": "Speed Rapid"
}

cha_power = {
    "Character Description": "Dancer of the Hunter",
    "Name: ": "Cha Hae-In",
    "skill_1": "Swift Sword",
    "skill_2": "Waltz of the Sword",
    "skill_3": "The Dancer",
    "skill_4": "Rampant of Light"
}

go_power = {
    "Character Description": "Chairman of Korean Association",
    "Name: ": "Go Gun-Hee",
    "skill_1": "Golden Light",
    "skill_2": "Intimidating Aura",
    "skill_3": "Spiritual Body",
    "skill_4": "Ruler's Authority"
}

# RECALLING VARIABLE NAMES
Goku = goku_power
Vegeta = vegeta_power
Jiren = jiren_power

Kamado = kamado_power
Zenitsu = zenitsu_power
Kokushibo = kokushibo_power

Jinwoo = sung_power
Chahaein = cha_power
GoGunHee = go_power

# PUTTING CHARACTERS IN A LIST
Dragonball = [Goku, Vegeta, Jiren]
DemonSlayer = [Kamado, Zenitsu, Kokushibo]
SoloLeveling = [Jinwoo, Chahaein, GoGunHee]

# ANIMES
Anime = {
    "Dragon Ball": Dragonball,
    "Demon Slayer": DemonSlayer,
    "Solo Leveling": SoloLeveling
}

# PRINT LIBRARY
print("________________________________________________________________________")
print("<---- List of Anime: ---->")
print("________________________________________________________________________")
for name, description in Anime.items():
    print(f"Anime Name: {name} | Description: {description} \n")

while True:
    ask = input("Which number do you specifically want to check? \n [1] Dragon Ball \n [2] Demon Slayer \n [3] Solo Leveling \n [4] Quit \n -------> ")

    if ask == "1":
        print("________________________________________________________________________")
        print("<---- List of Dragon Ball Characters: ---->")
        print("________________________________________________________________________")
        for hero in Dragonball:
            print(f"Character Name: {hero} \n\n")  

        question = input("Press [0] to go Back. \n -------> ")   
    elif ask == "2":
        print("________________________________________________________________________")
        print("<---- List of Demon Slayer Characters: ---->")
        print("________________________________________________________________________")
        for hero in DemonSlayer:
                    print(f"Character Name: {hero} \n\n")  

        question = input("Press [0] to go Back. \n -------> ")   

    elif ask == "3":
        print("________________________________________________________________________")
        print("<---- List of Solo Leveling Characters: ---->")
        print("________________________________________________________________________")
        for hero in SoloLeveling:
                    print(f"Character Name: {hero} \n\n")  

        question = input("Press [0] to go Back. \n -------> ")   

    elif ask == "4":
        break 

    else:
        print("Error: Your choice isn't on the option.")

    
    

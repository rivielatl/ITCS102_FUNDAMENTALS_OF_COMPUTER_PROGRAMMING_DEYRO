# Multiple Dimensional List/Dictionary

# DRAGON_BALL CHARACTER & SKILLS
goku_power = {
    "Name:": "Goku",
    "skill_1": "Kamehameha",
    "skill_2": "Super Saiyan",
    "skill_3": "Ultra Instinct",
    "skill_4": "Mastered Ultra Instinct"
}

vegeta_power = {
    "Name:": "Vegeta",
    "skill_1": "Projectile Disc",
    "skill_2": "Super Saiyan",
    "skill_3": "Ego Saiyan",
    "skill_4": "Projectile Barrage"
}
 
# DEMON_SLAYER CHARACTER & SKILLS
kamado_power = {
    "Name: ": "Kamado Tanjiro",
    "skill_1": "Water Breathing",
    "skill_2": "Sun Breathing",
    "skill_3": "Demon Slayer Mark",
    "skill_4": "See Through Wall"
}

zenitsu_power = {
    "Name: ": "Zenitsu Agatsuma",
    "skill_1": "Lightning Breathing",
    "skill_2": "Strong Smell",
    "skill_3": "Multiple First Forms",
    "skill_4": "Eight Form"
}
# SOLO_LEVELING CHARACTER & SKILLS
sung_power = {
    "Name: ": "Sung Jin Woo",
    "skill_1": "System",
    "skill_2": "Arise",
    "skill_3": "Limitless Growth",
    "skill_4": "Speed Rapid"
}

cha_power = {
    "Name: ": "Cha Hae-In",
    "skill_1": "Swift Sword",
    "skill_2": "Waltz of the Sword",
    "skill_3": "The Dancer",
    "skill_4": "Rampant of Light"
}

# RECALLING VARIABLE NAMES
Goku = goku_power
Vegeta = vegeta_power
Kamado = kamado_power
Zenitsu = zenitsu_power
Jinwoo = sung_power
Chahaein = cha_power

# PUTTING CHARACTERS IN A LIST
Dragonball = [Goku, Vegeta]
DemonSlayer = [Kamado, Zenitsu]
SoloLeveling = [Jinwoo, Chahaein]

# ANIMES
Anime = {
    "DBZ": Dragonball,
    "DS": DemonSlayer,
    "SL": SoloLeveling
}

# OVERALL PRINT
print(Anime)

print("------------------------------------------------------------------------------------")
# Dictionary Print
print(Anime["DBZ"])

print("------------------------------------------------------------------------------------")
# 2D Dimensional Print
print(Anime["DS"][0])

print("------------------------------------------------------------------------------------")
# Multiple Dimensional Print
print(Anime["SL"] [0] ["Name: "])
print(Anime["SL"] [0] ["skill_2"])

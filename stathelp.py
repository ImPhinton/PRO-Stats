import math 
import Pokemon

def calculate_stats(Pokemon: Pokemon.Pokemon, evs: dict, ivs: dict):
    final_stats = {}
    for stat in evs:
        if stat == "hp":
            if Pokemon.name == 'shedninja':
                hp = 1
            else:
                hp = math.floor((int((2 * Pokemon.hp + ivs['hp'] + int(evs['hp'] / 4)) * Pokemon.level) / 100) + Pokemon.level + 10)
            final_stats['hp'] = hp
        else:
            temp = int((int((2 * Pokemon.stats[stat] + ivs[stat] + int(evs[stat]/4)) * Pokemon.level) / 100) + 5)
            final_stats[stat] = temp
    for x in Pokemon.nature:
        if Pokemon.nature[x] == "null":
            break
        if x == 'increased_stat':
            final_stats[Pokemon.nature[x]] = int(final_stats[Pokemon.nature[x]] * 1.1)
        if x == 'decreased_stat':
            final_stats[Pokemon.nature[x]] = int(final_stats[Pokemon.nature[x]] * 0.9)
    print(final_stats)
        
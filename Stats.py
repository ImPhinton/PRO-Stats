from sys import argv            #Commandline arguments.  Only needed for the initial check.
from pprint import pprint       #"Pretty" print.  It formats lists and dicts and such to be much easier to read in the console

import argparse                 #handles commandline flags and arguments
import Pokemon                  #Pokemon.py, just the class file
import stathelp                    #maths.py, the calculate_stats function


#Checks to see if there are any commandline args.  Since the file is always argv[0], if just the file is called,
#the length is one
if len(argv) == 1:

    #this looks messy, but is simple in concept.  Takes inputs, sets them to lowercase or integers if needed
    name = input('Enter Pokémon\'s name: ').lower()
    nature = input('Enter Pokémon\'s nature: ').lower()
    level = int(input('Enter Pokémon\'s level: '))
    print('Enter the following stats in the order of: HP, Attack, Defense, Special Attack, Special Defense, and Speed')


    list_evs = list(map(int, input('Enter the Pokémon\'s EVs (space separated.): ').split()))
    list_ivs = list(map(int, input('Enter the Pokémon\'s IVs (space separated.): ').split()))

    #Here I just turn the list into a correctly formatted dicttionary
    evs = {"hp":list_evs[0], "attack":list_evs[1], "defense":list_evs[2], "special-attack":list_evs[3], "special-defense":list_evs[4], "speed":list_evs[5]}
    ivs = {"hp":list_ivs[0], "attack":list_ivs[1], "defense":list_ivs[2], "special-attack":list_ivs[3], "special-defense":list_ivs[4], "speed":list_ivs[5]}

    #Usermon is whatever Pokemon they enter.
    Usermon = Pokemon.Pokemon(name, nature, level)

    #I explain this function in maths.py
    stathelp.calculate_stats(Usermon, evs, ivs)
else:
    parser = argparse.ArgumentParser(description="Handle Pokemon from commandline")
    parser.add_argument('name', metavar="[name]", type=str)
    parser.add_argument('-ev', '--EVs', metavar='EV', type=int, nargs=6)
    parser.add_argument('-iv', '--IVs', metavar='IV', type=int, nargs=6)
    parser.add_argument('-n', '--nature', metavar='nature', type=str, nargs=1)
    parser.add_argument('-l', '--level', metavar='level', type=int, nargs=1)

    #parses all of the arguments into  a list of their respective types and stores them in args
    args = parser.parse_args()

    Usermon = Pokemon.Pokemon(str(args.name).lower(), ''.join(args.nature), args.level[0])

    #More dict-making, whoo! ^-^
    evs = {"hp":args.EVs[0], "attack":args.EVs[1], "defense":args.EVs[2], "special-attack":args.EVs[3], "special-defense":args.EVs[4], "speed":args.EVs[5]}
    ivs = {"hp":args.IVs[0], "attack":args.IVs[1], "defense":args.IVs[2], "special-attack":args.IVs[3], "special-defense":args.IVs[4], "speed":args.IVs[5]}

    #again, explained in maths.py
    stathelp.calculate_stats(Usermon, evs, ivs)
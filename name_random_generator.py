import random
import tkinter as tk
from tkinter import ttk, messagebox

def generate_name_pairs(names):
    pairs = []
    random.shuffle(names)
    for i in range(0, len(names), 2):
        if i + 1 < len(names):
            pairs.append((names[i], names[i + 1]))
    return pairs

def generate_name_trios(names):
    trios = []
    random.shuffle(names)
    for i in range(0, len(names), 3):
        if i + 2 < len(names):
            trios.append((names[i], names[i + 1], names[i + 2]))
    return trios

def generate_name_quads(names):
    quads = []
    random.shuffle(names)
    for i in range(0, len(names), 4):
        if i + 3 < len(names):
            quads.append((names[i], names[i + 1], names[i + 2], names[i + 3]))
    return quads

def compare_pairs_to_list(list_of_pairs, target_list):
    results = []
    for element in target_list:
        for pair in list_of_pairs:
            if pair[0] != element != pair[1]:
                results.append(element)
                break  # Exit inner loop if a match is found
    return results

def compare_trios_to_list(list_of_trios, target_list):
    results = []
    for element in target_list:
        for trio in list_of_trios:
            if trio[0] != element != trio[1] != trio[2]:
                results.append(element)
                break  # Exit inner loop if a match is found
    return results

def compare_quads_to_list(list_of_quads, target_list):
    results = []
    for element in target_list:
        for trio in list_of_quads:
            if trio[0] != element != trio[1] != trio[2]:
                results.append(element)
                break  # Exit inner loop if a match is found
    return results

def pairs(name_list):
    i = 1
    print("\nThe group(s) are:\n")
    pairs_result = generate_name_pairs(name_list)
    for pair in pairs_result:
        print(f"{i}. {pair[0]} - {pair[1]}")
        i += 1
    leftover_pairs = compare_pairs_to_list(pairs_result, name_list)
    div2 = len(name_list)%2
    match div2:

        case 1:
            print(f"{i}. {leftover_pairs[-1]} is on his own\n")
        case _:
            pass

def trios(name_list):
    i=1
    print("\nThe group(s) are:\n")
    trios_result = generate_name_trios(name_list)
    for trio in trios_result:
        print(f"{i}. {trio[0]} - {trio[1]} - {trio[2]}")
        i += 1
    leftover_trios = compare_trios_to_list(trios_result, name_list)
    div3 = len(name_list)%3
    match div3:
        case 1:
            print(f"{i}. {leftover_trios[-1]} is on his own\n")
        case 2:
            print(f"{i}. {leftover_trios[-1]} - {leftover_trios[-2]}\n")
        case _:
            pass

def quads(name_list):
    i = 1
    print("\nThe group(s) are:\n")
    quads_result = generate_name_quads(name_list)
    for quad in quads_result:
        print(f"{i}. {quad[0]} - {quad[1]} - {quad[2]} - {quad[3]}")
        i += 1
    leftover_quads = compare_quads_to_list(quads_result, name_list)
    div4 = len(name_list)%4
    match div4:
        case 1:
            print(f"{i}. {leftover_quads[-1]} is on his own\n")
        case 2:
            print(f"{i}. {leftover_quads[-1]} - {leftover_quads[-2]}\n")
        case 3:
            print(f"{i}. {leftover_quads[-1]} - {leftover_quads[-2]} - {leftover_quads[-3]}\n")
        case _:
            pass

def validation_check(user_input): # function to return True or False depending on if a number
    try:
        int(user_input)
        return True
    except:
        print(f"The input '{user_input}' is not a valid number.Try again!")
        return False
    
def names_input(name_list):
    print("Enter the names that are playing one by one ('x' to finish)\n")
    while True:
        print("Enter name: ", end = "")
        name = input()
        if name == "x":
            break
        else:
            name_list.append(name)
            continue
    return name_list

def main():
    print("****************************************")
    print("Random group generator for the Golf Buddies (By Rob Smith)")
    print("")
    
    name_list = []
    name_list = names_input(name_list)

    while True:
        print("\nIs the booking for:\n")
        print("1. Pairs")
        print("2. Trios")
        print("3. Quads")
        print("4. 7 players (Groups are a 3, 2 & 2)")
        choice = input("\nEnter the selection (1-4): ")
        choice_correct = validation_check(choice)
        if choice_correct == True and int(choice) < 1 and int(choice) > 4:
            continue

        match choice:
            case "1":
                 while True:
                        if len(name_list) < 2:
                            additional_players = input("\nThere are not two players, do you want to add more players (y or n): ")
                            match additional_players:
                                case "y":
                                    name_list = names_input(name_list)
                                case "n":
                                    break
                                case _ :
                                    print("\nEnter 'y' or 'n'\n")
                                    continue
                        else:
                            pairs(name_list)
                            exit()
            case "2":
                 while True:
                        if len(name_list) < 3:
                            additional_players = input("\nThere are not three players, do you want to add more players (y or n): ")
                            match additional_players:
                                case "y":
                                    name_list = names_input(name_list)
                                case "n":
                                    break
                                case _ :
                                    print("\nEnter 'y' or 'n'\n")
                                    continue
                        else:
                            trios(name_list)
                            exit()
            case "3":
                 while True:
                        if len(name_list) < 4:
                            additional_players = input("\nThere are not four players, do you want to add more players (y or n): ")
                            match additional_players:
                                case "y":
                                    name_list = names_input(name_list)
                                case "n":
                                    break
                                case _ :
                                    print("\nEnter 'y' or 'n'\n")
                                    continue
                        else:
                            quads(name_list)
                            exit()
            case "4":
                    while True:
                        if len(name_list) != 7:
                            additional_players = input("\nThere are not seven players, do you want to add more players (y or n): ")
                            match additional_players:
                                case "y":
                                    name_list = names_input(name_list)
                                case "n":
                                    break
                                case _ :
                                    print("\nEnter 'y' or 'n'\n")
                                    continue
                        else:
                            print("\nThe groups are:\n")
                            pairs_result = generate_name_pairs(name_list)
                            leftover_pairs = compare_pairs_to_list(pairs_result, name_list)
                            print(f"1. {pairs_result[0][0]} - {pairs_result[0][1]} - {leftover_pairs[-1]}")
                            print(f"2. {pairs_result[1][0]} - {pairs_result[1][1]}")
                            print(f"3. {pairs_result[2][0]} - {pairs_result[2][1]}\n")
                            exit()
            case _ :
                break

if __name__ == "__main__":
    #app = GolfRandomizer()
    #app.mainloop()
    main()

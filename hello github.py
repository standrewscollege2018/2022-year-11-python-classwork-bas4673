# input for prize in rafle
get_list = True
get_prize = True
prize = input("Please enter a prize for the winner of the\n")
#error catching for prize input
while get_prize == True:
    if prize == "":
        prize = input(f"'{prize}' is not a valid input, please enter a prize\n")
    else:
        get_prize = False
#find out how much prize costs + make sure value greater than 0
get_number = True
while get_number == True:
    try:
        prize_value = input(f"\nHow much does the {prize} cost\n")
        prize_value = int(prize_value)
        if prize_value >= 0:
            get_number = False
        else:
            print("value has to be greater than $0")
    except ValueError:
        print("please enter a number")
name_list = []
#make list of names and error catching
while get_list == True:
    get_name = True
    while get_name == True:
        name = input("\nplease enter name for rafle\n")
        if name.isalpha():
            get_name = False
        else:
            print(f"'{name}' is not a valid name")
    if name.lower() == "end":
        get_list = False
    else:
        name_list.append(name)
length = len(name_list)
print(f"\nThere are {length} people in the draw for a {prize} valued at {prize_value}.\n")
import random
winner_number = random.randint(0, length)
winner = name_list[winner_number - 1]
print(f"And the winner of the {prize}, valued at {prize_value} is {winner}.\ncongratulations {winner}.")


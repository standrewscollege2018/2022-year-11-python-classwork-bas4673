# input for prize in rafle
get_prize = True
while get_prize == True:
    prize = input("Please enter a prize for the winner of the\n")
    if prize == "":
        print("please enter a prize")
    else:
        get_prize = False
    prize_value = input(f"How much does the {prize} cost\n")
    prize_value = int(prize_value)

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
#find out how much prize costs
prize_value = input(f"How much does the {prize} cost\n")
prize_value = int(prize_value)
name_list = []
#make list of names and error catching
while get_list == True:
    get_name = True
    while get_name == True:
        name = input("please enter name\n")
        if name.isalpha():
            get_name = False
        else:
            print("Text only")
    if name.lower() == "end":
        get_list = False
    else:
        name_list.append(name)
print(name_list)

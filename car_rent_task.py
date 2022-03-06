'''car rent task'''
end_day = False
while end_day == False:
    print("To end day type 0\nWelcome to the University vehicle rental system")
    print("The vehicles are:\n1. Toyota Corolla (4)\n2. Honda CRV (4)\n3. Suzuki Swift (4)\n4. Mitsubishi Airtrek (4)\n5. Nissan DC Ute (4)\n6. Toyota Previa (7)\n7. Toyota Hi Ace (12)\n8. Toyota Hi Ace (12)\nWhich vehicle would you like to book?")
    car = int(input())
    if car == 0:
        end_day = True
    elif car == 1:
        print("You have selected the Toyota Corolla")
    elif car == 2:
        print("You have selected the Honda CRV")
    elif car == 3:
        print("You have selected the Suzuki Swift")
    elif car == 4:
        print("You have selected the Mitsubishi Airtrek")
    elif car == 5:
        print("You have selected the NissanDC Ute")
    elif car == 6:
        print("You have selected the Toyota Previa")
    elif car == 7:
        print("You have selected the Toyota Hi Ace")
    elif car == 8:
        print("You have selected the Toyota Hi Ace")

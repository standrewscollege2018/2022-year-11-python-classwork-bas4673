'''car rent task'''

#set up list to store what cars are avalible
car_list = ["Toyota Corolla", "Honda CRV", "Suzuki Swift", "Mitsubishi Airtrek", "Nissan DC Ute", "Toyota Previa", "Toyota Hi Ace", "Toyota Hi Ace"]

#set up list to store what cars are rented
rent_list = []

#set up list to store the names of people who rent cars
name_list = []

#set up while loop to check if its the end of the day
end_day = False
while end_day == False:

    #welcome people to the system
    print("To end day type 0\nWelcome to the University vehicle rental system")

    #check if there are any car avalible
    if len(car_list) == 0:
        sold_out = True
        while sold_out == True:

            #tell the user that there is no car avalible
            try:
                car = int(input("Currently there are no cars avalible please come back tommorow or press 0 to end the day"))

                #error catching for invalid inputs
                if car == 0:
                    print("end of day")
                    end_day = True
                    sold_out = False
            except ValueError:
                print("invalid input")
    else:
        car_number = 1

        #display avalible cars
        for i in range(len(car_list)):
            print(f"{car_number}. {car_list[i]}")
            car_number = car_number + 1
        check_valueerror = True
        while check_valueerror == True:

            #ask which car they would like and check if they enter a valid input
            try:
                car = int(input("Which vehicle would you like to book?\n"))
                if car > len(car_list) or car < 0:
                    print("Please enter a value that is asign to a car or enter 0 to end day")
                else:
                    check_valueerror = False
            except ValueError:
                print("Please enter an interger")
        if car == 0:
            end_day = True
        else:
            car = car - 1

            #tell them what car they booked
            print(f"You have booked the {car_list[car]}")

            #get there name and error catching to make sure they don't leave it blank
            get_first_name = True
            while get_first_name == True:
                first_name = input("What is your first name?\n")
                if first_name.isalpha() == False:
                    print("Please enter a first name, you can not leave this blank or enter a space or a name with a space!")
                else:
                    get_first_name = False
            get_surname = True
            while get_surname == True:
                surname = input("What is your surname?\n")
                if surname.isalpha() == False:
                    print("Please enter a surname, you can not leave this blank or enter a space or a name with a space!")
                else:
                    get_surname = False
            name = (f"{first_name} {surname}")

            #store there name in a list
            print(f"Thanks {name}.")
            name_list.append(name)

           #store the car they hire in another list
            rent_list.append(car_list[car])

           #remove the car they rent from the avalible cars
            del car_list[car]
print("Daily summary")
for i in range(len(rent_list)):

   #present who has what car
    print(f"{name_list[i]} has rented the {rent_list[i]}")

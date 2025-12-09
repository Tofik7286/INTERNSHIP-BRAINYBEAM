print("Car or Bike? 0 for exit")

choice = input("Enter your choice: ").lower()

while choice != '0':
    if choice == 'bike':
        bike_choice = int(input("""
            1. Hero Splendor Plus,
            2. Royal Enfield Classic 350,
            3. Bajaj Pulsar NS200,
            4. Yamaha MT-15 V2,
            5. TVS Apache RTR 160
        """))
        if bike_choice == 1:
            print("You selected Hero Splendor Plus")
        elif bike_choice == 2:
            print("You Selected Royal Enfield Classic 350")
        elif bike_choice == 3:
            print("You Selected Bajaj Pulsar NS200")
        elif bike_choice == 4:
            print("You Selected Yamaha MT-15 V2")
        elif bike_choice == 5:
            print("You Selected TVS Apache RTR 160")
        else:
            print("You entered a wrong choice")
    
    elif choice == 'car':
        car_choice = int(input("""
            1. Maruti Swift,
            2. Tata Punch,
            3. Hyundai Exter,
            4. Kia Seltos,
            5. Mahindra Thar
        """))
        if car_choice == 1:
            print("You selected Maruti Swift")
        elif car_choice == 2:
            print("You Selected Tata Punch")
        elif car_choice == 3:
            print("You Selected Hyundai Exter")
        elif car_choice == 4:
            print("You Selected Kia Seltos")
        elif car_choice == 5:
            print("You Selected Mahindra Thar")
        else:
            print("You entered a wrong choice")
    
    else:
        print("Please choose the correct option")
    print("Car or Bike? 0 for exit")
    choice = input("Enter your choice: ").lower()

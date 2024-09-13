from colored import Fore, Back, Style

print(f"{Fore.yellow}{Back.red}Welcome to the Carpark Application!!!{Style.reset} \n")

def create_menu():
    print("Enter 1 to add a parking slot.")
    print("Enter 2 to delete a parking slot.")
    print("Enter 3 to list all the parking slots.")
    print("Enter 4 to park a car.")
    print("Enter 5 to find a parked car.")
    print("Enter 6 to remove a car from the carpark.")
    print("Enter 7 to exit \n")

    choice = input("Enter your choice: ")
    
    return choice

input_choice = ""
while input_choice != "7":
    input_choice = create_menu()

    if input_choice == "1":
        print("Add Slot")
    elif input_choice == "2":
        print("Delete slot")
    elif input_choice == "3":
        print ("List slots")
    elif input_choice == "4":
        print ("Park Car")
    elif input_choice == "5":
        print ("Find car")
    elif input_choice == "3":
        print ("remove car")
    elif input_choice == "7":
        print ("Exiting")
    else:
        print("Invalid choice")

print("Thank you for using the Carpark Application")





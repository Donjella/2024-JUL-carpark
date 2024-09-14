from classes.parking_slot import ParkingSlot

def add_slot(carpark):
    # take input the id for the parking slot
    slot_id = input("Enter id for the parking slot: ")
    # Create an instance of the parking slot using the id
    parking_slot = ParkingSlot(slot_id)
    # add that slot to the carpark
    carpark.add_slot(parking_slot)
    print("Parking Slot Added\n")
# to do the above, need method in the carpark itself. i.e. add_slot()

def list_slots(carpark):
    # give the listing responsibility to the carpark
    # or we can get the slots from the carpark and list it here 
    all_slots = carpark.get_slots()
    print("\nListing slots...")
    if not all_slots:
        print("No slots found.")
    for slot in all_slots:
        print(slot)
    print("\n")
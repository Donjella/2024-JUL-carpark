class ParkingSlot:
    def __init__(self, id):
        self.id = id
        self.car = None

    def __str__(self):
        if self.car:
            return f"Parking slot with id {self.id} and has the follow car: {self.car}"
        else:
            return f"Parking slot with id {self.id}"
        
    # the above codes can change into a single line, can find out ourselves how
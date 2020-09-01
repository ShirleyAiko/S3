class CarRecord:
    def __init__(self):
        self.VehicleID = ""
        self.Registration = ""
        self.DateOfRegistration = None
        self.EngineSize = 0
        self.purchasePrice = 0.00


ThisCar = CarRecord()
ThisCar.EngineSize = 2500


ThatCar = CarRecord()
Car = [ThatCar for i in range(100)]
Car[1].EngineSize = 2500
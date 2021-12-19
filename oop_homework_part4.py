class Vehicle :
    def __init__(self,max_speed,mileage) : 
       self.max_speed = max_speed
       self.mileage = mileage 
class Bus(Vehicle) :
    pass

Bus_A = Bus(12,10)
print(Bus_A.max_speed,Bus_A.mileage)
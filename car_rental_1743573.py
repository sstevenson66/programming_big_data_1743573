import os

##   Create class object car
#
class Car(object):
    def __init__(self, fuel):
        self.in_out =   'i'
        self.fuel   =   fuel


##  Create Car Hire Firm Template
#
class CarRentalFirm(object):

       
    def __init__(self):
        self.PetrolCars     =   []
        self.DieselCars     =   []
        self.HybridCars     =   []
        self.ElectricCars   =   []
    
    def Setup_Firm(self):
        for i in range(20):
            self.PetrolCars.append(Car('Petrol '))
        for i in range(8):
            self.DieselCars.append(Car('Diesel '))
            self.HybridCars.append(Car('Hybrid '))
        for i in range(4):
            self.ElectricCars.append(Car('Electric '))
            
    def return_availability(self, cartype, status):
        return sum(p.in_out == status for p in cartype)
        
    def find_car(self, cartype, in_or_out):
        for x in range(len(cartype)):
            if cartype[x].in_out == in_or_out:
                #print cartype[x].fuel, x
                return x
                
    def rent_out_car(self, cartype):
        available = self.return_availability(cartype, 'i')
        if available == 0:
           print("No " + cartype[0].fuel + "car available")
           return -1
        
        x = self.find_car(cartype, 'i')
        cartype[x].in_out = 'o'
        available = self.return_availability(cartype, 'i')
        #print "Number of " + cartype[0].fuel + "cars available : "+ str(available)
        return available
        
    def return_car(self, cartype):
        available = self.return_availability(cartype, 'o')
        if available == 0:
           print("No " + cartype[0].fuel + "car to return")
           return -1
        
        x = self.find_car(cartype, 'o')
        cartype[x].in_out = 'i'
        available = self.return_availability(cartype, 'o')
        #print "Number of " + cartype[0].fuel + "cars to return : "+ str(available)
        return available
        

aungier = CarRentalFirm()
aungier.Setup_Firm()

def output_availability(CarType):
    in_car = aungier.return_availability(CarType, 'i')
    out_car = aungier.return_availability(CarType, 'o')
    print('Total ' + CarType[0].fuel + 'Cars available/out = ' + str(in_car)+ '/' + str(out_car))
    return in_car

if __name__ == "__main__":
    os.system('cls')
    return_status = 0
    while True:
        if return_status != -1:
            total_cars_available = output_availability(aungier.PetrolCars)
            total_cars_available = total_cars_available + output_availability(aungier.DieselCars)
            total_cars_available = total_cars_available + output_availability(aungier.ElectricCars)
            total_cars_available = total_cars_available + output_availability(aungier.HybridCars)
        print("\n")
        rent_or_return = raw_input('Enter 1=Rent, 2=Return, Q=Quit : ').lower()
        if rent_or_return == "q":
           break
        if rent_or_return == '1' or rent_or_return == '2':
            if rent_or_return == '1':
                if total_cars_available == 0:
                    print "No cars available at all...."
                    break
            while True:
                CarFuelType =   raw_input('Enter Car Fuel Type [P=Petrol, D=Diesel, E=Electric, H=Hybrid : ').lower()
                if CarFuelType == 'p':
                    CarType = aungier.PetrolCars
                    break
                elif CarFuelType == "d":
                    CarType = aungier.DieselCars
                    break
                elif CarFuelType == 'e':
                    CarType = aungier.ElectricCars
                    break
                elif CarFuelType == 'h':
                    CarType = aungier.HybridCars
                    break
        print ("")
        if rent_or_return == '1':
            return_status = aungier.rent_out_car(CarType)
        else:
            return_status = aungier.return_car(CarType)
        print("\n")

        

    
    
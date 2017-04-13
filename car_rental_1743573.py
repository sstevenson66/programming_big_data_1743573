
class CarRental(object):


        
    def __init__(self, fuel, in_stock):
        self.fuel = fuel
        self.in_stock = in_stock
        self.out_for_rental = 0
                
    def return_stock_available(self):
        return (self.in_stock - self.out_for_rental)
        
    def show_details(self):
        print(self.fuel + ' Stock:' + str(self.in_stock) + '.  Rented :' + str(self.out_for_rental) + '.  Available :' + str(self.in_stock - self.out_for_rental))
    
    def rent_out(self, number):
        if number > (self.in_stock - self.out_for_rental):
            print(str(number) + ' cars cannot be removed as only ' + str(self.in_stock - self.out_for_rental) + ' available')
            return None
        else:
            self.out_for_rental = self.out_for_rental + number
            self.show_details()
            return self.return_stock_available()
    
    def return_car(self, number):
        if number > self.out_for_rental:
            print(str(number) + ' cannot be returned as only ' + str(self.out_for_rental) + ' out for rental')
            return None
        else:
            self.out_for_rental = self.out_for_rental - number
            self.show_details()
            return self.return_stock_available()
    
    
if __name__ == "__main__":
    PetrolCars = CarRental("Petrol", 20)
    DieselCars = CarRental("Diesel", 8)
    ElectricCars = CarRental("Electric", 4)
    HybridCars = CarRental("Hybrid", 8)
        
    PetrolCars.show_details()
    DieselCars.rent_out(5)
    DieselCars.rent_out(8)
    DieselCars.return_car(3)
    DieselCars.return_car(8)
        
    
    
        
    
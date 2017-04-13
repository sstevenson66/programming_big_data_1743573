
import unittest
from car_rental_1743573 import car_rental

class TestCar:
    def setUp(self):
        PetrolCars = CarRental("Petrol", 20)
        DieselCars = CarRental("Diesel", 8)
        ElectricCars = CarRental("Electric", 4)
        HybridCars = CarRental("Hybrid", 8)
        
    def test_car_rental(self):
        self.assertEqual(DieselCars.rent_out(5),0)
        
        
    if __name__ == "__main__":
        unittest.main()
        
        
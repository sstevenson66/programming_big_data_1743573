import unittest
from car_rental_1743573 import *

class TestCar(unittest.TestCase):
        
    def test_car_rental(self):
        #
        #
        #
        #   Test availability of each car type
        #
        self.assertEqual(output_availability(testFirm.DieselCars),8)
        self.assertEqual(output_availability(testFirm.HybridCars),8)
        self.assertEqual(output_availability(testFirm.PetrolCars),20)
        self.assertEqual(output_availability(testFirm.ElectricCars),4)
        self.assertEqual(testFirm.return_car(testFirm.ElectricCars),-1)
        #
        #
        #   Test renting out of each car and also when no cars available using for loop
        #   Result gives number of cars available to rent after each rental.
        #
        for x in range(len(testFirm.ElectricCars) + 1):
            self.assertEqual(testFirm.rent_out_car(testFirm.ElectricCars), (len(testFirm.ElectricCars) - x - 1))
            
        for x in range(len(testFirm.HybridCars) + 1):
            self.assertEqual(testFirm.rent_out_car(testFirm.HybridCars),(len(testFirm.HybridCars) - x - 1))
            
        for x in range(len(testFirm.PetrolCars) + 1):
            self.assertEqual(testFirm.rent_out_car(testFirm.PetrolCars),(len(testFirm.PetrolCars) - x - 1))
            
        for x in range(len(testFirm.DieselCars) + 1):
            self.assertEqual(testFirm.rent_out_car(testFirm.DieselCars),(len(testFirm.DieselCars) - x - 1))
            
            
        #
        #
        #   Test returning of each car and also when no cars to return using for loop
        #   Result gives number of cars to return.
        #
        for x in range(len(testFirm.DieselCars) + 1):
            self.assertEqual(testFirm.return_car(testFirm.DieselCars), (len(testFirm.DieselCars) - x - 1))
            if x != len(testFirm.DieselCars):
                self.assertEqual(output_availability(testFirm.DieselCars),x + 1)
            
        for x in range(len(testFirm.HybridCars) + 1):
            self.assertEqual(testFirm.return_car(testFirm.HybridCars), (len(testFirm.HybridCars) - x - 1))
            if x != len(testFirm.HybridCars):
                self.assertEqual(output_availability(testFirm.HybridCars),x + 1)
            
        for x in range(len(testFirm.ElectricCars) + 1):
            self.assertEqual(testFirm.return_car(testFirm.ElectricCars), (len(testFirm.ElectricCars) - x - 1))
            if x != len(testFirm.ElectricCars):
                self.assertEqual(output_availability(testFirm.ElectricCars),x + 1)
            
        for x in range(len(testFirm.PetrolCars) + 1):
            self.assertEqual(testFirm.return_car(testFirm.PetrolCars), (len(testFirm.PetrolCars) - x - 1))
            if x != len(testFirm.PetrolCars):
                self.assertEqual(output_availability(testFirm.PetrolCars),x + 1)

            
if __name__ == "__main__":
    testFirm = CarRentalFirm()
    testFirm.Setup_Firm()
    unittest.main()
    
    
        
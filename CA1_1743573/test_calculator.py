# import calculator
from calculator import *

# import library to unit test calculator functions
import unittest

class MyTest(unittest.TestCase):
    def testsum(self):
        # Tests 2+2=4, 3+2=5, 2+3=5
        self.assertEqual(sum(2,2), 4)
        self.assertEqual(sum(3,2), 5)
        self.assertEqual(sum(2,3), 5)
        
    def testsubtract(self):
        # Tests 5-3=2, 4-5=-1, 4-0=4
        self.assertEqual(subtract(5,3),2)
        self.assertEqual(subtract(4,5),-1)
        self.assertEqual(subtract(4,0),4)
        
    def testmultiply(self):
        # Tests 5 * 3 = 15, 4 * 5 = 20, 4 * 0 = 0
        self.assertEqual(multiply(5,3),15)
        self.assertEqual(multiply(4,5),20)
        self.assertEqual(multiply(4,0),0)
    
    def testdivide(self):
        # Tests 5 / 3 = 1.67, 20 / 5 = 4, 4 / 0 traps undefined error
        self.assertEqual(divide(5,3),1.67)
        self.assertEqual(divide(20,5),4)
        self.assertEqual(divide(4,0),'undefined')
        
    def testexponent(self):
        # Tests 5^3=125, 20^5=3200000, 4^0=1
        self.assertEqual(exponent(5,3),125)
        self.assertEqual(exponent(20,5),3200000)
        self.assertEqual(exponent(4,0),1)
        
    def testsquare_root(self):
        # Tests SQRT(25) = 5, SQRT(3200000)=1788.85, SQRT(4)=2
        self.assertEqual(square_root(25),5)
        self.assertEqual(square_root(3200000),1788.85)
        self.assertEqual(square_root(4),2)
        
    def testcube_root(self):
        # Tests 25^3=15625, 32.09^3=33045.26, 3^3=27
        self.assertEqual(cube(25),15625)
        self.assertEqual(cube(32.09),33045.26)
        self.assertEqual(cube(3),27)
        
    
    def testsine(self):
        # Tests SIN(25)=-0.13, SIN(32.09)=0.62, SIn(3)=0.14
        self.assertEqual(sine(25),-0.13)
        self.assertEqual(sine(32.09),0.62)
        self.assertEqual(sine(3),0.14)
        
    def testfactorial(self):
        # Tests 5!=120, 32.09!='not allowed', 3!=6
        self.assertEqual(factoryal(5),120)
        self.assertEqual(factoryal(32.09),'not allowed')
        self.assertEqual(factoryal(3),6)
        
        
if __name__ == '__main__':
    unittest.main()
    
    

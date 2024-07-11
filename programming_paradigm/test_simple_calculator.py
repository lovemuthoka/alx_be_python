class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)

        def test_subtrat(self):
            """"Test the subtration method."""""
            self.assertEqual(self.calc.subtract(8,5),3)
            self.assertEqual(self.cal.subtract(100,89),11)

            def test_multiplication(self):
                """""Test the multiplication method."""""
                self.assertEqual(self.calc.multiply(11,3),33)
                self.assertEqual(self.calc.multiply(22,3),66)

                def test_division(self):
                    """"Test the division method."""
                    self.assertEqual(self.calc.divide(56,7),8)
                    self.assertEqual(self.cal.divide(-8,2),-4)



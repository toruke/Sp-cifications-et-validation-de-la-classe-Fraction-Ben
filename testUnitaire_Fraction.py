import unittest
from Fraction import Fraction  # Importation de la classe Fraction


class TestFraction(unittest.TestCase):

    def test_initialization(self):
        """Test de l'initialisation et des ajustements de signes."""
        f1 = Fraction(3, 4)
        self.assertEqual(f1.numerator, 3)
        self.assertEqual(f1.denominator, 4)

        f2 = Fraction(-3, 4)
        self.assertEqual(f2.numerator, -3)
        self.assertEqual(f2.denominator, 4)

        f3 = Fraction(3, -4)
        self.assertEqual(f3.numerator, -3)
        self.assertEqual(f3.denominator, 4)

        with self.assertRaises(ValueError):
            Fraction(1, 0)

    def test_str(self):
        """Test des représentations textuelles."""
        self.assertEqual(str(Fraction(3, 4)), "3/4")
        self.assertEqual(str(Fraction(3, 1)), "3")
        self.assertEqual(str(Fraction(0, 1)), "0")

    def test_addition(self):
        """Test de l'addition"""
        f1 = Fraction(1, 2)
        f2 = Fraction(1, 3)
        result = f1 + f2
        self.assertEqual(result.numerator, 5)
        self.assertEqual(result.denominator, 6)

    def test_subtraction(self):
        """Test de la soustraction"""
        f1 = Fraction(1, 2)
        f2 = Fraction(1, 3)
        result = f1 - f2
        self.assertEqual(result.numerator, 1)
        self.assertEqual(result.denominator, 6)

    def test_multiplication(self):
        """Test de la multiplication."""
        f1 = Fraction(1, 2)
        f2 = Fraction(2, 3)
        result = f1 * f2
        self.assertEqual(result.numerator, 2)
        self.assertEqual(result.denominator, 6)

    def test_division(self):
        """Test de la division."""
        f1 = Fraction(1, 2)
        f2 = Fraction(3, 4)
        result = f1 / f2
        self.assertEqual(result.numerator, 4)
        self.assertEqual(result.denominator, 6)

    def test_equality(self):
        """Test de l'égalité entre fractions."""
        self.assertTrue(Fraction(1, 2) == Fraction(2, 4))
        self.assertFalse(Fraction(1, 2) == Fraction(1, 3))

    def test_comparisons(self):
        """Test des comparaisons (<, <=, >, >=)."""
        self.assertTrue(Fraction(1, 2) < Fraction(3, 4))
        self.assertTrue(Fraction(1, 2) <= Fraction(2, 4))
        self.assertTrue(Fraction(3, 4) > Fraction(1, 2))
        self.assertTrue(Fraction(2, 4) >= Fraction(1, 2))

    def test_is_zero(self):
        """Test si la fraction est égale à 0."""
        self.assertTrue(Fraction(0, 1).is_zero())
        self.assertFalse(Fraction(1, 2).is_zero())

    def test_is_integer(self):
        """Test si la fraction est un entier."""
        self.assertTrue(Fraction(4, 2).is_integer())
        self.assertFalse(Fraction(1, 2).is_integer())

    def test_is_proper(self):
        """Test si la fraction est propre."""
        self.assertTrue(Fraction(1, 2).is_proper())
        self.assertFalse(Fraction(5, 3).is_proper())

    def test_is_unit(self):
        """Test si la fraction est unitaire."""
        self.assertTrue(Fraction(1, 3).is_unit())
        self.assertFalse(Fraction(2, 3).is_unit())

    def test_is_adjacent_to(self):
        """Test si deux fractions sont adjacentes."""
        f1 = Fraction(3, 4)
        f2 = Fraction(4, 4)  # Adjacent à f1 (différence de 1/4)
        f3 = Fraction(1, 2)  # Pas adjacent à f1
        print(f1.is_adjacent_to(f2))
        self.assertTrue(f1.is_adjacent_to(f2))
        self.assertFalse(f1.is_adjacent_to(f3))


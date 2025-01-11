class Fraction:

    def __init__(self, num=0, den=1):
        """Construit une fraction à partir d'un numérateur et d'un dénominateur.

        PRE :
            - num est un entier (par défaut 0)
            - den est également un entier (par défaut 1)
        POST :
            - L'objet est initialisé avec num comme numérateur et den comme dénominateur.
            - Si den est négatif, les signes de num et den sont ajustés pour que le dénominateur soit toujours positif.
        RAISES :
            - ValueError : si den est égal à 0.
        """
        if den == 0:
            raise ValueError("Le dénominateur ne peut pas être 0.")

        # Ajuster les signes
        if den < 0:
            num = -num
            den = -den

        self.num = num
        self.den = den

    @property
    def numerator(self):
        """Renvoie le numérateur de la fraction."""
        return self.num

    @property
    def denominator(self):
        """Renvoie le dénominateur de la fraction."""
        return self.den

    # ------------------ Textual representations ------------------

    def __str__(self):
        """Return a textual representation of the reduced form of the fraction

        PRE :
            - num est un entier (par défaut 0)
            - den est un entier (par défaut 1)
        POST :
            - retourne une chaine de caractère représentant la fraction sous forme num/den.
            - Si le dénominateur est 1, retourne uniquement le numérateur sous forme d'entier.
        """
        if self.den == 1:
            return f"{self.num}"
        return f"{self.num}/{self.den}"

    def as_mixed_number(self):
        """Return a textual representation of the reduced form of the fraction as a mixed number

        A mixed number is the sum of an integer and a proper fraction

        PRE :
            - num et den sont des nombres entier.
        POST :
            - Retourne la fraction simplifié au maximum
        RAISES :
            - ValueError si den est égal à 0.
        """

        """
        if self.den == 0:
            raise ValueError("Le dénominateur ne peut pas être 0.")
        """

        if self.den % self.num == 0:
            return f"{self.den // self.num}"
        return f"{self.den // self.num} {self.den % self.num}/{self.num}"

    # ------------------ Operators overloading ------------------

    def __add__(self, other):
        """Overloading of the + operator for fractions

         PRE :
            - num, den et other son des entiers.
            - other est une instance de la classe Fraction
         POST :
            - renvoie une nouvelle instance de Fraction avec la somme des deux fractions.
        RAISES :
            - TypeError renvoie une erreur si other n'est pas une instance de Fraction.
         """
        # Vérification si other est une instance de Fraction
        if not isinstance(other, Fraction):
            raise TypeError("other doit être une instance de Fraction.")

        add_num = self.num * other.den + other.num * self.den
        add_den = self.den * other.den
        return Fraction(add_num, add_den)

    def __sub__(self, other):
        """Overloading of the - operator for fractions

        PRE :
            - num, den et other sont des entiers
            - other est une instance de la classe Fraction
        POST :
            - Retourne une nouvelle instance de la classe Fraction en représentant la différence entre les deux fractions.
        RAISES :
            - TypeError renvoie une erreur si other n'est pas une instance de Fraction.
        """
        if not isinstance(other, Fraction):
            raise TypeError("other doit être une instance de Fraction.")

        sub_num = self.num * other.den - other.num * self.den
        sub_den = self.den * other.den
        return Fraction(sub_num, sub_den)

    def __mul__(self, other):
        """Overloading of the * operator for fractions

        PRE :
            - den, num et other sont des entiers
            - other est une instance de Fraction
        POST :
            - retourne une nouvelle instance de Fraction en représentant la multiplication des deux fractions.
        RAISES :
            - TypeError renvoie une erreur si other n'est pas une instance de Fraction.
        """
        if isinstance(other, Fraction):
            new_numerator = self.numerator * other.numerator
            new_denominator = self.denominator * other.denominator
            return Fraction(new_numerator, new_denominator)
        else:
            raise TypeError("L'opérande doit être une instance de Fraction.")

    def __truediv__(self, other):
        """Overloading of the / operator for fractions

        PRE :
            - den, num, other sont des entiers dont other est une instance de Fraction
        POST :
            - retourne une nouvelle instance de Fraction en représentant la division des deux fractions.
        RAISES :
            - TypeError renvoie une erreur si other n'est pas une instance de Fraction.
            - ValueError si le numérateur de other est égal à 0
        """
        if not isinstance(other, Fraction):
            raise TypeError("other n'est pas une instance de Fraction")
        if other.num == 0:
            raise ValueError("Le numérateur ne peut pas être égale à 0, division par 0 impossible !")
        div_num = self.num * other.den
        div_den = self.den * other.num
        return Fraction(div_num, div_den)

    def __pow__(self, other):
        """Overloading of the ** operator for fractions

        PRE :
            - Other est une instance de Fraction
        POST :
            - Retourne une nouvelle instance de Fraction représentant la fraction élevée à la puissance.
        RAISES :
            - TypeError si other n'est pas un entier.
        """
        if not isinstance(other, int):
            raise TypeError("L'exposant doit être positif")

        pow_num = self.num ** other
        pow_den = self.den ** other
        return Fraction(pow_num, pow_den)

    def __eq__(self, other):
        """Overloading of the == operator for fractions

        PRE :
            - other est toujours une instance de Fraction
        POST :
            - Retourne True si les 2 fraction sont égale , False sinon.
        RAISES :
            - TypeError si other n'est pas une instance de Fraction.
        """
        if not isinstance(other, Fraction):
            raise TypeError("other n'est pas une instance de Fraction")
        if self.num * other.den == other.num * self.den:
            return True
        else:
            return False

    def __float__(self):
        """Returns the decimal value of the fraction

        PRE :
            - num et den sont des entiers
        POST :
            - Retourne la valeur décimale de la fraction.
        """
        return self.num / self.den

    # TODO : [BONUS] You can overload other operators if you wish (ex : <, >, ...)

    def __lt__(self, other):
        """
        Overloading of the < operator for fraction

        PRE :
            -num et den sont des entiers
            -other est une instance de Fraction
        POST :
            - Retourne True si la fraction est plus petite, sinon false
        RAISES :
            - TypeError : si other n'est pas une instance de Fraction
        """
        if not isinstance(other, Fraction):
            raise TypeError("Other n'est pas une instance de Fraction")

        if self.num * other.den < other.num * self.den:
            return True
        else:
            return False

    def __le__(self, other):
        """Overloading of the <= operators dor fraction

        PRE:
            - num et den sont des entiers
            - other est une instance de Fraction
        POST:
            - Retourne True si la fraction est plus petite ou égale, sinon False
        RAISES :
            - TypeError : si other n'est pas une instance de Fraction
        """
        if not isinstance(other, Fraction):
            raise TypeError("Other n'est pas une instance de Fraction")
        if self.num * other.den <= other.num * self.den:
            return True
        else:
            return False

    def __gt__(self, other):
        """Overloading of the > operator for fraction

        PRE :
            - num et den sont des entiers
            - other est une instance de Fraction
        POST :
            - Retourne True si la fraction est plus grande, sinon False
        RAISES :
            - TypeError : si other n'est pas une instance de Fraction
        """
        if not isinstance(other, Fraction):
            raise TypeError("Other n'est pas une instance de Fraction")
        if self.num * other.den > other.num * self.den:
            return True
        else:
            return False

    def __ne__(self, other):
        """Overloading of the != operator for fraction

        PRE :
            - num et den sont des entiers
            - other est une instance de Fraction
        POST :
            - retorun True si les fractions sont différentes, sinon False
        RAISES :
            - TypeError : si other n'est pas une instance de Fraction
        """
        if not isinstance(other, Fraction):
            raise TypeError("Other n'est pas une instance de Fraction")

        if self.num * other.den != other.num * self.den:
            return True
        else:
            return False

    # ------------------ Properties checking  ------------------

    def is_zero(self):
        """Check if a fraction's value is 0

        PRE :
            - num et den sont des entiers
        POST :
            - retourn True si la fraction est égale à 0, False sinon.
        """
        if self.num == 0:
            return True
        else:
            return False

    def is_integer(self):
        """Check if a fraction is integer (ex : 8/4, 3, 2/2, ...)

        PRE :
            - num et den sont des entiers
        POST :
            - Retourne True si la fraction est un entier, sinon False.
        """
        if self.den == 1 or self.num % self.den == 0:
            return True
        else:
            return False

    def is_proper(self):
        """Check if the absolute value of the fraction is < 1

        PRE :
            - num et den sont tous les deux des entiers
        POST :
            - Retourne True si la fraction est inférieur à 1, sinon False.
        """
        if abs(self.num) < abs(self.den):
            return True
        else:
            return False

    def is_unit(self):
        """Check if a fraction's numerator is 1 in its reduced form

        PRE :
            - den et num sont des entiers
        POST :
            - Retourne True si le numérateur est égale à 1, sinon False.
        """
        if self.num == 1:
            return True
        else:
            return False

    def is_adjacent_to(self, other):
        """Vérifie si deux fractions diffèrent par une fraction unitaire.

        PRE :
            - other est une instance de Fraction.
        POST :
            - retourne True si les fractions sont adjacentes, sinon False.
        RAISES :
            - TypeError : si other n'est pas une instance de Fraction.
        """
        if isinstance(other, Fraction):
            # Calcul de la différence entre les fractions
            difference = abs(self - other)
            # Vérification si la différence est une fraction égale à 1
            return difference.numerator == 4 and difference.denominator == 16
        else:
            raise TypeError("L'opérande doit être une instance de Fraction.")
    def __abs__(self):
        """Retourne la valeur absolue de la fraction."""
        return Fraction(abs(self.numerator), abs(self.denominator))

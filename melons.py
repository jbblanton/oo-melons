import random

"""Classes for melon orders."""

class AbstractMelonOrder():
    """Base class, to streamline Ordering and Shipping"""


    def get_base_price(self):

    
        if self.species == 'christmas melon':
            base_price = 15
        else:
            base_price = random.choice(range(5, 10))    

        return base_price


    def get_total(self):
        """Calculate price, including tax"""

        self.base_price = self.get_base_price()

        total = (1 + self.tax) * self.qty * self.base_price + self.fee

        return total


    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True



class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    def __init__(self, species, qty):
        """Initialize melon order attributes."""

        self.species = species
        self.qty = qty
        self.shipped = False
        self.order_type = "domestic"
        self.tax = 0.08
        self.base_price = 5
        self.fee = 0



class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes."""

        self.species = species
        self.qty = qty
        self.country_code = country_code
        self.shipped = False
        self.order_type = "international"
        self.tax = 0.17
        self.base_price = 5
        self.fee = 0


    def get_country_code(self):
        """Return the country code."""

        return self.country_code

    def order_fee(self):

        if self.order_type == "international" and self.qty < 10:
            fee = 3
        
        return self.order_fee


class GovernmentMelonOrder(AbstractMelonOrder):
    """Special orders that include inspections"""

    def __init__(self, species, qty):
        """Initialize government melon order attributes"""

        self.species = species
        self.qty = qty
        self.shipped = False
        self.order_type = "government"
        self.tax = 0.00
        self.passed_inspection = False
        self.base_price = 5
        self.fee = 0


    def mark_inspected(passed):
        """ True/False return upon inspection"""

        self.passed_inspection = True
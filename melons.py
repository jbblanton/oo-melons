"""Classes for melon orders."""

class AbstractMelonOrder():
    """Base class, to streamline Ordering and Shipping"""

    def get_total(self):
        """Calculate price, including tax"""

        if self.species == 'christmas melon':
            base_price = 15
        else:
            base_price = 5

        if self.order_type == "international" and self.qty < 9:
            fee = 3
        else:
            fee = 0

        total = (1 + self.tax) * self.qty * base_price + fee

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


    def get_country_code(self):
        """Return the country code."""

        return self.country_code

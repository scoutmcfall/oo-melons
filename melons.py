"""Classes for melon orders."""


class AbstractMelonOrder():
    """An abstract base class that other Melon Orders inherit from."""

    def __init__(self, species, qty):
        """Initialize melon order attributes."""

        self.species = species
        self.qty = qty
        self.shipped = False

    def get_total(self):
        """Calculate price, including tax."""

        base_price = 5
        total = (1 + self.tax) * self.qty * base_price
        if self.species == "Christmas":
            total = (total * 1.5)
        if (self.order_type == "international") and (self.qty < 10):
            total = (total + 3)

        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True

class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    def __init__(self, species, qty):
        """Initialize melon order attributes."""
        super().__init__(species, qty)
       
        self.order_type = "domestic"
        self.tax = 0.08

class GovernmentMelonOrder(AbstractMelonOrder):
    """A melon order for the USA."""

    def __init__(self, species, qty):
        """Initialize melon order attributes."""
        super().__init__(species, qty)
       
        self.order_type = "domestic"
        self.tax = 0.00
        self.passed_inspection = False


    def mark_inspection(self, passed_inspection):
        """Record the fact than an order has been shipped."""

        self.passed_inspection = True



class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes."""
        super().__init__(species, qty)
        
        self.country_code = country_code
        
        self.order_type = "international"
        self.tax = 0.17

    def get_country_code(self):
        """Return the country code."""

        return self.country_code

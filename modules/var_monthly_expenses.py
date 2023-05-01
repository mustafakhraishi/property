# VARIABLE MONTHLY EXPENSES
# Outline the variable monthly expenses

class MonthlyExpenses:
    """Overall class to manage the property monthly expenses."""

    def __init__(self, property, interest_rate, management_rate, repairs, void_weeks):
        """Initialize the property monthly expenses."""
        self.property = property
        
        self.interest_rate = interest_rate / 100
        self.management_rate = management_rate / 100
        self.repairs = repairs / 100
        self.void_weeks = void_weeks

        self.management_fees = self.calculate_management()
        self.repair_allowance = self.calculate_repair_allowance()
        self.mortgage_payment = self.calculate_mortgage_payment()
        self.void_costs = self.calculate_void_costs()

    def calculate_management(self):
        """Calculate the management costs."""
        management = self.management_rate * self.property.monthly_rent
        return management

    def calculate_mortgage_payment(self):
        """Calculate the monthly mortgage payment."""
        monthly_mortgage_payment = (self.interest_rate * self.property.mortgage) / 12
        return monthly_mortgage_payment

    def calculate_repair_allowance(self):
        """Calculate the repair allowance."""
        monthly_repair_allowance = self.repairs * self.property.monthly_rent
        return monthly_repair_allowance

    def calculate_void_costs(self):
        """Calculate the void costs."""
        monthly_void_allowance = (self.void_weeks) * (self.property.monthly_rent / 4)
        return monthly_void_allowance
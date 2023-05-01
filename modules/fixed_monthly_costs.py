# FIXED MONTHLY EXPENSES
# Outline the fixed monthly expenses

class FixedMonthExp:
    """Overall class to manage the property fixed monthly expenses."""

    def __init__(self, service_charge, ground_rent, insurance, bills, other_expenses):
        """Initialize the property fixed monthly expenses."""
        self.service_charge = service_charge
        self.ground_rent = ground_rent
        self.insurance = insurance
        self.bills = bills
        self.other_expenses = other_expenses

        self.service_charge_payment = self.calculate_service_charge_payment()
        self.ground_rent_payment = self.calculate_ground_rent_payment()
        self.insurance_payment = self.calculate_insurance_payment()
        self.bills_payment = self.calculate_bills_payment()
        self.other_expenses_payment = self.calculate_other_expenses_payment()

    def calculate_service_charge_payment(self):
        """Calculate the service charge payment."""
        return self.service_charge

    def calculate_ground_rent_payment(self):
        """Calculate the ground rent payment."""
        return self.ground_rent

    def calculate_insurance_payment(self):
        """Calculate the insurance payment."""
        return self.insurance

    def calculate_bills_payment(self):
        """Calculate the bills payment."""
        return self.bills

    def calculate_other_expenses_payment(self):
        """Calculate the other expenses payment."""
        return self.other_expenses

# LTV TARGET TO ADJUST RISK

class LTVTarget:
    """An overall class to analyze monthly savings need to hit a new target LTV."""

    def __init__(self, property, target_LTV):
        """Initialize the original property values."""
        self.property = property
        self.target_LTV = target_LTV

        self.target_mortgage = self.calculate_target_borrowed_mortgage()
        self.target_adjusted_mortgage = self.calculate_target_adjusted_mortgage()

    def calculate_target_borrowed_mortgage(self):
        """Calculate the target borrowed mortgage."""
        target_mortgage = self.property.purchase_price * self.target_LTV
        return target_mortgage
 
    def calculate_target_adjusted_mortgage(self):
        """Calculate the target adjusted mortgage."""
        target_adjusted_mortgage = self.target_mortgage - self.property.mortgage
        return target_adjusted_mortgage
    
    def calculate_savings_new_LTV(self, months):
        """Calculate the monthly savings needed to reach the new target LTV."""
        if self.target_adjusted_mortgage >= 0:
            return 0

        if months in [12, 24, 36, 48, 60]:
            monthly_savings = abs(self.target_adjusted_mortgage / months)
            return monthly_savings
        else:
            raise ValueError("Invalid number of months. Accepted values are 12, 24, 36, 48, and 60.")


        

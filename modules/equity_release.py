class EquityRelease:
    """An overall class to asses equity release and new ROI metrics."""

    def __init__(self, property, equity_LTV, remortgage_price):
        """Initialize the new property values."""
        self.property = property
        self.equity_LTV = equity_LTV
        self.remortgage_price = remortgage_price

    def calculate_equity_release(self):
        self.equity_available = (self.remortgage_price * self.equity_LTV) - self.property.mortgage
        return self.equity_available

    def new_cash_invested(self):
        original_cash_invested = sum([
            self.property.deposit,
            self.property.stamp_duty,
            self.property.renovation,
            self.property.legal_fees,
            self.property.furnishing,
            self.property.mortgage_fees
        ])
        self.new_total_cash_invested = original_cash_invested - self.equity_available
        return self.new_total_cash_invested

    def updated_roi(self):
        self.new_equity_update_roi = (self.property.annual_net_income / self.new_total_cash_invested) * 100
        return self.new_equity_update_roi
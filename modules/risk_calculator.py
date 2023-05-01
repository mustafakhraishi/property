# RISK CALCULATOR
class RiskCalculator:
    """An overall class to assess the affect of interest rates and LTVs on the monthly cashflow."""

    def __init__(self, property, var_monthly_expenses, fixed_monthly_costs, risk_interest_rate, risk_LTV):
        """Initialize the original property values"""
        self.property = property
        self.var_monthly_expenses = var_monthly_expenses
        self.fixed_monthly_costs = fixed_monthly_costs
        self.risk_interest_rate = risk_interest_rate
        self.risk_LTV = risk_LTV

        self.risk_mortgage = self.new_borrowed()
        self.mortgage_difference = self.adjusted_borrowed()
        self.annual_mortgage_payment_risk = self.new_annual_mortgage_payments()
        self.monthly_mortgage_payment_risk = self.new_monthly_mortgage_payments()
        self.new_monthly_cash_position = self.new_monthly_cashflow()


    def new_borrowed(self):
        """Calculate the new mortgage based on the new LTV."""
        self.risk_mortgage = self.property.purchase_price * self.risk_LTV
        return self.risk_mortgage

    def adjusted_borrowed(self):
        """Calculate the difference between the old and new mortgages."""
        self.mortgage_difference = self.property.mortgage - self.risk_mortgage
        return self.mortgage_difference

    def new_annual_mortgage_payments(self):
        """Calculate the new risk adjsuted annual mortgage payments."""
        self.annual_mortgage_payment_risk = self.risk_mortgage * self.risk_interest_rate
        return self.annual_mortgage_payment_risk
    
    def new_monthly_mortgage_payments(self):
        """Calculate the new risk adjsuted monthly mortgage payments."""
        self.monthly_mortgage_payment_risk = self.annual_mortgage_payment_risk / 12
        return self.monthly_mortgage_payment_risk

    def new_monthly_cashflow(self):
        """Calculate the new monthly cash flow excluding the original mortgage payment."""
        total_monthly_expenses = (
            self.var_monthly_expenses.management_fees +
            self.var_monthly_expenses.repair_allowance +
            # Remove original mortgage payment and add new
            self.monthly_mortgage_payment_risk +
            self.var_monthly_expenses.void_costs +
            self.fixed_monthly_costs.service_charge_payment +
            self.fixed_monthly_costs.ground_rent_payment +
            self.fixed_monthly_costs.insurance_payment +
            self.fixed_monthly_costs.bills_payment +
            self.fixed_monthly_costs.other_expenses_payment
        )
        self.new_monthly_cash_position = self.property.monthly_rent - total_monthly_expenses
        return self.new_monthly_cash_position
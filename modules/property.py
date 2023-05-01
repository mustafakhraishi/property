# PROPERTY EVAL. DOCUMENT
# Create a class to represent the whole assessment

class Property:
    """An overall class to manage the property assessment"""

    def __init__(self, purchase_price, renovation, legal_fees, furnishing, mortgage_fees, monthly_rent, LTV, first_time_buyer):
        """Initialize the evaluation process and output the key metrics"""

        # Input variables
        self.purchase_price = purchase_price
        self.renovation = renovation
        self.legal_fees = legal_fees
        self.furnishing = furnishing
        self.mortgage_fees = mortgage_fees
        self.monthly_rent = monthly_rent
        self.LTV = LTV / 100
        self.first_time_buyer = first_time_buyer
        
        self.annual_gross_rent = self.calculate_annual_gross_rent()        
        self.mortgage = self.calculate_mortgage()
        self.deposit = self.calculate_deposit()
        self.stamp_duty = self.calculate_stamp_duty()
        
    def calculate_annual_gross_rent(self):
        """
        Calculate the annual gross rent based on the monthly rent.
        """
        return self.monthly_rent * 12

    def total_cash_invested(self):
        """Calculate the total cash invested using deposit and stamp duty from Property object."""
        self.cash_invested = self.deposit + self.stamp_duty + self.renovation + self.legal_fees + self.furnishing + self.mortgage_fees
        return self.cash_invested

    def annual_cash_flow(self, var_monthly_expenses, fixed_monthly_costs):
        """Calculate the annual cash flow using variable and fixed monthly expenses."""
        total_monthly_expenses = (
        var_monthly_expenses.management_fees +
        var_monthly_expenses.repair_allowance +
        var_monthly_expenses.mortgage_payment +
        var_monthly_expenses.void_costs +
        fixed_monthly_costs.service_charge_payment +
        fixed_monthly_costs.ground_rent_payment +
        fixed_monthly_costs.insurance_payment +
        fixed_monthly_costs.bills_payment +
        fixed_monthly_costs.other_expenses_payment
    )
        self.annual_rent = self.monthly_rent * 12
        self.annual_expenses = total_monthly_expenses * 12
        self.annual_net_income = self.annual_rent - self.annual_expenses
        return self.annual_net_income

    
    def annual_cash_flow_business_tax(self):
        """Calculate annual cash flow after business tax."""
        self.cash_flow_business_tax = self.annual_net_income * (1 - 0.19)
        return self.cash_flow_business_tax

    def annual_cash_flow_tax_adjusted(self):
        """Calculate annual cash flow after user-defined tax rate."""
        tax_percentage = 0.45  # Set the tax rate to 45%
        self.cash_flow_tax_adjusted = self.annual_net_income * (1 - tax_percentage)
        return self.cash_flow_tax_adjusted
    
    def monthly_cash_flow(self, var_monthly_expenses, fixed_monthly_costs):
        """Calculate the monthly cash flow using variable and fixed monthly expenses."""
        total_monthly_expenses = (
            var_monthly_expenses.management_fees +
            var_monthly_expenses.repair_allowance +
            var_monthly_expenses.mortgage_payment +
            var_monthly_expenses.void_costs +
            fixed_monthly_costs.service_charge_payment +
            fixed_monthly_costs.ground_rent_payment +
            fixed_monthly_costs.insurance_payment +
            fixed_monthly_costs.bills_payment +
            fixed_monthly_costs.other_expenses_payment
        )
        return self.monthly_rent - total_monthly_expenses
    
    def calculate_mortgage(self):
        """Calculate the total mortgage costs."""
        return self.purchase_price * self.LTV

    def calculate_deposit(self):
        """Calculate the total deposit amount."""
        deposit = self.purchase_price - (self.purchase_price * self.LTV)
        return deposit
    
    def calculate_stamp_duty(self):
        """Calculate the total stamp duty costs."""
        purchase_price = self.purchase_price

        if self.first_time_buyer:
            if purchase_price <= 425000:
                return 0
            elif purchase_price <= 625000:
                return (purchase_price - 425000) * 0.05
            else:
                # Property value > 625000, no relief, continue with standard calculation
                pass
                    
        if purchase_price > 1500000:
            duty = (purchase_price - 1500000) * 0.12
        else:
            duty = 0

        if purchase_price > 925000:
            duty += min(1500000 - 925000, purchase_price - 925000) * 0.1

        if purchase_price > 250000:
            duty += min(925000 - 250000, purchase_price - 250000) * 0.05

        if self.first_time_buyer:
            return duty
        else:
            if purchase_price > 125000:
                duty += min(250000 - 125000, purchase_price - 125000) * 0.02

            if purchase_price > 39999:
                duty += purchase_price * 0.03

            return duty

    def gross_yield(self):
        """Calculate the gross yield as a percentage of the property's purchase price."""
        return (self.annual_gross_rent / self.purchase_price) * 100

    def net_yield(self):
        """Calculate the net yield as a percentage of the property's purchase price."""
        return (self.annual_net_income / self.purchase_price) * 100

    def roi(self):
        """Calculate the return on investment as a percentage of the cash invested."""
        return (self.annual_net_income / self.cash_invested) * 100
    
    def roi_tax_adjusted(self):
        """Calculate the tax-adjusted return on investment as a percentage of the cash invested."""
        cash_flow_diff = abs(self.cash_flow_business_tax - self.cash_flow_tax_adjusted)
        self.roi_tax_diff = (cash_flow_diff / self.cash_invested) * 100
        return self.roi_tax_diff

    def oer(self):
        """Calculate the operating expense ratio as a percentage of the annual gross rent."""
        return (self.annual_expenses / self.annual_gross_rent) * 100
    
    def icr(self, var_monthly_expenses):
        """Calculate the interest coverage ratio."""
        annual_mortgage_interest_payments = var_monthly_expenses.mortgage_payment * 12
        return self.annual_gross_rent / annual_mortgage_interest_payments

    def s_icr(self):
        """Calculate the stress interest coverage ratio."""
        stress_rate = 0.05
        return self.annual_gross_rent / (self.mortgage * stress_rate)
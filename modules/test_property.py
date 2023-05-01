from property import Property
from var_monthly_expenses import MonthlyExpenses
from fixed_monthly_costs import FixedMonthExp

from max_spend import calculate_max_spend
from risk_calculator import RiskCalculator
from ltv_target import LTVTarget
from equity_release import EquityRelease

# Create a Property object with sample data
property1 = Property(
    purchase_price=205000,
    renovation=0,
    legal_fees=0,
    furnishing=0,
    mortgage_fees=4305,
    monthly_rent=1150,
    LTV=0.7
)

# Create an Assumptions object with sample data
var_monthly_expenses1 = MonthlyExpenses(
    property=property1,
    interest_rate=0.0489,
    management_rate=0.09,
    repairs=0,
    void_weeks=0,
)

# Create a FixedMonthExp object with sample data
fixed_monthly_costs1 = FixedMonthExp(
    service_charge=1984,
    ground_rent=0,
    insurance=0,
    bills=0,
    other_expenses=0,
)


# Create a RiskCalculator object with sample data
risk_calculator1 = RiskCalculator(
    property=property1,
    var_monthly_expenses=var_monthly_expenses1,
    fixed_monthly_costs=fixed_monthly_costs1,
    risk_interest_rate=0.06,  # For example, a 6% interest rate
    risk_LTV=0.75,  # For example, a 75% LTV
)

# Create a LTVTarget object with sample data
ltv_target1 = LTVTarget(
    property=property1,
    target_LTV=0.75,  # For example, a 60% target LTV
)

# Create an EquityRelease object with sample data
equity_release1 = EquityRelease(
    property=property1,
    equity_LTV=0.75,  # For example, a 75% LTV
    remortgage_price=220000,  # For example, a new remortgage price of 220,000
)


# Print the mortgage and stamp duty costs for the property
print("\nMortgage cost: ", property1.mortgage)
print("Deposit: ", property1.deposit)
print("Stamp duty: ", property1.stamp_duty)

# Print the management fees, repair allowance, mortgage payment, and void costs
print("\nManagement fees: ", var_monthly_expenses1.management_fees)
print("Repair allowance: ", var_monthly_expenses1.repair_allowance)
print("Mortgage payment: ", var_monthly_expenses1.mortgage_payment)
print("Void costs: ", var_monthly_expenses1.void_costs)

# Print the service charge, ground rent, insurance, bills, and other expenses
print("\nService charge payment: ", fixed_monthly_costs1.service_charge_payment)
print("Ground rent payment: ", fixed_monthly_costs1.ground_rent_payment)
print("Insurance payment: ", fixed_monthly_costs1.insurance_payment)
print("Bills payment: ", fixed_monthly_costs1.bills_payment)
print("Other expenses payment: ", fixed_monthly_costs1.other_expenses_payment)

# Calculate the total cash invested
total_cash_invested = property1.total_cash_invested()
print("\nTotal cash invested: ", total_cash_invested)

# Calculate the annual cash flow
annual_cash_flow = property1.annual_cash_flow(var_monthly_expenses1, fixed_monthly_costs1)
print("\nAnnual cash flow: ", annual_cash_flow)

# Calculate the annual cash flow business tax
annual_cash_flow_business_tax = property1.annual_cash_flow_business_tax()
print("Annual Cash Flow Business Tax: ", annual_cash_flow_business_tax)

# Calculate the annual cash flow tax adjusted
annual_cash_flow_tax_adjusted_value = property1.annual_cash_flow_tax_adjusted()
print("Annual Cash Flow Tax Adjusted: ", annual_cash_flow_tax_adjusted_value)

# Calculate the monthly cash flow
monthly_cash_flow = property1.monthly_cash_flow(var_monthly_expenses1, fixed_monthly_costs1)
print("\nMonthly cash flow: ", monthly_cash_flow)


# Calculate the monthly gross yield
print("\nGross Yield: ", property1.gross_yield())

# Calculate the monthly net yield
print("Net Yield: ", property1.net_yield())

# Calculate the ROI
print("ROI: ", property1.roi())

# Calculate the ROI
print("OER: ", property1.oer())

# Calculate the ICR
print("ICR: ", property1.icr(var_monthly_expenses1))

# Calculate the S-ICR
print("S-ICR: ", property1.s_icr())

# Calculate the ROI tax adjusted
roi_tax_adjusted_value = property1.roi_tax_adjusted()
print("ROI Tax Adjusted: ", roi_tax_adjusted_value)


# Calculate the maximum spend based on the desired gross yield
max_spend = calculate_max_spend(property1)
print("Maximum Spend: ", max_spend)

# Test RiskCalculator functions
print("\nRisk adjusted mortgage: ", risk_calculator1.new_borrowed())
print("Mortgage difference: ", risk_calculator1.adjusted_borrowed())
print("Risk adjusted annual mortgage payments: ", risk_calculator1.new_annual_mortgage_payments())
print("Risk adjusted monthly mortgage payments: ", risk_calculator1.new_monthly_mortgage_payments())
print("New monthly cash flow: ", risk_calculator1.new_monthly_cashflow())


# Print the target borrowed mortgage and target adjusted mortgage
print("\nTarget borrowed mortgage: ", ltv_target1.target_mortgage)
print("Target adjusted mortgage: ", ltv_target1.target_adjusted_mortgage)

# Calculate and print the monthly savings needed to reach the new target LTV
for months in [12, 24, 36, 48, 60]:
    print(f"\nMonthly savings needed for {months} months: ", ltv_target1.calculate_savings_new_LTV(months))


# Print the calculated equity release
equity_release_amount = equity_release1.calculate_equity_release()
print("\nEquity release amount: ", equity_release_amount)

# Print the new total cash invested
new_total_cash_invested = equity_release1.new_total_cash_invested
print("New total cash invested: ", new_total_cash_invested)

# Print the updated ROI
updated_roi = equity_release1.updated_roi()
print("Updated ROI: ", updated_roi)
import json
from flask import render_template, jsonify, request, redirect, url_for, session
from modules.property import Property
from modules.var_monthly_expenses import MonthlyExpenses
from modules.fixed_monthly_costs import FixedMonthExp
from modules.equity_release import EquityRelease
from modules.max_spend import calculate_max_spend
from modules.risk_calculator import RiskCalculator
from modules.ltv_target import LTVTarget
from utils import get_objects_from_session
from app import app

@app.route('/')
def index():
    """
    Renders the property index page.
    """
    return render_template('property_index.html')


@app.route('/', methods=['GET', 'POST'])
def property_form():
    """
    Renders the property form page and processes the form data when submitted.
    """
    if request.method == 'POST':
        # Extract form data
        property_data = {
        'purchase_price': float(request.form['purchase_price']),
        'renovation': float(request.form['renovation']),
        'legal_fees': float(request.form['legal_fees']),
        'furnishing': float(request.form['furnishing']),
        'mortgage_fees': float(request.form['mortgage_fees']),
        'monthly_rent': float(request.form['monthly_rent']),
        'LTV': float(request.form['LTV']),
        'first_time_buyer': True if 'first_time_buyer' in request.form else False
        }
        var_monthly_expenses_data = {
            'interest_rate': float(request.form['interest_rate']),
            'management_rate': float(request.form['management_rate']),
            'repairs': float(request.form['repairs']),
            'void_weeks': int(request.form['void_weeks'])
        }
        fixed_monthly_costs_data = {
            'service_charge': float(request.form['service_charge']),
            'ground_rent': float(request.form['ground_rent']),
            'insurance': float(request.form['insurance']),
            'bills': float(request.form['bills']),
            'other_expenses': float(request.form['other_expenses'])
        }

        # Create a dictionary with the extracted data
        data = {
            'property': property_data,
            'var_monthly_expenses': var_monthly_expenses_data,
            'fixed_monthly_costs': fixed_monthly_costs_data
        }

        # Convert the dictionary to a JSON object and store it in the session
        session['json_data'] = json.dumps(data)

        return redirect(url_for('results'))  # Redirect to results page

    return render_template('property_index.html')

########################################################### KEY METRICS ###########################################################

@app.route('/results')
def results():
    """
    Renders the results page with the calculated metrics.
    """
    # Retrieve the JSON object from the session and convert it to a dictionary
    data = json.loads(session.get('json_data'))

    # Instantiate objects using the data dictionary
    property_data = {k: v for k, v in data['property'].items() if k != 'first_time_buyer'}
    property_obj = Property(first_time_buyer=data['property']['first_time_buyer'], **property_data)
    monthly_expenses_obj = MonthlyExpenses(property_obj, **data['var_monthly_expenses'])
    fixed_monthly_costs_obj = FixedMonthExp(**data['fixed_monthly_costs'])

    # Calculate metrics using instantiated objects
    total_cash_invested = property_obj.total_cash_invested()
    annual_cash_flow = property_obj.annual_cash_flow(monthly_expenses_obj, fixed_monthly_costs_obj)    
    annual_cash_flow_tax_adjusted = property_obj.annual_cash_flow_tax_adjusted()
    annual_cash_flow_business_tax = property_obj.annual_cash_flow_business_tax()
    monthly_cash_flow = property_obj.monthly_cash_flow(monthly_expenses_obj, fixed_monthly_costs_obj)
    gross_yield = property_obj.gross_yield()
    net_yield = property_obj.net_yield()
    roi = property_obj.roi()
    roi_tax_adjusted = property_obj.roi_tax_adjusted()
    oer = property_obj.oer()
    icr = property_obj.icr(monthly_expenses_obj)
    s_icr = property_obj.s_icr()
    mortgage = property_obj.calculate_mortgage()
    deposit = property_obj.calculate_deposit()
    stamp_duty = property_obj.calculate_stamp_duty()
    
    service_charge_payment = fixed_monthly_costs_obj.calculate_service_charge_payment()
    ground_rent_payment = fixed_monthly_costs_obj.calculate_ground_rent_payment()
    insurance_payment = fixed_monthly_costs_obj.calculate_insurance_payment()
    bills_payment = fixed_monthly_costs_obj.calculate_bills_payment()
    other_expenses_payment = fixed_monthly_costs_obj.calculate_other_expenses_payment()
    
    mortgage_payment = monthly_expenses_obj.calculate_mortgage_payment()
    management_fees = monthly_expenses_obj.calculate_management()
    repair_allowance = monthly_expenses_obj.calculate_repair_allowance()
    void_costs = monthly_expenses_obj.calculate_void_costs()

    # Render the results page with the calculated metrics
    return render_template('results.html',
                           property_obj=property_obj,
                           monthly_expenses_obj=monthly_expenses_obj,
                           fixed_monthly_costs_obj=fixed_monthly_costs_obj,
                           total_cash_invested=total_cash_invested,
                           annual_cash_flow=annual_cash_flow,
                           annual_cash_flow_tax_adjusted=annual_cash_flow_tax_adjusted,
                           annual_cash_flow_business_tax=annual_cash_flow_business_tax,
                           monthly_cash_flow=monthly_cash_flow,
                           gross_yield=gross_yield,
                           net_yield=net_yield,
                           roi=roi,
                           roi_tax_adjusted=roi_tax_adjusted,
                           oer=oer,
                           icr=icr,
                           s_icr=s_icr,
                           mortgage=mortgage,
                           deposit=deposit,
                           stamp_duty=stamp_duty,
                           service_charge_payment=service_charge_payment,
                           ground_rent_payment=ground_rent_payment,
                           insurance_payment=insurance_payment,
                           bills_payment=bills_payment,
                           other_expenses_payment=other_expenses_payment,
                           mortgage_payment=mortgage_payment,
                           management_fees=management_fees,
                           repair_allowance=repair_allowance,
                           void_costs=void_costs)


########################################################### EQUITY RELEASE ###########################################################

@app.route('/equity-release', methods=['GET', 'POST'])
def equity_release():
    """
    Render the equity release template with the property object and its annual net income.
    """
    # Retrieve objects from session
    property_obj, monthly_expenses_obj, fixed_monthly_costs_obj = get_objects_from_session()
    
    # Calculate and set the annual_net_income attribute for the Property object
    property_obj.annual_net_income = property_obj.annual_cash_flow(monthly_expenses_obj, fixed_monthly_costs_obj)
    
    # Render the equity release template with the Property object
    return render_template('equity_release.html', property_obj=property_obj)

@app.route('/api/update_results', methods=['POST'])
def update_results():
    """
    Update the results after calculating the equity release, new cash invested, and updated ROI.
    """
    # Get the request data
    data = request.json

    # Retrieve objects from session
    property_obj, monthly_expenses_obj, fixed_monthly_costs_obj = get_objects_from_session()

    # Calculate and set the annual_net_income attribute for the Property object
    property_obj.annual_net_income = property_obj.annual_cash_flow(monthly_expenses_obj, fixed_monthly_costs_obj)

    # Create an EquityRelease object with the updated data
    equity_obj = EquityRelease(property_obj, data['equity_LTV'], data['remortgage_price'])

    # Calculate the equity release, new cash invested, and updated ROI
    equity_release = equity_obj.calculate_equity_release()
    new_cash_invested = equity_obj.new_cash_invested()
    updated_roi = equity_obj.updated_roi()

    # Return the updated results as a JSON object
    return jsonify({
        'equity_release': equity_release,
        'new_cash_invested': new_cash_invested,
        'updated_roi': updated_roi
    })
    
########################################################### MAX SPEND ###########################################################

@app.route('/max-spend-calculator', methods=['GET', 'POST'])
def max_spend_calculator():
    if request.method == 'POST':
        # Extract form inputs
        monthly_rent = float(request.form['monthly_rent'])
        desired_gross_yield = float(request.form['desired_gross_yield'])

        # Calculate the maximum spend
        max_spend = calculate_max_spend(monthly_rent, desired_gross_yield)

        # Return the result as JSON
        return jsonify({'max_spend': max_spend})

    return render_template('risk_assessment.html')   
    
########################################################### RISK ASSESSMENT ###########################################################

@app.route('/risk-assessment')
def risk_assessment():
    # Retrieve objects from session
    property_obj, monthly_expenses_obj, fixed_monthly_costs_obj = get_objects_from_session()

    # Extract the values
    monthly_rent = property_obj.monthly_rent
    original_borrowed = property_obj.calculate_mortgage()
    monthly_costs = property_obj.monthly_cash_flow(monthly_expenses_obj, fixed_monthly_costs_obj)

    # Pass the values to the render_template function
    return render_template('risk_assessment.html', monthly_rent=monthly_rent, original_borrowed=original_borrowed, monthly_costs=monthly_costs)


@app.route('/risk-calculator', methods=['POST'])
def risk_calculator():
    # Retrieve objects from session
    property_obj, monthly_expenses_obj, fixed_monthly_costs_obj = get_objects_from_session()

    data = request.get_json()
    risk_interest_rate = float(data['risk_interest_rate'])
    risk_LTV = float(data['risk_LTV'])

    risk_calculator_obj = RiskCalculator(property_obj, monthly_expenses_obj, fixed_monthly_costs_obj, risk_interest_rate, risk_LTV)

    return jsonify({
        'new_borrowed': risk_calculator_obj.risk_mortgage,
        'adjusted_borrowed': risk_calculator_obj.mortgage_difference,
        'annual_mortgage_payment': risk_calculator_obj.annual_mortgage_payment_risk,
        'monthly_mortgage_payment': risk_calculator_obj.monthly_mortgage_payment_risk,
        'monthly_cashflow': risk_calculator_obj.new_monthly_cash_position
    })
    

@app.route('/ltv-target', methods=['POST'])
def ltv_target():
    # Retrieve objects from session
    property_obj, _, _ = get_objects_from_session()

    # Get the request data
    data = request.json
    target_LTV = float(data['target_LTV'])

    # Create an LTVTarget object with the updated data
    ltv_target_obj = LTVTarget(property_obj, target_LTV)

    # Calculate the savings for each time period
    savings = {}
    for months in [12, 24, 36, 48, 60]:
        savings[f'saving_{months}_months'] = ltv_target_obj.calculate_savings_new_LTV(months)

    # Return the updated results as a JSON object
    return jsonify({
        'target_borrowed': ltv_target_obj.target_mortgage,
        'ltv_adjusted_borrowed': ltv_target_obj.target_adjusted_mortgage,
        **savings
    })
    
if __name__ == '__main__':
    app.run(debug=True)
import json
from modules.property import Property
from modules.var_monthly_expenses import MonthlyExpenses
from modules.fixed_monthly_costs import FixedMonthExp
from flask import session

def get_objects_from_session():
    """Retrieves Property, MonthlyExpenses, and FixedMonthExp objects from the session data."""
    json_data = session.get('json_data')
    data = json.loads(json_data)

    property_obj = Property(
        purchase_price=data['property']['purchase_price'], 
        renovation=data['property']['renovation'],
        legal_fees=data['property']['legal_fees'], 
        furnishing=data['property']['furnishing'],
        mortgage_fees=data['property']['mortgage_fees'], 
        monthly_rent=data['property']['monthly_rent'], 
        LTV=data['property']['LTV'],
        first_time_buyer=data['property']['first_time_buyer']
    )

    monthly_expenses_obj = MonthlyExpenses(
        property_obj, 
        interest_rate=data['var_monthly_expenses']['interest_rate'],
        management_rate=data['var_monthly_expenses']['management_rate'], 
        repairs=data['var_monthly_expenses']['repairs'],
        void_weeks=data['var_monthly_expenses']['void_weeks']
    )

    fixed_monthly_costs_obj = FixedMonthExp(
        service_charge=data['fixed_monthly_costs']['service_charge'], 
        ground_rent=data['fixed_monthly_costs']['ground_rent'],
        insurance=data['fixed_monthly_costs']['insurance'], 
        bills=data['fixed_monthly_costs']['bills'],
        other_expenses=data['fixed_monthly_costs']['other_expenses']
    )

    return property_obj, monthly_expenses_obj, fixed_monthly_costs_obj
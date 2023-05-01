# MAXIMUM SPEND CALCULATOR

def calculate_max_spend(gross_annual_rent, desired_gross_yield=0):
    """
    A function to obtain the max spend given a desired gross yield.
    """
    if desired_gross_yield == 0:
        return 0

    max_spend = gross_annual_rent / (desired_gross_yield / 100)
    return max_spend
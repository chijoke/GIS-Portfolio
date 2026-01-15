def calculate_land_value(area_sq_m, price_per_sq_m):
    """
    Calculates total property value for local GIS surveys.
    Inputs: area_sq_m (float), price_per_sq_m (float)
    Returns: total_value (float)
    """
    # 1. THE PRO CHECK (Error Handling)
    if area_sq_m <= 0 or price_per_sq_m <= 0:
        return "Error: Area and price must be positive numbers."

    # 2. THE LOCAL LOGIC
    total_value = area_sq_m * price_per_sq_m
    
    return f"Total Value: ₦{total_value:,.2f}" # Professional formatting with Naira

# 3. THE ACTION (Testing it)
print(calculate_land_value(500, 15000)) # Example for a 500sqm plot in Lagos
def dms_to_decimal(degrees, minutes, seconds):
    """
    Converts DMS to Decimal Degrees for spatial analysis.
    Pro-Feature: Validates input to ensure minutes and seconds are realistic.
    """
    # STREET-WISE ERROR HANDLING: Minutes and Seconds cannot be 60 or more
    if not (0 <= minutes < 60) or not (0 <= seconds < 60):
        return "Error: Minutes and seconds must be between 0 and 59.99"

    if degrees < 0:
        result = degrees - (minutes / 60) - (seconds / 3600)
    else:
        result = degrees + (minutes / 60) + (seconds / 3600)
    
    return round(result, 6) # Professional standard is 6 decimal places



# --- ACTION: APPLIED TO NIGERIA ---
# Coordinates for a point in Lagos Island (approx)
lagos_dms = '''6° 26' 37"''' 

# Extracting and converting
parts = lagos_dms.replace('°', '').replace("'", "").replace('"', "").split()

# The Action: Running the tool
result = dms_to_decimal(float(parts[0]), float(parts[1]), float(parts[2]))
print(f"Lagos Decimal Degrees: {result}")

# The Street-Wise Hemisphere Check
if result > 0:
    hemisphere = "North"
else:
    hemisphere = "South"

print(f"The location is in the {hemisphere} hemisphere.")
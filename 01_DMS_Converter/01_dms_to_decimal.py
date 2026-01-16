def dms_to_decimal(degrees, minutes, seconds):
    if degrees < 0:
          result = degrees - minutes/60 - seconds/3600
    else:
          result = degrees + minutes/60 + seconds/3600
    return result

coordinate = '''37° 46' 26.2992"'''

# Add the code below to extract the parts from the coordinate string,
# call the function to convert to decimal degrees and print the result
# The expected answer is 37.773972

def dms_to_decimal(degrees, minutes, seconds):
     """ Convert DMS to Decimal Degrees for spatial Analysis."""
     if degrees < 0:
          result = degrees - minutes/60 - seconds/3600
     else:
          result = degrees + minutes/60 + seconds/3600
     return result

# --- SOLUTION -----
coordinate = '''37° 46' 26.2992"'''
#Cleaning the string to get just numbers 
clean_coord = coordinate.replace('°', ' ').replace("'", "").replace('"', "")
parts = clean_coord.split()  # Splits into ['37', '46', '26.2992']

# Convert strings to floats
d = float(parts[0])
m = float(parts[1])
s = float(parts[2])

decimal_degree = dms_to_decimal(d, m, s)
print(f"Decimal Result: {decimal_degree}")

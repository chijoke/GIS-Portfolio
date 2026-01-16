import math

class GeoConverter:
    """
    Professional utility for geospatial coordinate transformations.
    Standardizes DMS to Decimal Degrees (DD) conversion.
    """

    @staticmethod
    def dms_to_dd(degrees: float, minutes: float, seconds: float) -> float:
        """
        Converts Degrees Minutes Seconds to Decimal Degrees.
        Formula: DD = d + (m/60) + (s/3600)
        """
        # 1. Validation: Avoid bad data, code don't break my downstream analysis
        if not (0 <= minutes < 60):
            raise ValueError(f"Invalid minutes ({minutes}). Must be 0-59.")
        if not (0 <= seconds < 60):
            raise ValueError(f"Invalid seconds ({seconds}). Must be 0-59.")
        if not (-180 <= degrees <= 180):
            raise ValueError(f"Degrees ({degrees}) out of global range.")

        # 2. Logic: Handle negative degrees (South/West) correctly
        # The absolute value ensures the math works before re-applying the sign
        decimal = abs(degrees) + (minutes / 60.0) + (seconds / 3600.0)
        
        return round(decimal if degrees >= 0 else -decimal, 8)

    @staticmethod
    def get_hemisphere(lat: float, lon: float) -> str:
        """Determines the global quadrant."""
        ns = "North" if lat >= 0 else "South"
        ew = "East" if lon >= 0 else "West"
        return f"{ns}, {ew}"

def main():
    print("--- Pro Geo-Coordinate Converter ---")
    try:
        # Example: Input Latitude
        print("\nEnter Latitude:")
        d = float(input("  Degrees: "))
        m = float(input("  Minutes: "))
        s = float(input("  Seconds: "))
        lat_dd = GeoConverter.dms_to_dd(d, m, s)

        # Example: Input Longitude
        print("\nEnter Longitude:")
        d_lon = float(input("  Degrees: "))
        m_lon = float(input("  Minutes: "))
        s_lon = float(input("  Seconds: "))
        lon_dd = GeoConverter.dms_to_dd(d_lon, m_lon, s_lon)

        # Output Results
        print("\n" + "="*30)
        print(f"Decimal Degrees: {lat_dd}, {lon_dd}")
        print(f"Quadrant:        {GeoConverter.get_hemisphere(lat_dd, lon_dd)}")
        print("="*30)

    except ValueError as e:
        print(f"\n[!] Data Entry Error: {e}")
    except Exception as e:
        print(f"\n[!] Unexpected System Error: {e}")

if __name__ == "__main__":
    main()
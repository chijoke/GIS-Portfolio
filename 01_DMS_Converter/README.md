# DMS to Decimal Degree Converter (pro)

A high-precision geospatial utility built to demonstrate **defensive programming** and **object-oriented design** in Python.

## My Mission
Most beginner scripts are fragile. This project was built to explore how professional developers handle "dirty data" and ensure mathematical precision in GIS (Geographic Information Systems) applications.



## Key Features
* **Input Validation:** The system rejects unrealistic minutes/seconds (e.g., 61 minutes) before they reach the math engine.
* **Architectural Structure:** Uses a `GeoConverter` class with `@staticmethods` for modular, reusable code.
* **Type Safety:** Implements Python Type Hinting (`-> float`) to ensure data integrity across the pipeline.
* **Global Accuracy:** Precision-tuned to 8 decimal places (millimeter-level accuracy).

##  How It Works
The core logic handles the conversion while maintaining the correct sign for Northern/Southern and Eastern/Western hemispheres.

```python
from converter import GeoConverter

# Example: Convert 34° 15' 30"
result = GeoConverter.dms_to_dd(34, 15, 30)
print(f"Decimal Degrees: {result}")

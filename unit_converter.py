import streamlit as st

# Conversion dictionary
conversions = {
    "meter": ["kilometer", "centimeter", "millimeter", "foot", "yard"],
    "kilometer": ["meter", "mile"],
    "centimeter": ["meter", "inch", "yard"],
    "millimeter": ["meter"],
    "inch": ["centimeter"],
    "foot": ["meter", "yard"],
    "yard": ["meter", "foot", "centimeter"],
    "mile": ["kilometer"]
}

# Function to convert units
def convert_units(value, unit_from, unit_to):
    conversion_factors = {
        "meter_kilometer": 0.001, "kilometer_meter": 1000,
        "meter_centimeter": 100, "centimeter_meter": 0.01,
        "meter_millimeter": 1000, "millimeter_meter": 0.001,
        "inch_centimeter": 2.54, "centimeter_inch": 0.393701,
        "foot_meter": 0.3048, "meter_foot": 3.28084,
        "yard_meter": 0.9144, "meter_yard": 1.09361,
        "yard_foot": 3, "foot_yard": 0.333333,
        "mile_kilometer": 1.60934, "kilometer_mile": 0.621371,
        "yard_centimeter": 91.44, "centimeter_yard": 0.0109361
    }
    
    key = f"{unit_from}_{unit_to}"
    
    if unit_from == unit_to:
        return value  # If the units are the same, return the original value
    
    if key in conversion_factors:
        return value * conversion_factors[key]
    
    return "Invalid conversion: Units are not compatible"

# Streamlit UI
st.title("Unit Converter")

value = st.number_input("Enter the value you want to convert", step=1.0)

# Select "Convert from" unit
unit_from = st.selectbox("Convert from", list(conversions.keys()))

# Filter "Convert to" options based on the selected "Convert from" unit
unit_to = st.selectbox("Convert to", conversions[unit_from])

if st.button("Convert"):
    result = convert_units(value, unit_from, unit_to)
    st.write(f"{value} {unit_from} is equal to {result} {unit_to}")

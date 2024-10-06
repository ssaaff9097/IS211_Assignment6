class ConversionNotPossible(Exception):
    pass

def convert(fromUnit, toUnit, value):
    if fromUnit == "Celsius" and toUnit == "Kelvin":
        return value + 273.15
    elif fromUnit == "Celsius" and toUnit == "Farenheit":
        return (value * 9/5) + 32
    elif fromUnit == "Farenheit" and toUnit == "Celsius":
        return (value - 32) * 5/9
    elif fromUnit == "Farenheit" and toUnit == "Kelvin":
        return (value - 32) * 5/9 + 273.15
    elif fromUnit == "Kelvin" and toUnit == "Celsius":
        return value - 273.15
    elif fromUnit == "Kelvin" and toUnit == "Farenheit":
        return (value - 273.15) * 9/5 + 32
    
    if fromUnit == "Miles" and toUnit == "Yards":
        return value * 1760
    elif fromUnit == "Miles" and toUnit == "Meters":
        return value * 1609.34
    elif fromUnit == "Yards" and toUnit == "Miles":
        return value / 1760
    elif fromUnit == "Yards" and toUnit == "Meters":
        return value * 0.9144
    elif fromUnit == "Meters" and toUnit == "Miles":
        return value / 1609.34
    elif fromUnit == "Meters" and toUnit == "Yards":
        return value / 0.9144
    if fromUnit == toUnit:
        return value 
    raise ConversionNotPossible(f"Conversion from {fromUnit} to {toUnit} is not possible.")

def test_convert_temperature():
    test_cases = [
        ("Celsius", "Kelvin", 0.0, 273.15),
        ("Celsius", "Farenheit", 0.0, 32.0),
        ("Farenheit", "Celsius", 32.0, 0.0),
        ("Farenheit", "Kelvin", 32.0, 273.15),
        ("Kelvin", "Celsius", 273.15, 0.0),
        ("Kelvin", "Farenheit", 273.15, 32.0),
    ]
    for fromUnit, toUnit, value, expected in test_cases:
        result = convert(fromUnit, toUnit, value)
        print(f"Converting {value} {fromUnit} to {toUnit}: Expected {expected}, got {result}")

def test_convert_distance():
    test_cases = [
        ("Miles", "Meters", 1.0, 1609.34),
        ("Miles", "Yards", 1.0, 1760.0),
        ("Meters", "Miles", 1609.34, 1.0),
        ("Meters", "Yards",0.9144, 1.0),
        ("Yards", "Miles", 1760.0, 1.0),
        ("Yards", "Meters", 1.0, 0.9144),
    ]
    for fromUnit, toUnit, value, expected in test_cases:
        result = convert(fromUnit, toUnit, value)
        print(f"Converting{value} {fromUnit} to {toUnit}: Expected {expected}, got {result}")

def test_convert_incompatible_units():
    try:
        convert("Celsius", "Miles", 1.0)
    except ConversionNotPossible as e:
        print(e)
    try:
        convert("Farenheit", "Yards", 1.0)
    except ConversionNotPossible as e:
        print(e)

if __name__ == "__main__":
    test_convert_temperature()
    test_convert_distance()
    test_convert_incompatible_units() 
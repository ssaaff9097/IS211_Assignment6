
def convertCelsiusToKelvin(celsius):
    """Takes in a float representing a Celsius measurement, and returns that temperature converted into Kelvins"""
    kelvins = 0
    
    return kelvins


def convertCelsiusToFarenheit(celsius):
    """Takes in a float representing a Celsius measurement, and returns that temperature converted into Fahrenheit"""
    fahrenheit = 0
    
    return fahrenheit

def test_convertCelsiusToKelvin():
    test_cases = [
        (0.0, 273.15),
        (100.0, 373.15),
        (300, 573.15),
        (-273.15, 0.0),
        (25.0, 298.15),
    ]

    for celsius, expected in test_cases:
        result = convertCelsiusToKelvin(celsius)
        print(f"Converting {celsius}C to Kelvin: Expected {expected}, got {result}")

def test_convertCelsiusToFarenheit():
    test_cases = [
        (0.0, 32.0),
        (100.0, 212.0),
        (300.0, 572.0),
        (-40.0, -40.0),
        (25.0, 77.0),
    ]

    for celsius, expected in test_cases:
        result = convertCelsiusToFarenheit(celsius)
        print(f"Converting {celsius} to Farenheit: Expected {expected}, got {result}")


if __name__ == "__main__":
    test_convertCelsiusToKelvin()
    test_convertCelsiusToFarenheit() 

""" Part 2"""

def convertCelsiusToKelvin(celsius): 
    return celsius + 273.15

def convertCelsiusToFarenheit(celsius):
    return (celsius * 9/5) + 32

def test_convertCelsiusToKelvin():
    test_cases = [
        (0.0, 273.15),
        (100.0, 373.15),
        (300.0, 573.15),
        (-273.15, 0.0),
        (25.0, 298.15),
    ]
    for celsius, expected in test_cases:
        result = convertCelsiusToKelvin(celsius)
        print(f"Converting {celsius}C to Kelvin, Expected {expected}, got {result}")

def test_convertCelsiusToFarenheit():
    test_cases = [
        (0.0, 32.0),
        (100.0, 212.0),
        (300.0, 572.0),
        (-40.0, -40.0),
        (25.0, 77.0),
    ]

    for celsius, expected in test_cases:
        result = convertCelsiusToFarenheit(celsius)
        print(f"Converting {celsius}C to Farenheit, Expected {expected}, got {result}")

if __name__ == "__main__":
    test_convertCelsiusToKelvin()
    test_convertCelsiusToFarenheit() 

def convertCelsiusToKelvin(celsius):
    return celsius + 273.15
def convertCelsiusToFarenheit(celsius):
    return (celsius * 9/5) + 32
def convertFarenheitToCelsius(farenheit):
    return (farenheit - 32) * 5/9
def convertFarenheitToKelvin(farenheit):
    celsius = convertFarenheitToCelsius(farenheit)
    return convertCelsiusToKelvin(celsius)
def convertKelvinToCelsius(kelvin):
    return kelvin - 273.15
def convertKelvinToFarenheit(kelvin):
    celsius = convertKelvinToCelsius(kelvin)
    return convertCelsiusToFarenheit(celsius)

def test_convertCelsiusToKelvin():
    test_cases = [
        (0.0, 273.15),
        (100.0, 3733.15),
        (300.0, 573.15),
        (-273.15, 0.0),
        (25.0, 298.15),
    ]
    for celsius, expected in test_cases:
        result = convertCelsiusToKelvin(celsius)
        print(f"Converting {celsius}C to Kelvin, expected {expected} got {result}")

def test_convertCelsiusToFarenheit():
    test_cases = [
        (0.0, 32.0),
        (100.0, 212.0),
        (300.0, 572.0),
        (-40.0, -40.0),
        (25.0, 77.0),
    ]
    for celsius, expected in test_cases:
        result = convertCelsiusToFarenheit(celsius)
        print(f"Converting {celsius}C to Farenheit, expected {expected}, got {result}")

def test_convertFarenheitToCelsius():
    test_cases = [
        (32.0, 0.0),
        (212.0, 100.0),
        (572.0, 300.0),
        (-40.0, -40.0),
        (77.0, 25.0),
    ]
    for farenheit, expected in test_cases:
        result = convertFarenheitToCelsius(farenheit)
        print(f"Converting {farenheit}F to Celsius, expected {expected}, got {result}")

def test_convertFarenheitToKelvin():
    test_cases = [
        (32.0, 273.15),
        (212.0, 373.15),
        (572.0, 573.15),
        (-40.0, 233.15),
        (77.0, 298.15),
    ]
    for farenheit, expected in test_cases:
        result = convertFarenheitToKelvin(farenheit)
        print(f"Converting {farenheit}F to Kelvin, expected {expected}, got {result}")

def test_convertKelvinToCelsius():
    test_cases = [
        (273.15, 0.0),
        (373.15, 100.0),
        (573.15, 300.0),
        (0.0, -273.15),
        (298.15, 25.0),
    ]
    for kelvin, expected in test_cases:
        result = convertKelvinToCelsius(kelvin)
        print(f"Converting {kelvin}K to Celsius: expected {expected}, got {result}")

def test_convertKelvinToFarenheit():
    test_cases = [
        (273.15, 32.0),
        (373.15, 212.0),
        (573.15, 572.0),
        (0.0, -459.67),
        (298.15, 77.0),
    ]
    for kelvin, expected in test_cases:
        result = convertKelvinToFarenheit(kelvin)
        print(f"Converting {kelvin}K to Farenheit: expected {expected}, got {result}")

if __name__ == "__main__":
    test_convertCelsiusToKelvin()
    test_convertCelsiusToFarenheit()
    test_convertFarenheitToCelsius()
    test_convertFarenheitToKelvin()
    test_convertKelvinToCelsius()
    test_convertKelvinToFarenheit()
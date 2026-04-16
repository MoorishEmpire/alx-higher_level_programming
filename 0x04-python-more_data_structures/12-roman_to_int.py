#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str):
        return 0
    roman_values = {"I": 1, "II": 2, "III": 3, "IV": 4, "V": 5,
                    "VI": 6, "VII": 7, "VIII": 8, "IX": 9,
                    "X": 10, "XX": 20, "XXX": 30, "XL": 40,
                    "L": 50, "LX": 60, "LXX": 70, "LXXX": 80, "XC": 90,
                    "C": 100, "CC": 200, "CCC": 300, "CD": 400,
                    "D": 500, "DC": 600, "DCCC": 700, "DCCC": 800, "CM": 900,
                    "M": 1000, "MM": 2000, "MMM": 3000}
    number = 0
    current = ""
    for c in roman_string:
        current += c
        if current not in roman_values:
            number += roman_values[current[:-1]]
            current = c
    number += roman_values[current]
    return number

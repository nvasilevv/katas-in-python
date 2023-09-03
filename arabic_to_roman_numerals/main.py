CONVERSION_FACTORS = [
    (1000, "M"),
    (900, "CM"),
    (500, "D"),
    (400, "CD"),
    (100, "C"),
    (90, "XC"),
    (50, "L"),
    (40, "XL"),
    (10, "X"),
    (9, "IX"),
    (5, "V"),
    (4, "IV"),
    (1, "I")
]

def convert_to_roman(number: int):
    if number == 0:
        return ""
    arabic, roman = [entry for entry in CONVERSION_FACTORS if entry[0] <= number][0]
    return roman + convert_to_roman(number - arabic)

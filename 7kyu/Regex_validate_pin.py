"""
Regex validate PIN code (7Kyu)
https://www.codewars.com/kata/55f8a9c06c018a0d6e000132


ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot contain anything but exactly 4 digits or exactly 6 digits.

If the function is passed a valid PIN string, return true, else return false.

Examples
"1234"   -->  true
"12345"  -->  false
"a234"   -->  false

def validate_pin(pin):
    return len(pin) in (4, 6) and pin.isdigit()
"""


def validate_pin(pin):
    print(type(pin))
    print(pin.isnumeric())
    return len(pin) == 4 or len(pin) == 6 if pin.isnumeric() else False

print(validate_pin("1234"))

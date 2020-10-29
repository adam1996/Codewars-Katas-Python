"""

Credit Card Mask (7Kyu)
https://www.codewars.com/kata/5412509bd436bd33920011bc

Usually when you buy something, you're asked whether your credit card number, phone number or answer to your most secret question is still correct.
 However, since someone could look over your shoulder, you don't want that shown on your screen. Instead, we mask it.

Your task is to write a function maskify, which changes all but the last four characters into '#'.

Examples
maskify("4556364607935616") == "############5616"
maskify(     "64607935616") ==      "#######5616"
maskify(               "1") ==                "1"
maskify(                "") ==                 ""

# "What was the name of your first pet?"
maskify("Skippy")                                   == "##ippy"
maskify("Nananananananananananananananana Batman!") == "####################################man!"
"""


# return masked string
def maskify(cc):
    return str(cc[-4:]) if len(str(cc)) <= 4 else "#" * (len(str(cc)) - 4) + str(cc[-4:])
            # Return last 4 digits if len() of cc is less than 4 digits, no need to mask.
            # When len() > 4 add hash simples in place of missing digits, leaving last 4 for id.
            # BETTER SOLUTION:
            # --> return "#"*(len(cc)-4) + cc[-4:]
            #       If cc is less than four then we're multiplying our # by zero or a negative number which disregards it. No need to check.

print(maskify("SF$SDfgsd2eA"))
